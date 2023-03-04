//Author: Fenfang Li
//@Time: 2023/3

#include "sz.h" 
#include <stdio.h>
#include <stdlib.h>
#include "fpzip.h"
#include "fpc.h"
#include "SPC/SPC.h"
#include "BFPRT_rand.h"
#include <sys/time.h>

using namespace std;
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
	buffer=NULL;

	return outbytes;
}


int main(int argc, char* argv[])
{

	size_t r5=0,r4=0,r3=0,r2=0,r1=0;
	char oriFilePath[640], outputFilePath[640], medianFilePath[640];
	struct timeval start, end;
	size_t dataLength ;
	int rows, cols,layers;
	int sizeN;

	if(argc < 3)
	{
		printf("Test case: testdouble_compress [srcFilePath] [dimension sizes...]\n");
		printf("Example: testdouble_compress testdouble_8_8_128.dat 8 8 128\n");
		exit(0);
	}
	sprintf(oriFilePath, "%s", argv[1]);
	if(argc>=3)
		r1 = atoi(argv[2]); //8
	if(argc>=4)
		r2 = atoi(argv[3]); //8
	if(argc>=5)
		r3 = atoi(argv[4]); //128

	sprintf(outputFilePath, "%s", oriFilePath);
	
	dataLength = computeDataLength(r5,r4,r3,r2,r1);
	rows=r2;
	cols=r1;
	layers=r3;
	sizeN=rows*cols;
	int i,j;


	float *data =(float *)malloc(dataLength*sizeof(float));	
	FILE *ori_fp=fopen(oriFilePath,"r");
	if(ori_fp==NULL){
		printf("Cannot open file %s.\n",oriFilePath);	
		return 0;
	}
	fread(data,dataLength,sizeof(float),ori_fp);
	fclose(ori_fp);
	ori_fp=NULL;

	int c_size_fpzip;
	const size_t m = layers/2;
	float *C =(float *)malloc(sizeN*sizeof(float));
	float *delta_X  =(float *)malloc(layers*sizeof(float));
	float median;

	gettimeofday(&start, NULL);
	for(i=0;i<rows;i++)
                for(j=0;j<cols;j++){
                        if(j==0)
                        {

                                for(int k=0;k<layers;k++){
                                        delta_X[k]=data[k*sizeN+i*cols+j];
                                }
				BFPRT(delta_X,0,layers,layers/2);
                                C[i*cols+j]= delta_X[layers/2-1];
                        }
                        else
                        {
                                for(int k=0;k<layers;k++){
                                        delta_X[k]=data[k*sizeN+i*cols+j-1]-data[k*sizeN+i*cols+j];
                                }
				BFPRT(delta_X,0,layers,layers/2);
                                median=delta_X[layers/2-1];

                                C[i*cols+j]= C[i*cols+j-1]-median;

                        }
                }
	gettimeofday(&end,NULL);
	double endtime=(double)1000 * (end.tv_sec - start.tv_sec) + ((end.tv_usec - start.tv_usec) / 1000.0);
	printf("fpzip ori+ BFPRT median time is %fms\n",endtime);
	
	gettimeofday(&start, NULL);
        for(i=0;i<rows;i++)
                for(j=0;j<cols;j++)
                        for(int k=0;k<layers;k++)
                                data[k*sizeN+i*cols+j]-= C[i*cols+j];
	gettimeofday(&end,NULL);
	endtime=(double)1000 * (end.tv_sec - start.tv_sec) + ((end.tv_usec - start.tv_usec) / 1000.0);
	printf("fpzip ori+ with BFPRT precondition time is %fms\n",endtime);

	
	gettimeofday( &start, NULL );
	c_size_fpzip=fpzip_float_array(data, dataLength, 1, 1, 32);
        gettimeofday(&end,NULL);
	endtime=(double)1000 * (end.tv_sec - start.tv_sec) + ((end.tv_usec - start.tv_usec) / 1000.0);
	printf("fpzip ori+ BFPRT compress time is %fms\n",endtime);
	printf("fpzip ori+ BFPRT compression ratio=%lf\n",(float)dataLength*sizeof(float)/c_size_fpzip);

	

	free(data);
	free(delta_X);
	free(C);
	data=NULL;
	delta_X=NULL;
	C=NULL;
	return 0;
}
