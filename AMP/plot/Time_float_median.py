#Author: Fenfang Li
#@Time: 2022/12

import matplotlib.pyplot as plt
import numpy as np

import sys
import array
import os

#load data
name_hat = "./fig/"
#data1 = np.loadtxt("../src/results/Time_OridataSet_float_FPZIP.result.dat")
#data2 = np.loadtxt("../src/results/Time_OridataSet_float_FPZIP.result2.dat")
#data1 = np.hstack((data1, data2))

data3 = np.loadtxt("../src/results/Time_OridataSet_float_FPZIP+.result.dat")
data3 = data3.reshape(18,-1)
data4 = np.loadtxt("../src/results/Time_OridataSet_float_FPZIP+.result2.dat")
data4 = data4.reshape(6,-1)
#data3 = np.hstack((data3, data4)).reshape(24,-1)

data5 = np.loadtxt("../src/results/Time_OridataSet_float_FPZIP+approxiMedian.result1.dat")
data5 = data5.reshape(18,-1)
data6 = np.loadtxt("../src/results/Time_OridataSet_float_FPZIP+approxiMedian.result2.dat")
#data5 = np.hstack((data5, data6)).reshape(24,-1)
data6 = data6.reshape(6,-1)

#the range means the number of the dataset in one namelist
x=range(0,18)

datalist1 = ["CLOUD","P","PRECIP","QGRAUP",
           "QICE","QRAIN","QSNOW","QVAPOR","TC",
           "U","V","W","CLOUD.lg","PRECIP.lg",
           "QGRAUP.lg","QICE.lg","QRAIN.lg","QSNOW.lg"]

datalist2 = ["density_b","density_d","temp","velocity_x","velocity_y","velocity_z"]
#datalist =datalist1+datalist2

'''ori means baseline and unoptimized method
   FPZIP+ represents socc proposed method
   FPZIP+approxi represents our method
'''
#ori_FPZIP1 = data1[:,0]
#ori_FPZIP2 = data2[:,0]

FPZIP_median1 = data3[:,0]
FPZIP_compress1 =data3[:,1]
FPZIP_median2 = data4[:,0]
FPZIP_compress2 =data4[:,1]

FPZIP_approxi_median1 = data5[:,0]
FPZIP_approxi_compress1 = data5[:,1]
FPZIP_approxi_median2 = data6[:,0]
FPZIP_approxi_compress2 =data6[:,1]

#Get the Time of all datasets
fig = plt.figure(num=None,figsize=(16,6))
axis_font = {'size':'16'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'28'}

ind = np.arange(len(x))
width = 0.25

ax = fig.add_subplot(111)

#rects1 = ax.bar(ind-width, data1, width, color='#7ED0F8',label="FPZIP",edgecolor='#FFF0F5')
rects2 = ax.bar(ind-width, FPZIP_compress1, width, color='#7ED0F8',label="FPZIP+comp",edgecolor='#FFF0F5')
rects3 = ax.bar(ind-width, FPZIP_median1, width,bottom=FPZIP_compress1,  color='#FFDC7E',label="FPZIP+med",edgecolor='#FFF0F5')
rects4 = ax.bar(ind, FPZIP_approxi_compress1, width, color='#7ED0F8',label="FPZIP+approxi_comp",edgecolor='#FFF0F5')
rects5 = ax.bar(ind, FPZIP_approxi_median1, width, bottom=FPZIP_approxi_compress1,  color='#FAAA89',label="FPZIP+approxi_med",edgecolor='#FFF0F5')

ax.set_ylabel('Time (ms)',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( datalist1,rotation=90 )
ax.set_xlim([-0.5,17.6])

ax.legend(loc=2,ncol=2,  prop=font,bbox_to_anchor=(0.1, 1.32))
plt.savefig(name_hat+'Time_FPZIP_Hurricane.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


fig = plt.figure(num=None,figsize=(11,5))
axis_font = {'size':'14'}
plt.rc('xtick', labelsize=30)
plt.rc('ytick', labelsize=30)
font = {'size':'24'}
x=range(0,6)
ind = np.arange(len(x))
width = 0.18

ax = fig.add_subplot(111)

#rects5 = ax.bar(ind-width, data2, width, color='#7ED0F8',label="FPZIP",edgecolor='#FFF0F5')
rects6 = ax.bar(ind-width, FPZIP_compress2, width, color='#7ED0F8',label="FPZIP+comp",edgecolor='#FFF0F5')
rects7 = ax.bar(ind-width, FPZIP_median2,width, bottom=FPZIP_compress2,  color='#FFDC7E',label="FPZIP+med",edgecolor='#FFF0F5')
rects8 = ax.bar(ind, FPZIP_approxi_compress2, width, color='#7ED0F8',label="FPZIP+approxi_comp",edgecolor='#FFF0F5')
rects9 = ax.bar(ind, FPZIP_approxi_median2, width,bottom=FPZIP_approxi_compress2, color='#FAAA89',label="FPZIP+approxi_med",edgecolor='#FFF0F5')


ax.set_ylabel('Time (ms)',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( datalist2,rotation=90 )
ax.set_xlim([-0.5,5.6])

ax.legend(loc=2,ncol=2,  prop=font,bbox_to_anchor=(0, 1.3))
plt.savefig(name_hat+'Time_FPZIP_NYX.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
