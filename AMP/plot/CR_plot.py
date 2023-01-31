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
data = np.loadtxt("../src/results/OridataSet.result1.dat")
data12 = np.loadtxt("../src/results/NewdataSet.result1.dat")
data0 = np.hstack((data, data12))
data0 = data0.reshape(-1,12)
data = data.reshape(-1,12)
data12 = data12.reshape(-1,12)
data = np.average(data,axis=0) 


data2 = np.loadtxt("../src/results/OridataSet_newComp.result1.dat")
data22 = np.loadtxt("../src/results/NewdataSet_newComp.result1.dat")
data2 = np.hstack((data2, data22))
data2 = data2.reshape(-1,4)

data3 = np.loadtxt("../src/results/OridataSet_newComp1.result1.dat")
data32 = np.loadtxt("../src/results/NewdataSet_newComp1.result1.dat")
data3 = np.hstack((data3, data32))
data3 = data3.reshape(-1,4)

#the range means the number of the dataset in one namelist
x=range(0,14)
#x=range(0,16)

namelist1=["diffusivity", "pressure","velocityx","velocityy","velocityz","viscocity",
           "diffusivity\'","pressure\'","velocityx\'", "velocityy\'","velocityz\'","viscocity\'",
           "astro_pt","wave"]
namelist2=["Miranda","astro_pt","wave"]
#namelist2=["redsea", "astro_mhp", "astro_pt","wave"]

#ori means baseline and unoptimized method
ori_fpc1 =data0[:,0]
ori_fpc1_ave = np.append(data[0],data12[:,0])
ori_fpzip1 = data0[:,1]
ori_fpzip1_ave = np.append(data[1],data12[:,1])
ori_fpc2= data0[:,2]
ori_fpc2_ave = np.append(data[2],data12[:,2])
ori_fpzip2= data0[:,3]
ori_fpzip2_ave = np.append(data[3],data12[:,3])
ori_fpc3 =data0[:,4]
ori_fpc3_ave = np.append(data[4],data12[:,4])
ori_fpzip3= data0[:,5]
ori_fpzip3_ave = np.append(data[5],data12[:,5])

ori_spdp1 = data2[:,0]
ori_spdp2 = data2[:,1]
ori_spdp3 = data2[:,2]

ori_ndzip1 = data3[:,0]
ori_ndzip2 = data3[:,1]
ori_ndzip3 = data3[:,2]

#CMP represents our method
CMP_fpc = data0[:,6]
CMP_fpc_ave = np.append(data[6],data12[:,6])
CMP_fpzip = data0[:,7]
CMP_fpzip_ave = np.append(data[7],data12[:,7])
CMP_spdp = data2[:,3]
CMP_ndzip = data3[:,3]


#get average compression improvement of CMP
data0_avg = np.average(data0,axis=0)
imprv_fpc=(data0_avg[6]-data0_avg[0])/data0_avg[0]
imprv_fpzip=(data0_avg[7]-data0_avg[1])/data0_avg[1]

print("improvement of FPC on average is ",imprv_fpc)
print("improvement of FPZIP on average is ",imprv_fpzip)

imprv_fpc=(data[6]-data[0])/data[0]
imprv_fpzip=(data[7]-data[1])/data[1]
print("improvement of FPC on average is ",imprv_fpc)
print("improvement of FPZIP on average is ",imprv_fpzip)

imprv_fpc=(data0[0,6]-data0[0,0])/data0[0,0]
imprv_fpzip=(data0[0,7]-data0[0,1])/data0[0,1]
print("improvement of FPC on diffusivity is ",imprv_fpc)
print("improvement of FPZIP on diffusivity is ",imprv_fpzip)

imprv_fpc=(data0[5,6]-data0[5,0])/data0[5,0]
imprv_fpzip=(data0[5,7]-data0[5,1])/data0[5,1]
print("improvement of FPC on viscocity is ",imprv_fpc)
print("improvement of FPZIP on viscocity is ",imprv_fpzip)



#Get the CR figure of ori methods

#FPC
fig = plt.figure(num=None,figsize=(16,4))
#fig = plt.figure(num=None,figsize=(10,4)) #new dataset

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

ind = np.arange(len(x))  
width = 0.27       

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori_fpc1, width, color='#F6B0A4',label="FPC+O")
rects2 = ax.bar(ind, ori_fpc2, width, color='#FED498',label="FPC+H")
rects3 = ax.bar(ind+width, ori_fpc3, width, color='#9E94B6',label="FPC+Z")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels( namelist1,rotation=90 )
ax.set_xlim([-0.5,13.6])
#ax.set_xlim([-0.5,3.6])

ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(0.92, 1.3))

plt.savefig(name_hat+'SFC_double_FPC_RAAW.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#FPZIP
fig = plt.figure(num=None,figsize=(16,4))
#fig = plt.figure(num=None,figsize=(10,4)) #new dataset
axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

ind = np.arange(len(x))  
width = 0.27       

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-width, ori_fpzip1, width, color='#F6B0A4',label="FPZIP+O")
rects2 = ax.bar(ind, ori_fpzip2, width, color='#FED498',label="FPZIP+H")
rects3 = ax.bar(ind+width, ori_fpzip3, width, color='#9E94B6',label="FPZIP+Z")
ax.set_ylabel('Compression ratio',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels( namelist1,rotation=90 )
#ax.set_xlim([-0.5,3.6])
ax.set_xlim([-0.5,13.6])

ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(0.95, 1.3))

plt.savefig(name_hat+'SFC_double_FPZIP_RAAW.pdf', format='pdf',bbox_inches="tight",pad_inches=0)




#Get the CR figure of CMP
fig = plt.figure(num=None,figsize=(24,4))
#fig = plt.figure(num=None,figsize=(10,4)) #new dataset

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'24'}

ind = np.arange(len(x))  # the x locations for the groups
width = 0.2       # the width of the bars

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-2*width, ori_fpc1, width, color='#FAAA89',label="FPC")#FCD3B5
rects2 = ax.bar(ind-width, CMP_fpc, width, color='#FFDC7E',label="FPC$^+$")#DF8D8F
rects3 = ax.bar(ind, ori_fpzip1, width, color='#7ED0F8',label="FPZIP")#FED498
rects4 = ax.bar(ind+width,CMP_fpzip, width, color='#DF8D8F',label="FPZIP$^+$")#FAAA89

ax.set_ylabel('Compression ratio',fontsize=24)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( namelist1,rotation=90 )
ax.set_xlim([-0.5,13.6])
#ax.set_xlim([-0.5,10])
ax.set_ylim([1,2])
ax.legend(loc=1,ncol=4,  prop=font,bbox_to_anchor=(0.92,1))

plt.savefig(name_hat+'CR_double_FPC_FPZIP_RAAW_v1.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
#plt.show()


#For aveage
fig = plt.figure(num=None,figsize=(6,4))
#fig = plt.figure(num=None,figsize=(10,4)) #new dataset

axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'22'}
x=range(0,3)
ind = np.arange(len(x))  # the x locations for the groups
width = 0.2       # the width of the bars

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-2*width, ori_fpc1_ave, width, color='#FAAA89',label="FPC")#FCD3B5
rects2 = ax.bar(ind-width, CMP_fpc_ave, width, color='#FFDC7E',label="FPC$^+$")#DF8D8F
rects3 = ax.bar(ind, ori_fpzip1_ave, width, color='#7ED0F8',label="FPZIP")#FED498
rects4 = ax.bar(ind+width,CMP_fpzip_ave, width, color='#DF8D8F',label="FPZIP$^+$")#FAAA89

ax.set_ylabel('Compression ratio',fontsize=24)

ax.set_xticks(ind-width/2)
ax.set_xticklabels( namelist2,rotation=90 )
ax.set_xlim([-0.5,2.6])
#ax.set_xlim([-0.5,10])
ax.set_ylim([1,2])
ax.legend(loc=2,ncol=2,  prop=font,bbox_to_anchor=(-0.02,1))

plt.savefig(name_hat+'CR_double_FPC_FPZIP_RAAW_ave.pdf', format='pdf',bbox_inches="tight",pad_inches=0)

