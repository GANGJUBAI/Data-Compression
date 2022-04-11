#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<pthread.h>

int length;
double **newArray;
int thread_count;

int cmpfunc (const void * a, const void * b) {
	return ( *(double*)a - *(double*)b );
}


//sort columns in ascending order
void *colSort(void* rank){
       long my_rank=(long)rank;
       int i,j;
       int local_r;
       int my_first_col;
       int my_last_col;
       int remainder;
       
       if(length > thread_count){
	       local_r=length/thread_count;
	       remainder= length %thread_count;
	       //printf("remainder is %d\n",remainder);	       
	       if(remainder ==0){
		  my_first_col=my_rank*local_r;
		  my_last_col=(my_rank+1)*local_r-1;
	       }
	       else{
		  if(0<= my_rank && my_rank<remainder){
		     my_first_col=my_rank*(local_r+1);
		     my_last_col=(my_rank+1)*(local_r+1)-1;	   
		  }
		  else{
		     my_first_col=remainder+my_rank*local_r;
		     my_last_col=remainder+(my_rank+1)*local_r-1;
		  }
	       
	       }
       }
       else{
	      local_r=1;
	      my_first_col=my_rank*local_r;
              my_last_col=(my_rank+1)*local_r-1;
       }

       for(int j=my_first_col;j<my_last_col+1;j++){
	       double t;
	       for(int m=length-1;m>0;m--)
	       {
		    for(int n=0;n<m;n++)
		    {
			  if(newArray[n][j]>newArray[n+1][j])
			  {
			      t=newArray[n][j];
			      newArray[n][j]=newArray[n+1][j];
			      newArray[n+1][j]=t;
			  }
		    } 
	       } 
      } 
}


//sort rows in ascending order
void *rowSort(void* rank){
       long my_rank=(long)rank;
       int i,j;
       int local_r;
       int my_first_row;
       int my_last_row;
       int remainder;
       
       if(length > thread_count){
	       local_r=length/thread_count;
	       remainder= length %thread_count;
	       //printf("remainder is %d\n",remainder);	       
	       if(remainder ==0){
		  my_first_row=my_rank*local_r;
		  my_last_row=(my_rank+1)*local_r-1;
	       }
	       else{
		  if(0<= my_rank && my_rank< remainder){
		     my_first_row=my_rank*(local_r+1);
		     my_last_row=(my_rank+1)*(local_r+1)-1;	   
		  }
		  else{
		     my_first_row=remainder+my_rank*local_r;
		     my_last_row=remainder+(my_rank+1)*local_r-1;
		  }
	       
	       }
       }
       else{
	      local_r=1;
	      my_first_row=my_rank*local_r;
              my_last_row=(my_rank+1)*local_r-1;
       }
       for(int j=my_first_row;j<my_last_row+1;j++){
  	   qsort(newArray[j], length, sizeof(double), cmpfunc);  
       }
}


double Median_Odd(double *Array,int dataLength){
  
  int fillNum;	
 // int length;
  int dataSize;
  double median;
  
  pthread_t *thread_handles;
  long thread;
  thread_count=32;
  thread_handles=(pthread_t *)malloc(thread_count*sizeof(pthread_t));
  

  length= ceill(sqrt(dataLength));

  //adjust length
  if(length % 2 == 0){
    length +=1;
  }
  dataSize=length*length;

  //compute number of fill block 
  fillNum = dataSize-dataLength;
  //printf("fillNum is %d\n",fillNum);

  double * tempArray=(double *)calloc(dataSize,sizeof(double));
    
  newArray=(double **)calloc(dataSize,sizeof(double));
   
  for(int i=fillNum; i<dataSize; i++){
	  tempArray[i]=Array[i-fillNum];
  }
  /*
  for(int i=0; i<length*length;i++){	  
	  printf("tempArray[%d]: %f\n",i,tempArray[i]);
  }*/
  for(int i=0; i<length;i++){
          newArray[i]= &tempArray[(int)length*i];
  }
  /*
  for(int i=0; i<length;i++){
 	for(int j=0; j<length;j++){
	  printf("newArray[%d][%d]: %f\n",i,j,newArray[i][j]);
          
	}
  }*/

//sort columns in ascending order
  for(thread=0; thread<thread_count;thread++){
 	pthread_create(&thread_handles[thread],NULL,colSort,(void*)thread);
  }
  for(thread=0; thread<thread_count;thread++){
  	pthread_join(thread_handles[thread],NULL);
  }
  
//sort rows in ascending order
  for(thread=0; thread<thread_count;thread++){
        pthread_create(&thread_handles[thread],NULL,rowSort,(void*)thread);
  }
  for(thread=0; thread<thread_count;thread++){
        pthread_join(thread_handles[thread],NULL);
  }

  //diagonalsort
  for(int k=0;k<length;k++){
	for(int i=0;i<length;i++){
	    for(int j=length-1;j>=0;j--){
			if (i + 1 < length && j-1 >-1 && newArray[i][j] > newArray[i+1][j-1]){
			double t = newArray[i][j];
			newArray[i][j] = newArray[i+1][j-1];
			newArray[i+1][j-1] = t;
			}
	    }
	}
  }

  median = newArray[(length-1)/2][(length-1)/2]; 

  free(tempArray);
  free(newArray);

  return median;
}



