//Author: Fenfang Li
//@Time: 2023/3

#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;
     	
template <typename T>
void swap(T A[],int a,int b){
  T temp=A[a];
  A[a]=A[b];
  A[b]=temp;
 }

template <typename T>
void Init(T* a,int l,int r)
{
    srand((int)time(NULL));
    int idx = rand()%(l-r)+l;
    swap(a[idx],a[l]);
    return;
}

template <typename T>
void Show(T* a,int n)
{
    for(int i=0;i<n;++i)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

template <typename T>
int BFPRT(T* a,int l,int r,int k)
{
    if(r-l == 1) return l;   //return the found number
    Init(a,l,r);
    T povit=a[l];
    int i=l,j=r;
    while(i<j)
    {
        do ++i; while(i+1 < r && a[i]<povit);
        do --j; while(a[j]>povit);
        if(i<j) swap(a[i],a[j]);
    }
    swap(a[l],a[j]);
    int num=j-l+1;  //Povit ranks in the current sequence 
    if(k == num) return j;
    else if(num > k) return BFPRT(a,l,j,k);
    else return BFPRT(a,j+1,r,k-num);
}

