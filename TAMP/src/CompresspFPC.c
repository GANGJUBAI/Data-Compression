#include "sz.h"          
#include <stdio.h>
#include <stdlib.h>
#include "SPC.h"
#include <time.h>
#include<stdint.h>
#include <sys/time.h>
#include "pfpc.h"

int main(int argc, char* argv[])
{

	size_t r5=0,r4=0,r3=0,r2=0,r1=0;
	char oriFilePath[640], outputFilePath[640];
	//clock_t start,end;
        struct timeval start, end;
	
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

	//sprintf(outputFilePath, "%s.sz", oriFilePath);
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

	double *data =(double *)malloc(dataLength*sizeof(double));
	double *C =(double *)malloc(sizeN*sizeof(double));

	fread(data,dataLength,sizeof(double),fp);
	fclose(fp);



	int c_size_pfpc;
	int dc_size_fpc;

        gettimeofday( &start, NULL );
	fp=fopen("ori.pfpc","w");
	if(fp==NULL){
		printf("Cannot open file %s.pfpc\n",oriFilePath);
		return 0;
	}
	fwrite(data,dataLength, sizeof(double),fp);
	fclose(fp);



	fp=fopen("ori.pfpc","r");
	if(fp==NULL){
		printf("Cannot open file %s.pfpc\n",oriFilePath);
		return 0;
	}
        
        
        c_size_pfpc=pFPC_Compress(11,128,4,fp);

	gettimeofday( &end, NULL );
        double endtime=(double)1000 * (end.tv_sec - start.tv_sec) + ((end.tv_usec - start.tv_usec) / 1000.0);
        printf("time is %fms\n",endtime);
        
        fclose(fp);
//	printf("c_size_pfpc is %d\n",c_size_fpc);
//	printf("datalength is %f\n",(double)dataLength*sizeof(double));
	printf("pfpc ori compression ratio=%lf\n",(double)dataLength*sizeof(double)/c_size_pfpc);
        

	
	free(data);	
	remove("result_ori.pfpc");
	return 0;
}
