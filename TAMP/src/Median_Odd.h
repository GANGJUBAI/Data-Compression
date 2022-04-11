#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int cmpfunc (const void * a, const void * b) {
	return ( *(double*)a - *(double*)b );
}

double Median_Odd(double *Array,int dataLength){
  
  int fillNum;	
  int length;
  int dataSize;
  double median;

  length= ceill(sqrt(dataLength));

  //adjust length
  if(length % 2 == 0){
    length +=1;
  }
  dataSize=length*length;

  //compute number of fill block 
  fillNum = dataSize-dataLength;


  double * tempArray=(double *)calloc(dataSize,sizeof(double));
    
  double ** newArray=(double **)calloc(dataSize,sizeof(double));
   
  for(int i=fillNum; i<dataSize; i++){
	  tempArray[i]=Array[i-fillNum];
  }

  for(int i=0; i<length;i++){
          newArray[i]= &tempArray[(int)length*i];
  }

  
  //sort columns in ascending order
  for(int j=0;j<length;j++) 
    {
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

  
  //sort rows in ascending order
  for(int j=0;j<length;j++){
  	qsort(newArray[j], length, sizeof(double), cmpfunc);  
  }

  
  //diagonalsort
  for(int k=0;k<length;k++){
      for(int i=0;i<length;i++){
          for(int j=length-1;j>=0;j--){
	  			if (i + 1 < length && j-1 >-1 && newArray[i][j] > newArray[i+1][j-1]) {
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


