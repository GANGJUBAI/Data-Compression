//Author: Fenfang Li
//@Time: 2022/12

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>

#define Eps 1e-15

#define _computeCnt(T) computeCnt$_##T##_$
#define computeCnt(T) _computeCnt(T)

////// Compute Cnt /////////////////////////////////////////////////////////////////////////////////////
#define _computeCnt_IMPL(T) 										\
void computeCnt(T)(T Array[], int groupNum, int dataLength, int *Cnt, double mean, double delta) { 	\
	for(int i=0;i<dataLength;i++){ 									\
		double offset = (Array[i]-mean)/delta; 							\
		if(offset <-3) Cnt[0]++; 								\
		else if(offset >3) Cnt[groupNum-1]++; 							\
		else Cnt[(int)(offset+4)]++; 								\
	}												\
}
#define computeCnt_IMPL(T) _computeCnt_IMPL(T)

computeCnt_IMPL(int);
computeCnt_IMPL(float);
computeCnt_IMPL(double);


////// MediandFind //////////////////////////////////////////////////////////////////////
#define _medianFind(T) medianFind$_##T##_$
#define medianFind(T) _medianFind(T)

#define _medianFind_IMPL(T) T medianFind(T)(T Array[], int groupNum,int dataLength){	\
	double var;								    	\
	double sum;								    	\
	double mean;								    	\
	double delta;								    	\
	double squareSum;							    		\
	int cdfSum=0;									\
	int *Cnt=(int*)calloc(groupNum,sizeof(int));						\
	sum=0;										\
	var=0;										\
	squareSum=0;									\
	for(int i=0;i< dataLength;i++){								\
		sum += Array[i];								\
	}										\
	mean=sum/dataLength;								\
	for(int i=0;i<dataLength;i++){								\
		var += (Array[i]-mean)*(Array[i]-mean);						\
	}										\
	delta=sqrt(var/dataLength);								\
	if(-Eps < delta && delta <Eps){								\
	      free(Cnt);									\
      	      return mean;									\
	}										\
											\
	computeCnt(T)(Array,groupNum,dataLength,Cnt,mean,delta);			\
											\
	int i;										\
	for(i=0;i<groupNum;i++){							\
		cdfSum+=Cnt[i];								\
		if(cdfSum>=dataLength/2) break;						\
	}										\
	free(Cnt);									\
	return mean+(i-3.5)*delta;							\
}

#define medianFind_IMPL(T) _medianFind_IMPL(T)

medianFind_IMPL(int);
medianFind_IMPL(float);
medianFind_IMPL(double);