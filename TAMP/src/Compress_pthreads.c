#include "sz.h"          
#include <stdio.h>
#include <stdlib.h>
#include "fpzip.h"       
#include "fpc.h"
#include "SPC.h"
#include <time.h>
#include<stdint.h>
#include<pthread.h>
#include <sys/time.h>

int cmpfunc (const void * a, const void * b) {
	return ( *(int*)a - *(int*)b );
}

int rows,cols,layers;
double *data,*C;
int thread_count; 

void* CreateCMP(void* rank){
       long my_rank=(long)rank;
       int i,j;
       int local_r=rows/thread_count;
       int my_first_row=my_rank*local_r;
       int my_last_row=(my_rank+1)*local_r-1;
       double *delta_X  =(double *)malloc(layers*sizeof(double));
       printf("this process %ld running \n",my_rank);

       for(i=my_first_row;i<=my_last_row;i++)
                for(j=0;j<cols;j++){
                        if(j==0)
                        {
                                //C[i*cols+j]=10;
                                for(int k=0;k<layers;k++){
                                        delta_X[k]=data[k*rows*cols+i*cols+j];
                                }
                                qsort(delta_X, layers, sizeof(double), cmpfunc);

                                C[i*cols+j]= delta_X[layers/2];

                        }
                        else
                        {
                                for(int k=0;k<layers;k++){
                                        delta_X[k]=data[k*rows*cols+i*cols+j-1]-data[k*rows*cols+i*cols+j];
                                }
                                qsort(delta_X, layers, sizeof(double), cmpfunc);
                                double median=delta_X[layers/2];
									
                                C[i*cols+j]= C[i*cols+j-1]-median;	
                        }
                }
       return NULL;
}



/* compress doubleing-point data */
	static size_t
compress(FPZ* fpz, const void* data)
{
	size_t size;
	//write header 
	if (!fpzip_write_header(fpz)) {
		fprintf(stderr, "cannot write header: %s\n", fpzip_errstr[fpzip_errno]);
		return 0;
	}
	//perform actual compression 
	size = fpzip_write(fpz, data);
	if (!size) {
		fprintf(stderr, "compression failed: %s\n", fpzip_errstr[fpzip_errno]);
		return 0;
	}
	return size;
}

/* perform compression, decompression, and validation of double array */
	static size_t
fpzip_double_array(const double* field, int nx, int ny, int nz, int prec)
{
	int status;
	int dims = (nz == 1 ? ny == 1 ? 1 : 2 : 3);
	size_t inbytes = nx * ny * nz * sizeof(double);
	size_t bufbytes = 1024 + inbytes;
	size_t outbytes = 0;
	void* buffer = malloc(bufbytes);
	char name[0x100];

	// compress to memory 
	FPZ* fpz = fpzip_write_to_buffer(buffer, bufbytes);
	fpz->type = FPZIP_TYPE_DOUBLE;
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

void  get_zordering_recipe(int *encode_recipe, int rows, int cols, int layers)
{
	int i,j,k;

	int z_size= EncodeMorton3(cols-1,rows-1,layers-1)+1;
	int *z_index=(int *)malloc(z_size*sizeof(int));
	for(k=0;k<z_size;k++){
		z_index[k]=-1;
	}

	int box_size=rows*cols*layers;
	for(k=0;k<layers;k++)
		for(j=0;j<cols;j++)
			for(i=0;i<rows;i++)

			{
				z_index[EncodeMorton3(j,i,k)]=j+i*cols+k*rows*cols;
			}
	int tr=0;
	for(k=0;k<z_size;k++){
		if(z_index[k]!=-1)
			encode_recipe[tr++]=z_index[k];
	}
	if(tr!=box_size){
		printf("tr!=box_size, %d, %d\n",tr,box_size);
		//for (k=0;k<box_size;k++)
		//	printf("%d ",encode_recipe[k]);
	}
	free(z_index);




}

void  get_hilbert_recipe(int *encode_recipe, int rows, int cols, int layers)
{
	int i,j,k;
        int box_size=rows*cols*layers;
	struct point * p_point=(struct point *)malloc(box_size*sizeof(struct point));
	array=p_point;
	int width=cols;
	int height=rows;
	int depth=layers;
	if (width >= height&&width >= depth)
		gilbert3d(0, 0, 0,
				width, 0, 0,
				0, height, 0,
				0, 0, depth);

	else if( height >= width && height >= depth)
		gilbert3d(0, 0, 0,
				0, height, 0,
				width, 0, 0,
				0, 0, depth);

	else
		gilbert3d(0, 0, 0,
				0, 0, depth,
				width, 0, 0,
				0, height, 0);
	for( i=0;i<box_size;i++)
	{
		encode_recipe[i]=p_point[i].x+p_point[i].y*cols+p_point[i].z*rows*cols;
	}
	free(p_point);



}
int main(int argc, char* argv[])
{

	size_t r5=0,r4=0,r3=0,r2=0,r1=0;
	char oriFilePath[640], outputFilePath[640];
	//clock_t start,end;
        timeval t_start, t_end;

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
	//int rows, cols,layers;
	rows=r2;cols=r1;
	layers=r3;
	int sizeN=rows*cols;
	int i,j;

	data =(double *)malloc(dataLength*sizeof(double));
	C =(double *)malloc(sizeN*sizeof(double));

	fread(data,dataLength,sizeof(double),fp);
	fclose(fp);





	int c_size_fpc;
	int c_size_fpzip;
	int dc_size_fpc;
	//raw fpc compression
/*	fp=fopen("ori","w");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}
	fwrite(data,dataLength, sizeof(double),fp);
	fclose(fp);



	fp=fopen("ori","r");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}

        c_size_fpc=FPC_Compress(20,fp);
	fclose(fp);
	printf("c_size_fpc is %d\n",c_size_fpc);
	printf("datalength is %f\n",(double)dataLength*sizeof(double));
	printf("fpc ori compression ratio=%lf\n",(double)dataLength*sizeof(double)/c_size_fpc);
        
	fp=fopen("result_ori.fpc","r");
        if(fp==NULL){
                printf("Cannot open file %s.fpc\n",oriFilePath);
                return 0;
        }

	dc_size_fpc=FPC_Decompress(fp);
        fclose(fp);
        printf("fpc ori decompression ratio=%lf\n",(double)dataLength*sizeof(double)/dc_size_fpc);
*/
	
        pthread_t *thread_handles;
	long thread;
	thread_count=2;

	thread_handles=(pthread_t *)malloc(thread_count*sizeof(pthread_t));
        

	gettimeofday( &t_start, NULL);
	for(thread=0; thread<thread_count;thread++){
	 pthread_create(&thread_handles[thread],NULL,CreateCMP,(void*)thread);
	}
        for(thread=0; thread<thread_count;thread++){
	  pthread_join(thread_handles[thread],NULL);
	}

	gettimeofday( &t_end, NULL);
        double delta_t = (t_end.tv_sec-t_start.tv_sec) + 
                    (t_end.tv_usec-t_start.tv_usec)/1000000.0;
	printf("pthreads time is %fms\n",delta_t*1000);

        

	double *datatrans =(double *)malloc(dataLength*sizeof(double));

        for(i=0;i<rows;i++)
                for(j=0;j<cols;j++)
                        for(int k=0;k<layers;k++)
                                datatrans[k*sizeN+i*cols+j]=data[k*sizeN+i*cols+j]-C[i*cols+j];
        
        
          
	fp=fopen("ori+","w");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}
	fwrite(datatrans,dataLength, sizeof(double),fp);
	fclose(fp);

	fp=fopen("ori+","r");
	if(fp==NULL){
		printf("Cannot open file %s.fpc\n",oriFilePath);
		return 0;
	}

	c_size_fpc=FPC_Compress(20,fp);
	fclose(fp);


	double *outdata =(double *)malloc(dataLength*sizeof(double));
	for(i=0;i<rows;i++)
                for(j=0;j<cols;j++)
                        for(int k=0;k<layers;k++)
                                outdata[k*sizeN+i*cols+j]=datatrans[k*sizeN+i*cols+j]+ C[i*cols+j];



        printf("c_size_fpc is %d\n",c_size_fpc);
        printf("datalength is %f\n",(double)dataLength*sizeof(double));
        printf("fpc ori compression ratio=%lf\n",(double)dataLength*sizeof(double)/c_size_fpc);

	
        fp=fopen("result_ori.fpc","r");
        if(fp==NULL){
                printf("Cannot open file %s.fpc\n",oriFilePath);
                return 0;
        }
        

        dc_size_fpc=FPC_Decompress(fp);
        fclose(fp);
	printf("fpc ori decompression ratio=%lf\n",(double)dataLength*sizeof(double)/dc_size_fpc);

   
	free(data);
	free(datatrans);
	free(outdata);
	free(C);
	free(thread_handles);
	remove("result_ori.fpc");
	return 0;
}
