#include "sz.h"          
#include <stdio.h>
#include <stdlib.h>
#include "fpzip.h"       
#include "fpc.h"
#include "SPC.h"
#include <time.h>
#include<stdint.h>
#include "Median_Mean.h"
#include <sys/time.h>

int cmpfunc (const void * a, const void * b) {
	return ( *(int*)a - *(int*)b );
}

double RMSE(int rows,int cols,int layers,int sizeN,size_t datalength,double *dataori,double *datatrans){
  double sum=0;
  double rmse;
  double length =(double)datalength;
  int m=0,n0=0,n1=0,n3=0;
//  int p0=0,p01=0,p03=0,p06=0,p1=0,p3=0,p5=0;
 // double *data =(double *)malloc(datalength*sizeof(double));

 // FILE *fp ;
 /* fp=fopen("Data_Loss_Diffusity.dat","w");
  if(fp==NULL){
                printf("Cannot open Data_Loss_Diffusity file \n");
  }*/

  /*for(int i= 0;i<length;i++)
  {
    if(dataori[i]-datatrans[i] !=0)
          {
                      m++;
             if(dataori[i]-datatrans[i]>3.0)
                {
                    n++;
                    printf("dataori[%d] is %7f\n",i,dataori[i]-datatrans[i]);
                }


  }*/
  for(int i=0;i<rows;i++){
     for(int j=0;j<cols;j++){
       for(int k= 0;k<layers;k++){
	 /* if(k==1&&i==0&&j==0)
	  {
		  printf("data[1-0-0] is %20a\t,outdata[1-0-0] is %20a\n",dataori[0*sizeN+1*cols+111],datatrans[0*sizeN+1*cols+111]);

	  }*/
	 /* if((*(uint64_t*)&dataori[k*sizeN+i*cols+j] ^ *(uint64_t*)&dataori[k*sizeN+i*cols+j]) == 1)
	  {
		  m++;
	  }*/
	  if(dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j] <-1.0*pow(2,-1023) || dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j] >1.0*pow(2,-1023))
	  {
             	      m++;
             //data[k*sizeN+i*cols+j]=dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j];
	     if(fabs(dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])>0&&fabs(dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])<=1.0)
                {
                    n0++;
		   /* if(fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])>=0.0&&fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])<0.0000001)
                    {
                            p0++;
                    }
		    if(fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])>=0.0000001&&fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])<0.000001)
                    {
                            p01++;
                    }

		    if(fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])>=0.000001&&fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])<0.00001)
                    {
                            p03++;
                    }
		    if(fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])>=0.00001&&fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])<0.0001)
                    {
                            p06++;
                    }
		    if(fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])>=0.0001&&fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])<0.001)
                    {
                            p1++;
                    }

		   if(fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])>=0.001&&fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])<0.005)
                    {
                            p3++;
                    }

		    if(fabs((dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])/dataori[k*sizeN+i*cols+j])>=0.005)
	            {		   
			    p5++;
	            }*/
		 //  fprintf(fp,"dataori[%d-%d-%d] is %.15lf\n",k,i,j,dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j]);
                }
	     if(fabs(dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])>1.0&&fabs(dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])<=3.0)
                {
                    n1++;
		}
             if(fabs(dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j])>3.0)
		{     
		    n3++;
		   // fprintf(fp,"dataori[%d-%d-%d] is %7f\n",k,i,j,dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j]);
                    //printf("dataori[%d-%d-%d] is %7f\n",k,i,j,dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j]);
		}

          } 	  
          sum+=pow(dataori[k*sizeN+i*cols+j]-datatrans[k*sizeN+i*cols+j],2);
      }
     }
   }

 /* fp=fopen("Data_Loss_Viscocity.dat","w");
  if(fp==NULL){
                printf("Cannot open Data_Loss_Viscocity file \n");
  }
  fwrite(data,datalength, sizeof(double),fp);
  fclose(fp);
  */          
// printf("m is %d\n",m);
// printf("n0 is %d,n1 is %d,n3 is %d\n",n0,n1,n3);
  //printf("p0 is %d,p01 is %d,p03 is %d,p06 is %d,p1 is %d,p3 is %d,p5 is %d\n",p0,p01,p03,p06,p1,p3,p5);

  return rmse=sqrt(sum/length);
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

	double *data =(double *)malloc(dataLength*sizeof(double));
	double *C =(double *)malloc(sizeN*sizeof(double));

	fread(data,dataLength,sizeof(double),fp);
	fclose(fp);
        
//	printf("dataLength is %d\n",(int)dataLength);




	int c_size_fpc;
	int c_size_fpzip;
	int dc_size_fpc;

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
	
	double *delta_X  =(double *)malloc(layers*sizeof(double));
        int findMedianStage=0;
	double mean=0;
	double sigma=0;
	double mediantemp=0;

        gettimeofday( &start, NULL );
        //start=clock();
        for(i=0;i<rows;i++)
                for(j=0;j<cols;j++){
                        if(j==0)
                        {
                                //C[i*cols+j]=10;
                                for(int k=0;k<layers;k++){ 
                                        delta_X[k]=data[k*sizeN+i*cols+j];
                                }
				if(findMedianStage == 0){
				 mediantemp= medianFindStage1(delta_X,layers,8,&mean,&sigma);
				 findMedianStage=1;
				 //printf("delta:%.15f\n",delta);
				 //printf("mediantemp:%f\n",mediantemp);
				}
				else if(findMedianStage == 1)
				  mediantemp= medianFindStage2(delta_X,layers,8,&mean,&sigma);

                                //qsort(delta_X, layers, sizeof(double), cmpfunc);

                                //C[i*cols+j]= delta_X[layers/2];
				C[i*cols+j]=mediantemp;
                        }
                        else
                        {
                                for(int k=0;k<layers;k++){
                                        delta_X[k]=data[k*sizeN+i*cols+j-1]-data[k*sizeN+i*cols+j];
                                }
                                //qsort(delta_X, layers, sizeof(double), cmpfunc);
                                //double median=delta_X[layers/2];
									
                                //C[i*cols+j]= C[i*cols+j-1]-median;
				mediantemp =medianFindStage2(delta_X,layers,8,&mean,&sigma);
	
			        C[i*cols+j]=C[i*cols+j-1]-mediantemp;
                                //printf("%lf\n", C[i*cols+j]);

                        }
                }
        //end=clock();
        //double endtime=(double)(end-start)/CLOCKS_PER_SEC;
	//printf("time is %fms\n",endtime*1000);
        gettimeofday( &end, NULL );
        double endtime=(double)1000 * (end.tv_sec - start.tv_sec) + ((end.tv_usec - start.tv_usec) / 1000.0);
        printf("time is %fms\n",endtime);
	
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
	//end=clock();
	//double endtime=(double)(end-start)/CLOCKS_PER_SEC;

	//printf("fpc ori+ compression ratio=%lf\n",(double)dataLength*sizeof(double)/c_size_fpc);

	double *outdata =(double *)malloc(dataLength*sizeof(double));
	for(i=0;i<rows;i++)
                for(j=0;j<cols;j++)
                        for(int k=0;k<layers;k++)
                                outdata[k*sizeN+i*cols+j]=datatrans[k*sizeN+i*cols+j]+ C[i*cols+j];
	//double rmse=RMSE(dataLength,data,outdata);
	double rmse=RMSE(rows,cols,layers,sizeN,dataLength,data,outdata);


//        printf("RMSE is %.40lf\n",rmse);
//        printf("c_size_fpc is %d\n",c_size_fpc);
//        printf("datalength is %f\n",(double)dataLength*sizeof(double));
        printf("fpc ori compression ratio=%lf\n",(double)dataLength*sizeof(double)/c_size_fpc);
	//printf("compression is completed，time is：%f ms.\n",endtime*1000);

        //start=clock();	
        fp=fopen("result_ori.fpc","r");
        if(fp==NULL){
                printf("Cannot open file %s.fpc\n",oriFilePath);
                return 0;
        }
        

        dc_size_fpc=FPC_Decompress(fp);
        fclose(fp);
        //end=clock();
        //endtime=(double)(end-start)/CLOCKS_PER_SEC;
	//printf("fpc ori decompression ratio=%lf\n",(double)dataLength*sizeof(double)/dc_size_fpc);
        //printf("compression is completed，time is：%f ms.\n",endtime*1000);

	free(data);
	free(datatrans);
	free(outdata);
	free(C);
	remove("result_ori.fpc");
	return 0;
}
