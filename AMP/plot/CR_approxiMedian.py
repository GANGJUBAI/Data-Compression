#CR_approximate.py
#Author: Fenfang Li
#@Time: 2022/12

import matplotlib.pyplot as plt
import numpy as np

import sys
import array
import os

#load data
name_hat = "/to/path/src/results/fig/"

data1 = np.loadtxt("../src/results/rawCompress.result1.dat")
data3 = np.loadtxt("../src/results/rawCompress.result2.dat")
data1 = np.hstack((data1, data3))
data1 = data1.reshape(-1,10)

data2 = np.loadtxt("../src/results/AMP_Compress.result1.dat")
data4 = np.loadtxt("../src/results/AMP_Compress.result2.dat")
data2 = np.hstack((data2, data4))
data2 = data2.reshape(-1,6) 

data5 = np.loadtxt("../src/results/rawCompress_float.result1.dat")#Hurricane
data5 = data5.reshape(-1,6)
data6 = np.loadtxt("../src/results/AMP_float.result1.dat")
data6 = data6.reshape(-1,4)

data7 = np.loadtxt("../src/results/rawCompress_float.result2.dat")#NYX
data7 = data7.reshape(-1,6)
data8 = np.loadtxt("../src/results/AMP_float.result2.dat")
data8 = data8.reshape(-1,4)

data9 = np.loadtxt("../src/results/rawCompress_float.result3.dat")#SCALE
data9 = data9.reshape(-1,6)
data10 = np.loadtxt("../src/results/AMP_float.result3.dat")
data10 = data10.reshape(-1,4)

data11 = np.loadtxt("../src/results/rawCompress_float.result4.dat")#CESM
data11 = data11.reshape(-1,6)
data12 = np.loadtxt("../src/results/AMP_float.result4.dat")
data12 = data12.reshape(-1,4)


#the range means the number of the dataset in one namelist
x=range(0,14)
x1=range(0,20)
x2=range(0,6)
x3=range(0,12)
x4=range(0,33)


datalist=["diffusivity","pressure","velocityx","velocityy","velocityz","viscocity",
         "diffusivity\'","pressure\'","velocityx\'","velocityy\'","velocityz\'","viscocity\'","astro_pt","wave"]

datalist1=["CLOUD","P","PRECIP","QCLOUD","QGRAUP",
           "QICE","QRAIN","QSNOW","QVAPOR","TC",
           "U","V","W","CLOUD.log","PRECIP.log",
           "QCLOUD.log","QGRAUP.log","QICE.log","QRAIN.log","QSNOW.log"]

datalist2=["density_b","density_d","temperature","velocity_x","velocity_y","velocity_z"]

datalist3=["PRES","QG","QR","QV","T","V","QC","QI","QS","RH","U","W"]

datalist4=["CLDICE"," CONCLD"," ICIMR"," Q"," U",
           "VU"," CLDLIQ"," DCQ"," ICLDIWP"," QC",
            "UU"," VV"," CLOUD"," DTCOND"," ICLDTWP",
            "QRL"," V"," Z3"," CMFDQ"," DTV",
            "ICWMR"," QRS"," VD01"," CMFDQR"," FICE",
            "OMEGA"," RELHUM"," VQ"," CMFDT"," GCLDLWP",
            "OMEGAT"," T"," VT"]


#ori means baseline and unoptimized method
#for Double dataset, i.e.,dataset1-4
CR_fpc = data1[:,1]
CR_fpzip = data1[:,3]
CR_fpc_p = data1[:,7]
CR_fpzip_p = data1[:,9]
Time_fpc = data1[:,0]
Time_fpzip = data1[:,2]
Time_fpc_p_med = data1[:,4]
Time_fpc_p_precondition = data1[:,5]
Time_fpc_p_compress = data1[:,6]
Time_fpzip_p_compress = data1[:,8]

CR_fpc_AMD =data2[:,3]
CR_fpzip_AMD =data2[:,5]
Time_AMD = data2[:,0]
Time_AMD_precondition =data2[:,1]
Time_AMD_fpc_compress =data2[:,2]
Time_AMD_fpzip_compress =data2[:,4]

#for float dataset, i.e.,dataset5-12
#Dataset Hurricane
CR_fpzip1 = data5[:,1]
CR_fpzip_p1 = data5[:,5]
Time_fpzip1 = data5[:,0]
Time_fpzip_p_med1 = data5[:,2]
Time_fpzip_p_precondition1 = data5[:,3]
Time_fpzip_p_compress1 = data5[:,4]

CR_fpzip_AMD1 =data6[:,3]
Time_AMD1 = data6[:,0]
Time_AMD_precondition1 =data6[:,1]
Time_AMD_fpzip_compress1 =data6[:,2]

#Dataset NYX
CR_fpzip2 = data7[:,1]
CR_fpzip_p2 = data7[:,5]
Time_fpzip2 = data7[:,0]
Time_fpzip_p_med2 = data7[:,2]
Time_fpzip_p_precondition2 = data7[:,3]
Time_fpzip_p_compress2 = data7[:,4]

CR_fpzip_AMD2 =data8[:,3]
Time_AMD2 = data8[:,0]
Time_AMD_precondition2 =data8[:,1]
Time_AMD_fpzip_compress2 =data8[:,2]

#Dataset SCALE
CR_fpzip3 = data9[:,1]
CR_fpzip_p3 = data9[:,5]
Time_fpzip3 = data9[:,0]
Time_fpzip_p_med3 = data9[:,2]
Time_fpzip_p_precondition3 = data9[:,3]
Time_fpzip_p_compress3 = data9[:,4]

CR_fpzip_AMD3 =data10[:,3]
Time_AMD3 = data10[:,0]
Time_AMD_precondition3 =data10[:,1]
Time_AMD_fpzip_compress3 =data10[:,2]

#Dataset CESM
CR_fpzip4 = data11[:,1]
CR_fpzip_p4 = data11[:,5]
Time_fpzip4 = data11[:,0]
Time_fpzip_p_med4 = data11[:,2]
Time_fpzip_p_precondition4 = data11[:,3]
Time_fpzip_p_compress4 = data11[:,4]

CR_fpzip_AMD4 =data12[:,3]
Time_AMD4 = data12[:,0]
Time_AMD_precondition4 =data12[:,1]
Time_AMD_fpzip_compress4 =data12[:,2]



#Get the CR figure of ori methods
#double-poiting dataset
fig = plt.figure(num=None,figsize=(24,6))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

ind = np.arange(len(x))
width = 0.15

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width,CR_fpc_p , width, color='#FAAA89',label="FPC+")
rects2 = ax.bar(ind, CR_fpc_AMD, width, color='#FFDC7E',label="AMP_FPC")
rects3 = ax.bar(ind+width,CR_fpzip_p , width, color='#7ED0F8',label="FPZIP+")
rects4 = ax.bar(ind+2*width, CR_fpzip_AMD, width, color='#DF8D8F',label="AMP_FPZIP")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind+width/2)
ax.set_xticklabels( datalist,rotation=90 )
ax.set_xlim([-0.5,13.6])

ax.legend(loc=1,ncol=4, prop=font,bbox_to_anchor=(0.96, 1.2))
plt.savefig(name_hat+'CR_double_FPC_FPZIP_approxMD.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#single-poiting dataset
#Dataset Hurricane
fig = plt.figure(num=None,figsize=(24,6))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'28'}
ind = np.arange(len(x1))
width = 0.18

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, CR_fpzip_p1, width, color='#FAAA89',label="FPZIP+")
rects2 = ax.bar(ind, CR_fpzip_AMD1, width, color='#FFDC7E',label="AMP_FPZIP")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( datalist1,rotation=90 )
ax.set_xlim([-0.5,19.6])

ax.legend(loc=1,ncol=2, prop=font,bbox_to_anchor=(0.76, 1.2))
plt.savefig(name_hat+'CR_float_FPZIP_Hurricane_approxMD.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#Dataset NYX
fig = plt.figure(num=None,figsize=(14,4))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'28'}
ind = np.arange(len(x2))
width = 0.18

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, CR_fpzip_p2, width, color='#FAAA89',label="FPZIP+")
rects2 = ax.bar(ind, CR_fpzip_AMD2, width, color='#FFDC7E',label="AMP_FPZIP")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( datalist2,rotation=90 )
ax.set_xlim([-0.5,5.6])

ax.legend(loc=1,ncol=2, prop=font,bbox_to_anchor=(0.76, 1.2))
plt.savefig(name_hat+'CR_float_FPZIP_NYX_approxMD.pdf', format='pdf',bbox_inches="tight",pad_inches=0)



#Dataset SCALE
fig = plt.figure(num=None,figsize=(24,6))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'28'}
ind = np.arange(len(x3))
width = 0.18

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, CR_fpzip_p3, width, color='#FAAA89',label="FPZIP+")
rects2 = ax.bar(ind, CR_fpzip_AMD3, width, color='#FFDC7E',label="AMP_FPZIP")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( datalist3,rotation=90 )
ax.set_xlim([-0.5,19.6])

ax.legend(loc=1,ncol=2, prop=font,bbox_to_anchor=(0.76, 1.2))
plt.savefig(name_hat+'CR_float_FPZIP_SCALE_approxMD.pdf', format='pdf',bbox_inches="tight",pad_inches=0)



#Dataset CESM
fig = plt.figure(num=None,figsize=(24,6))

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'28'}
ind = np.arange(len(x4))
width = 0.18

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, CR_fpzip_p4, width, color='#FAAA89',label="FPZIP+")
rects2 = ax.bar(ind, CR_fpzip_AMD4, width, color='#FFDC7E',label="AMP_FPZIP")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( datalist4,rotation=90 )
ax.set_xlim([-0.5,32.6])

ax.legend(loc=1,ncol=2, prop=font,bbox_to_anchor=(0.76, 1.2))
plt.savefig(name_hat+'CR_float_FPZIP_CESM_approxMD.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
