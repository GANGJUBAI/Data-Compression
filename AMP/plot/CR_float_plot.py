#Author: Fenfang Li
#@Time: 2022/12

import matplotlib.pyplot as plt
import numpy as np

import sys
import array
import os
import re

#load data
name_hat = "./fig/"

#load results from fpzip 
data1 = np.loadtxt("../src/results/OridataSet_float.result1.dat")   #Hurricane
data2 = np.loadtxt("../src/results/OridataSet_float.result2.dat")   #NYX
data3 = np.loadtxt("../src/results/NewdataSet_float.result1.dat")    #SCALE
data4 = np.loadtxt("../src/results/NewdataSet_float.result2.dat")   #CESM
data23 = np.hstack((data2,data3))

data1 = data1.reshape(-1,6)
data2 = data2.reshape(-1,6)
data3 = data3.reshape(-1,6)
data4 = data4.reshape(-1,6)
data23 = data23.reshape(-1,6)

data1_avg=np.average(data1,axis=0)
data2_avg=np.average(data2,axis=0)
data3_avg=np.average(data3,axis=0)
data4_avg=np.average(data4,axis=0)


#the range means the number of the dataset in one namelist
x1=range(0,20)
x2=range(0,6)
x3=range(0,12)
x4=range(0,33)


namelist1=["CLOUD","P","PRECIP","QCLOUD","QGRAUP",
           "QICE","QRAIN","QSNOW","QVAPOR","TC",
           "U","V","W","CLOUD.log","PRECIP.log",
           "QCLOUD.log","QGRAUP.log","QICE.log","QRAIN.log","QSNOW.log"]

namelist2=["density_b","density_d","temp","velocity_x","velocity_y","velocity_z"]

namelist3=["PRES","QG","QR","QV","T","V","QC","QI","QS","RH","U","W"]

namelist4=["CLDICE"," CONCLD"," ICIMR"," Q"," U",
           "VU"," CLDLIQ"," DCQ"," ICLDIWP"," QC",
            "UU"," VV"," CLOUD"," DTCOND"," ICLDTWP",
            "QRL"," V"," Z3"," CMFDQ"," DTV",
            "ICWMR"," QRS"," VD01"," CMFDQR"," FICE",
            "OMEGA"," RELHUM"," VQ"," CMFDT"," GCLDLWP",
            "OMEGAT"," T"," VT"]
namelist5=namelist2+namelist3

namelist=["Hurricane","NYX","SCALE","CESM"]
#ori means baseline and unoptimized methods
#for Hurricane
ori11 = data1[:,0]
ori12 = data1[:,1]
ori13 = data1[:,2]

#for NYX
ori21 = data2[:,0]
ori22 = data2[:,1]
ori23 = data2[:,2]

#for SCALE
ori31 = data3[:,0]
ori32 = data3[:,1]
ori33 = data3[:,2]

#for CESM
ori41 = data4[:,0]
ori42 = data4[:,1]
ori43 = data4[:,2]

#merge SCALE into NYX
ori51 = data23[:,0]
ori52 = data23[:,1]
ori53 = data23[:,2]

ori_avg1 = np.append(data1_avg[0],data2_avg[0])
ori_avg1 = np.append(ori_avg1,data3_avg[0])
ori_avg1 = np.append(ori_avg1,data4_avg[0])

ori_avg2 = np.append(data1_avg[1],data2_avg[1])
ori_avg2 = np.append(ori_avg2,data3_avg[1])
ori_avg2 = np.append(ori_avg2,data4_avg[1])

ori_avg3 = np.append(data1_avg[2],data2_avg[2])
ori_avg3 = np.append(ori_avg3,data3_avg[2])
ori_avg3 = np.append(ori_avg3,data4_avg[2])


#CMP represents our method
CMP1 = data1[:,3]
CMP2 = data2[:,3]
CMP3 = data3[:,3]
CMP4 = data4[:,3]
CMP5 = data23[:,3]

CMP_avg = np.append(data1_avg[3],data2_avg[3])
CMP_avg = np.append(CMP_avg,data3_avg[3])
CMP_avg = np.append(CMP_avg,data4_avg[3])


#Get the CR figure of ori methods

#FPZIP-Hurricane
fig = plt.figure(num=None,figsize=(16,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

ind = np.arange(len(x1))  # the x locations for the groups
width = 0.27       # the width of the bars

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori11, width, color='#F6B0A4',label="FPZIP+O")
rects2 = ax.bar(ind, ori12, width, color='#FED498',label="FPZIP+H")
rects3 = ax.bar(ind+width, ori13, width, color='#9E94B6',label="FPZIP+Z")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels(namelist1,rotation=90)

#xlim must match the x
ax.set_xlim([-0.5,19.5])

ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(.95, 1.35))
plt.savefig(name_hat+'SFC_float_FPZIP_Hurricane.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#FPZIP-NYX
fig = plt.figure(num=None,figsize=(12,4))   #NYX

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'28'}

ind = np.arange(len(x2))  # the x locations for the groups
width = 0.18       # the width of the bars

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori21, width, color='#F6B0A4',label="FPZIP+O")
rects2 = ax.bar(ind, ori22, width, color='#FED498',label="FPZIP+H")
rects3 = ax.bar(ind+width, ori23, width, color='#9E94B6',label="FPZIP+Z")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels(namelist2,rotation=90)

#xlim must match the x
ax.set_xlim([-0.5,5.5])

ax.legend(loc=1,ncol=3, prop=font,bbox_to_anchor=(1, 1.26))  #NYX
plt.savefig(name_hat+'SFC_float_FPZIP_NYX.pdf', format='pdf',bbox_inches="tight",pad_inches=0)

#For FPZIP-SCALE
fig = plt.figure(num=None,figsize=(16,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

ind = np.arange(len(x3))  # the x locations for the groups
width = 0.27       # the width of the bars

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori31, width, color='#F6B0A4',label="FPZIP+O")
rects2 = ax.bar(ind, ori32, width, color='#FED498',label="FPZIP+H")
rects3 = ax.bar(ind+width, ori33, width, color='#9E94B6',label="FPZIP+Z")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels(namelist3,rotation=90)

#xlim must match the x
ax.set_xlim([-0.5,11.5])

ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(.95, 1.35))
plt.savefig(name_hat+'SFC_float_FPZIP_SCALE.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#FPZIP-CESM
fig = plt.figure(num=None,figsize=(16,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

ind = np.arange(len(x4))  # the x locations for the groups
width = 0.27       # the width of the bars

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori41, width, color='#F6B0A4',label="FPZIP+O")
rects2 = ax.bar(ind, ori42, width, color='#FED498',label="FPZIP+H")
rects3 = ax.bar(ind+width, ori43, width, color='#9E94B6',label="FPZIP+Z")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels(namelist4,rotation=90)

#xlim must match the x
ax.set_xlim([-0.5,32.5])

ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(.95, 1.35))
plt.savefig(name_hat+'SFC_float_FPZIP_CESM.pdf', format='pdf',bbox_inches="tight",pad_inches=0)




#Get the CR figure of CMP
fig = plt.figure(num=None,figsize=(24,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=28)          
plt.rc('ytick', labelsize=32)          
font = {'size':'24'}

ind = np.arange(len(x1))  
width = 0.18       

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori11, width, color='#FAAA89',label="FPZIP")
rects2 = ax.bar(ind,CMP1, width, color='#FFDC7E',label="FPZIP$^+$")


ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels(namelist1,rotation=90 )

#xlim must match the x
ax.set_xlim([-0.5,19.5])

ax.legend(loc=1,ncol=2,  prop=font,bbox_to_anchor=(0.92, 1.25))
plt.savefig(name_hat+'CR_float_FPZIP_Hurricane_v1.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


fig = plt.figure(num=None,figsize=(16,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          
plt.rc('ytick', labelsize=32)          
font = {'size':'24'}

ind = np.arange(len(x2))  
width = 0.18       

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori21, width, color='#FAAA89',label="FPZIP")
rects2 = ax.bar(ind,CMP2, width, color='#FFDC7E',label="FPZIP$^+$")


ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels(namelist2,rotation=90 )

#xlim must match the x
ax.set_xlim([-0.5,5.5])

ax.legend(loc=1,ncol=2,  prop=font,bbox_to_anchor=(0.92, 1.25))
plt.savefig(name_hat+'CR_float_FPZIP+_NYX_v1.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


fig = plt.figure(num=None,figsize=(16,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          
plt.rc('ytick', labelsize=32)          
font = {'size':'24'}

ind = np.arange(len(x3))  
width = 0.18       

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori31, width, color='#FAAA89',label="FPZIP")
rects2 = ax.bar(ind,CMP3, width, color='#FFDC7E',label="FPZIP$^+$")

ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels(namelist3,rotation=90 )

#xlim must match the x
ax.set_xlim([-0.5,11.5])
ax.set_ylim([1,4])

ax.legend(loc=1,ncol=2,  prop=font,bbox_to_anchor=(0.92, 1.25))
plt.savefig(name_hat+'CR_float_FPZIP+_SCALE_v1.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


fig = plt.figure(num=None,figsize=(24,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=28)          
plt.rc('ytick', labelsize=32)          
font = {'size':'24'}

ind = np.arange(len(x4))  
width = 0.18       

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori41, width, color='#FAAA89',label="FPZIP")
rects2 = ax.bar(ind,CMP4, width, color='#FFDC7E',label="FPZIP$^+$")

ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels(namelist4,rotation=90 )

#xlim must match the x
ax.set_xlim([-0.5,32.5])

ax.legend(loc=1,ncol=2,  prop=font,bbox_to_anchor=(0.92, 1.25))
plt.savefig(name_hat+'CR_float_FPZIP_CESM_v1.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#For FPZIP-NYX+SCALE
fig = plt.figure(num=None,figsize=(16,4))

axis_font = {'size':'24'}
plt.rc('xtick', labelsize=20)          # fontsize of the tick labels
plt.rc('ytick', labelsize=22)
font = {'size':'18'}
x=range(0,18)
ind = np.arange(len(x))  # the x locations for the groups
width = 0.18       # the width of the bars

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori51, width, color='#FAAA89',label="FPZIP")
rects2 = ax.bar(ind,CMP5, width, color='#FFDC7E',label="FPZIP$^+$")

ax.set_ylabel('Compression ratio',fontsize=22)

ax.set_xticks(ind-width/2)
ax.set_xticklabels(namelist5,rotation=90 )

#xlim must match the x
ax.set_xlim([-0.5,17.5])
ax.set_ylim([1,4])

ax.legend(loc=1,ncol=2,  prop=font,bbox_to_anchor=(0.92, 1.2))
plt.savefig(name_hat+'CR_float_FPZIP_NYX_SCALE_v1.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#for average
fig = plt.figure(num=None,figsize=(6,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          
plt.rc('ytick', labelsize=32)          
font = {'size':'24'}
x=range(0,4)
ind = np.arange(len(x))  
width = 0.18       

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori_avg1, width, color='#FAAA89',label="FPZIP")
rects2 = ax.bar(ind,CMP_avg, width, color='#FFDC7E',label="FPZIP$^+$")

ax.set_ylabel('Compression ratio',fontsize=24)

ax.set_xticks(ind-width/2)
ax.set_xticklabels(namelist,rotation=90 )

#xlim must match the x
ax.set_xlim([-0.5,3.5])

ax.legend(loc=2,ncol=1,  prop=font,bbox_to_anchor=(0.4, 1))
plt.savefig(name_hat+'CR_float_FPZIP_avg.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
