#include "sz.h"
#include <stdio.h>
#include <stdlib.h>
#include "zfp.h"
#include "../util.h"
#include "fpzip.h"
#include "fpc.h"
#define ratioEB 0.00001

#define Threshold 0.95


int cmpfunc (const void * a, const void * b) {
	return ( *(int*)a - *(int*)b );
}
/* compress floating-point data */
	static size_t
compress(FPZ* fpz, const void* data)
{
	size_t size;
	/* write header */
	if (!fpzip_write_header(fpz)) {
		fprintf(stderr, "cannot write header: %s\n", fpzip_errstr[fpzip_errno]);
		return 0;
	}
	/* perform actual compression */
	size = fpzip_write(fpz, data);
	if (!size) {
		fprintf(stderr, "compression failed: %s\n", fpzip_errstr[fpzip_errno]);
		return 0;
	}
	return size;
}

/* perform compression, decompression, and validation of float array */
	static size_t
fpzip_float_array(const float* field, int nx, int ny, int nz, int prec)
{
	int status;
	int dims = (nz == 1 ? ny == 1 ? 1 : 2 : 3);
	size_t inbytes = nx * ny * nz * sizeof(float);
	size_t bufbytes = 1024 + inbytes;
	size_t outbytes = 0;
	void* buffer = malloc(bufbytes);
	char name[0x100];

	/* compress to memory */
	FPZ* fpz = fpzip_write_to_buffer(buffer, bufbytes);
	fpz->type = FPZIP_TYPE_FLOAT;
	fpz->prec = prec;
	fpz->nx = nx;
	fpz->ny = ny;
	fpz->nz = nz;
	fpz->nf = 1;
	outbytes = compress(fpz, field);
	status = (0 < outbytes && outbytes <= bufbytes);
	fpzip_write_close(fpz);

	free(buffer);

	return outbytes;
}
int main(int argc, char* argv[])
{

	size_t r5=0,r4=0,r3=0,r2=0,r1=0;
	char oriFilePath[640], outputFilePath[640];

	if(argc < 3)
	{
		printf("Test case: testfloat_compress [srcFilePath] [dimension sizes...]\n");
		printf("Example: testfloat_compress testfloat_8_8_128.dat 8 8 128\n");
		exit(0);
	}
	sprintf(oriFilePath, "%s", argv[1]);
	if(argc>=3)
		r1 = atoi(argv[2]); //8
	if(argc>=4)
		r2 = atoi(argv[3]); //8
	if(argc>=5)
		r3 = atoi(argv[4]); //128
	if(argc>=6)
		r4 = atoi(argv[5]);
	if(argc>=7)
		r5 = atoi(argv[6]);
	sprintf(outputFilePath, "%s.sz", oriFilePath);
	FILE *fp=fopen(oriFilePath,"r");
	if(fp==NULL){
		printf("Cannot open file %s.\n",oriFilePath);	
		return 0;
	}
	size_t dataLength = computeDataLength(r5,r4,r3,r2,r1);
	int rows, cols,layers;
	rows=r2;cols=r1;
	layers=r3;
	int sizeN=rows*cols;
	int i,j;

	float *data =(float *)malloc(dataLength*sizeof(float));
	float *C =(float *)malloc(sizeN*sizeof(float));

	float max=-100000000;
	float min=100000000;
	fread(data,dataLength,sizeof(float),fp);
	fclose(fp);
	for(i=0;i<dataLength;i++){
		//		fscanf(fp,"%lf",&data[i]);	
		if(data[i]>max)
			max=data[i];
		if(data[i]<min)
			min=data[i];
	}

	//	double EB=(max-min)*ratioEB;
	float EB=max*ratioEB;
	char *confFile = "sz.config";
	SZ_Init(confFile);
	confparams_cpr->absErrBound =EB;

	int c_size=0;

	size_t outSize;
	unsigned char *bytes = SZ_compress(SZ_FLOAT, data, &outSize, 0, 0, 0, 0,dataLength);
	c_size+=outSize;

	free(bytes);
	//	printf("timecost=%f\n",totalCost);

	int c_size_zfp=zfp1D_compress_float(data,dataLength,EB);
	//	int c_size_zfp=zfp3D_compress(data,cols,rows,layers,EB);


	printf("SZ compression ratio=%lf\n",(float)dataLength*sizeof(float)/c_size);
	printf("ZFP compression ratio=%lf\n",(float)dataLength*sizeof(float)/c_size_zfp);
	int c_size_fpzip=fpzip_float_array(data, dataLength, 1, 1, 32);
	printf("fpzip compression ratio=%lf\n",(float)dataLength*sizeof(float)/c_size_fpzip);

	fp=fopen(oriFilePath,"r");
	if(fp==NULL){
		printf("Cannot open file %s.\n",oriFilePath);
		return 0;
	}
	int c_size_fpc=FPC_Compress(20,fp);
	//printf("%d\n",dataLength);
	fclose(fp);
	printf("fpc compression ratio=%lf\n",(float)dataLength*sizeof(float)/c_size_fpc);

	float *delta_X  =(float *)malloc(layers*sizeof(float));
	for(i=0;i<rows;i++)
		for(j=0;j<cols;j++){
			if(j==0)
			{
				//C[i*cols+j]=10;
				for(int k=0;k<layers;k++){
					delta_X[k]=data[k*sizeN+i*cols+j];
				}
				qsort(delta_X, layers, sizeof(float), cmpfunc);

				C[i*cols+j]= delta_X[layers/2];
			}
			else
			{
				for(int k=0;k<layers;k++){
					delta_X[k]=data[k*sizeN+i*cols+j-1]-data[k*sizeN+i*cols+j];
				}
				qsort(delta_X, layers, sizeof(float), cmpfunc);
				float median=delta_X[layers/2];

				C[i*cols+j]= C[i*cols+j-1]-median;
				//printf("%lf\n", C[i*cols+j]);
				// printf("%lf\n", median);

			}
		}
	for(i=0;i<rows;i++)
		for(j=0;j<cols;j++)
			for(int k=0;k<layers;k++)
				data[k*sizeN+i*cols+j]-= C[i*cols+j]; 

	int delta_size=0;
	unsigned char *bytes_C = SZ_compress(SZ_FLOAT, C, &outSize, 0, 0, 0, 0,sizeN);
	delta_size+=outSize;

	free(bytes_C);

	unsigned char *bytes_delta = SZ_compress(SZ_FLOAT, data, &outSize, 0, 0, 0, 0,dataLength);
	delta_size+=outSize;


	free(bytes_delta);

	printf("SZ with reducedModel compression ratio=%lf\n",(float)dataLength*sizeof(float)/delta_size);


	//	int delta_size_zfp = zfp3D_compress(data,cols,rows,layers,EB);
	int delta_size_zfp = zfp1D_compress_float(data,dataLength,EB);
	delta_size_zfp += zfp1D_compress_float(C,cols*rows,EB);



	printf("ZFP with reducedModel compression ratio=%lf\n",(float)dataLength*sizeof(float)/delta_size_zfp);

	int delta_size_fpzip=fpzip_float_array(data, dataLength, 1, 1, 32);
	delta_size_fpzip += fpzip_float_array(C,cols*rows, 1, 1, 32);
	printf("fpzip with reducedModel compression ratio=%lf\n",(float)dataLength*sizeof(float)/delta_size_fpzip);

	fp=fopen("temp.fpc","w");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}
	fwrite(data,dataLength, sizeof(float),fp);
	fclose(fp);

	fp=fopen("temp.fpc","r");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}
	int delta_size_fpc=FPC_Compress(20,fp);
	fclose(fp);
	fp=fopen("C.fpc","w");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}
	fwrite(C,cols*rows, sizeof(float),fp);
	fclose(fp);

	fp=fopen("C.fpc","r");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}
	delta_size_fpc+=FPC_Compress(20,fp);
	fclose(fp);

	printf("fpc with reducedModel compression ratio=%lf\n",(float)dataLength*sizeof(float)/delta_size_fpc);

	free(data);
	free(C);
	free(delta_X);
	return 0;
}
