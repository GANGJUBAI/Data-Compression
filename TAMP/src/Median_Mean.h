#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define Eps 1e-15

void computeCnt(double *Array,int groupNum,int *Cnt,double mean,double delta){
  int dataLength;
  int groupLoc;
  
  dataLength=sizeof(Array);
  groupLoc=groupNum+3;

  for(int i=0;i<dataLength;i++){
    if(Array[i]<=(mean)){
      groupLoc=floor((double)(mean-Array[i])/delta);
      if(groupLoc < 2){
        if(groupLoc==0){
          groupLoc=floor((double)(mean-Array[i])*3/delta);
          Cnt[groupNum/2-groupLoc]++;
        }
        else Cnt[groupNum/2-2-groupLoc]++;
      }
      else Cnt[0]++;
    }
    else{
      groupLoc=floor((double)(Array[i]-mean)/delta);
      if(groupLoc < 2){
        if(groupLoc==0){
          groupLoc=floor((double)(Array[i]-mean)*3/delta);
          Cnt[groupNum/2+1+groupLoc]++;
        }
        else Cnt[groupNum/2+3+groupLoc]++;
      }
      else Cnt[groupNum+1]++;
    }
  }
}

double medianFindStage1(double *Array,size_t datalength,int groupNum,double *mean,double *delta){
  double var;
  double sum;
  double squareSum;
  int dataLength;
  int groupLoc;
  int leftsum;
  int *Cnt=(int *)calloc(groupNum+2,sizeof(int));
  
  //paramter initialization
  sum=0;
  var=0;
  leftsum=0;
  squareSum=0;
  groupLoc=groupNum+3;
  dataLength=(int)datalength;
  
  for(int i=0;i< dataLength;i++){
    sum += Array[i];
    squareSum +=Array[i]*Array[i];
  }

  *mean=(double)sum/dataLength;
  var=squareSum/dataLength-pow(*mean,2);
  *delta=pow(var,0.5);
  
  computeCnt(Array,groupNum,Cnt,*mean,*delta);
  free(Cnt);

  return (2*(*mean)-(*delta)/3)/2;//final median interval
}



double medianFindStage2(double *Array,size_t datalength,int groupNum,double *mean,double *delta){
  double var;
  double sum;
  double meanTemp;
  double deltaTemp;
  double squareSum;
  int dataLength;
  int deltaIndex;
  int groupLoc;
  int leftsum;
  int rightsum;
  int adjustIndex;
  int *Cnt=(int *)calloc(groupNum+2,sizeof(int));

  //parameter initialization
  sum=0;
  var=0;
  squareSum=0;
  leftsum=0;
  rightsum=0;
  adjustIndex=0;
  dataLength=(int)datalength;
  deltaIndex=0;
  groupLoc=groupNum+3;
  
  if(-Eps< *delta && *delta< Eps){
    deltaIndex=1;
    adjustIndex=1;
  }

  if(deltaIndex == 0){
	 for(int i=0;i< dataLength;i++){
	    //compute sum and squareSum currently 
	    sum += Array[i];
	    squareSum +=Array[i]*Array[i];
	    
	    // compute location of Arrays of elements in group
	    //and compute the count within each group
	    if(Array[i]<=(*mean)){
	      groupLoc=floor((double)(*mean-Array[i])/(*delta));
	      if(groupLoc < 2){
		if(groupLoc==0){
		  groupLoc=floor((double)(*mean-Array[i])*3/(*delta));
		  Cnt[groupNum/2-groupLoc]++;
		}
		else Cnt[groupNum/2-2-groupLoc]++;
	      }
	      else Cnt[0]++;
	    }
	    else{
	      groupLoc=floor((double)(Array[i]-*mean)/(*delta));
	      if(groupLoc < 2){
		if(groupLoc==0){
		  groupLoc=floor((double)(Array[i]-*mean)*3/(*delta));
		  Cnt[groupNum/2+1+groupLoc]++;
		}
		else Cnt[groupNum/2+3+groupLoc]++;
	      }
	      else Cnt[groupNum+1]++;
	    }  
	   }
  }
  else if(deltaIndex == 1){
    for(int i=0;i< dataLength;i++){
            //compute sum and squareSum currently 
            sum += Array[i];
            squareSum +=Array[i]*Array[i];
    }
  }
  
  //compute mean and delta currently
  meanTemp=(double)sum/dataLength;
  var=(double)squareSum/dataLength-pow(meanTemp,2);
  deltaTemp=pow(var,0.5);

  //determine the data distribution
  for(int i=0;i<groupNum/2+1;i++){
    leftsum +=Cnt[i];
    if(leftsum >=dataLength/2+2){
      adjustIndex=1;
     // printf("adjust\n");
      break;
    }
    rightsum +=Cnt[groupNum+1-i];
    if(rightsum >=dataLength/2+2){
      adjustIndex=1;
      //printf("adjust\n");
      break;
    }
  }

  if(adjustIndex == 0){
    for(int i=0;i <2;i++)
      if(Cnt[groupNum/2-i]!=0){
	free(Cnt);
	return (2*(*mean)-(*delta)*(i+1)/3)/2;//?
      }
  }
  
  if(adjustIndex ==1){
    //reset Cnt
    for(int i=0;i<groupNum+2;i++){
      Cnt[i]=0;
    }
    //printf("adjust\n");
    *mean=meanTemp;
    *delta=deltaTemp;
    if(-Eps< *delta && *delta< Eps){
      free(Cnt);
      return *mean;
    }
    else  computeCnt(Array,groupNum,Cnt,*mean,*delta);
    
    //find median interval
    for(int i=0;i <2;i++)
      if(Cnt[groupNum/2-i]!=0){
       free(Cnt);
       return (2*(*mean)-(*delta)*(i+1)/3)/2;
      }
  }//end if
}


