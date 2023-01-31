#Time_approximate.py
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
data8 = np.loadtxt("../src/results/AMP_float.result2.dat")
data9 = np.loadtxt("../src/results/rawCompress_float.result3.dat")#SCALE
data10 = np.loadtxt("../src/results/AMP_float.result3.dat")
#merge SCALE into NYX
data79 = np.hstack((data7,data9))
data810 = np.hstack((data8,data10))

data7 = data7.reshape(-1,6)
data8 = data8.reshape(-1,4)
data9 = data9.reshape(-1,6)
data10 = data10.reshape(-1,4)
data79 = data79.reshape(-1,6)
data810 = data810.reshape(-1,4)

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

datalist2=["density_b","density_d","temp","velocity_x","velocity_y","velocity_z"]

datalist3=["PRES","QG","QR","QV","T","V","QC","QI","QS","RH","U","W"]

datalist4=["CLDICE"," CONCLD"," ICIMR"," Q"," U",
           "VU"," CLDLIQ"," DCQ"," ICLDIWP"," QC",
            "UU"," VV"," CLOUD"," DTCOND"," ICLDTWP",
            "QRL"," V"," Z3"," CMFDQ"," DTV",
            "ICWMR"," QRS"," VD01"," CMFDQR"," FICE",
            "OMEGA"," RELHUM"," VQ"," CMFDT"," GCLDLWP",
            "OMEGAT"," T"," VT"]

datalist5=datalist2+datalist3

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

#Dataset NYX+SCLAE
CR_fpzip5 = data79[:,1]
CR_fpzip_p5 = data79[:,5]
Time_fpzip5 = data79[:,0]
Time_fpzip_p_med5 = data79[:,2]
Time_fpzip_p_precondition5 = data79[:,3]
Time_fpzip_p_compress5 = data79[:,4]

CR_fpzip_AMD5 =data810[:,3]
Time_AMD5 = data810[:,0]
Time_AMD_precondition5 =data810[:,1]
Time_AMD_fpzip_compress5 =data810[:,2]


#Get average sppedup improvement 
data1_avg = np.average(data1,axis=0);
data2_avg = np.average(data2,axis=0);
imprv_med = data1_avg[4]/data2_avg[0];
imprv_fpc = ((data1_avg[4]+data1_avg[5]+data1_avg[6])-(data2_avg[0]+data2_avg[1]+data2_avg[2]))/(data1_avg[4]+data1_avg[5]+data1_avg[6])
imprv_fpzip = ((data1_avg[4]+data1_avg[5]+data1_avg[8])-(data2_avg[0]+data2_avg[1]+data2_avg[4]))/(data1_avg[4]+data1_avg[5]+data1_avg[8])
timeRatio = data2_avg[0]/(data2_avg[0]+data2_avg[1]+data2_avg[2])
timeRatio_fpzip = data2_avg[0]/(data2_avg[0]+data2_avg[1]+data2_avg[4])
oritimeRatio =(data2_avg[0]+data2_avg[1]+data2_avg[2])/data1_avg[0]
oritimeRatio_fpzip =(data2_avg[0]+data2_avg[1]+data2_avg[4])/data1_avg[2]
print("improvement of median on average is ",imprv_med)
print("improvement of FPC on average is ",imprv_fpc)
print("improvement of FPZIP on average is ",imprv_fpzip)
print("the ratio of approx median time FPC is",timeRatio)
print("the ratio of approx median time FPZIP is",timeRatio_fpzip)
print("the ratio of approx median time vs ori FPC is",oritimeRatio)
print("the ratio of approx median time vs ori FPZIP is",oritimeRatio_fpzip)

#Hurricane
data1_avg = np.average(data5,axis=0);
data2_avg = np.average(data6,axis=0);
imprv_med = data1_avg[2]/data2_avg[0];
imprv_fpzip = ((data1_avg[2]+data1_avg[3]+data1_avg[4])-(data2_avg[0]+data2_avg[1]+data2_avg[2]))/(data1_avg[2]+data1_avg[3]+data1_avg[4])
timeRatio = data2_avg[0]/(data2_avg[0]+data2_avg[1]+data2_avg[2])
oritimeRatio =(data2_avg[0]+data2_avg[1]+data2_avg[2])/data1_avg[0]
print("improvement of median on average is ",imprv_med)
print("improvement of FPZIP on average is ",imprv_fpzip)
print("the ratio of approx median time is",timeRatio)
print("the ratio of approx median time vs ori FPZIP is",oritimeRatio)

#NYX
data1_avg = np.average(data7,axis=0);
data2_avg = np.average(data8,axis=0);
imprv_med = data1_avg[2]/data2_avg[0];
imprv_fpzip = ((data1_avg[2]+data1_avg[3]+data1_avg[4])-(data2_avg[0]+data2_avg[1]+data2_avg[2]))/(data1_avg[2]+data1_avg[3]+data1_avg[4])
timeRatio = data2_avg[0]/(data2_avg[0]+data2_avg[1]+data2_avg[2])
oritimeRatio =(data2_avg[0]+data2_avg[1]+data2_avg[2])/data1_avg[0]
print("improvement of median on average is ",imprv_med)
print("improvement of FPZIP on average is ",imprv_fpzip)
print("the ratio of approx median time is",timeRatio)
print("the ratio of approx median time vs ori FPZIP is",oritimeRatio)

#SCALE
data1_avg = np.average(data9,axis=0);
data2_avg = np.average(data10,axis=0);
imprv_med = data1_avg[2]/data2_avg[0];
imprv_fpzip = ((data1_avg[2]+data1_avg[3]+data1_avg[4])-(data2_avg[0]+data2_avg[1]+data2_avg[2]))/(data1_avg[2]+data1_avg[3]+data1_avg[4])
timeRatio = data2_avg[0]/(data2_avg[0]+data2_avg[1]+data2_avg[2])
oritimeRatio =(data2_avg[0]+data2_avg[1]+data2_avg[2])/data1_avg[0]
print("improvement of median on average is ",imprv_med)
print("improvement of FPZIP on average is ",imprv_fpzip)
print("the ratio of approx median time is",timeRatio)
print("the ratio of approx median time vs ori FPZIP is",oritimeRatio)

#CESM
data1_avg = np.average(data11,axis=0);
data2_avg = np.average(data12,axis=0);
imprv_med = data1_avg[2]/data2_avg[0];
imprv_fpzip = ((data1_avg[2]+data1_avg[3]+data1_avg[4])-(data2_avg[0]+data2_avg[1]+data2_avg[2]))/(data1_avg[2]+data1_avg[3]+data1_avg[4])
timeRatio = data2_avg[0]/(data2_avg[0]+data2_avg[1]+data2_avg[2])
oritimeRatio =(data2_avg[0]+data2_avg[1]+data2_avg[2])/data1_avg[0]
print("improvement of median on average is ",imprv_med)
print("improvement of FPZIP on average is ",imprv_fpzip)
print("the ratio of approx median time is",timeRatio)
print("the ratio of approx median time vs ori FPZIP is",oritimeRatio)

#Get the Time figure
#double-poiting dataset-Miranda

fig = plt.figure(num=None,figsize=(24,6))
axis_font = {'size':'16'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'24'}

ind = np.arange(len(x))
width = 0.15
cum1 =list(map(sum, zip(list(Time_fpc_p_compress),list(Time_fpc_p_precondition))))
cum2 =list(map(sum, zip(list(Time_AMD_fpc_compress),list(Time_AMD_precondition))))
cum3 =list(map(sum, zip(list(Time_fpzip_p_compress),list(Time_fpc_p_precondition))))
cum4 =list(map(sum, zip(list(Time_AMD_fpzip_compress),list(Time_AMD_precondition))))

ax = fig.add_subplot(111)

rects1 = ax.bar(ind-2*width, Time_fpc, width, color='#7ED0F8',label="FPC",edgecolor='#FFF0F5')
rects2 = ax.bar(ind-width, Time_fpc_p_compress, width, color='#7ED0F8',edgecolor='#FFF0F5')#	#B0E0E6
rects3 = ax.bar(ind-width, Time_fpc_p_precondition, width,bottom=Time_fpc_p_compress,color='#B0E0E6',label="FPC+_preC.",edgecolor='#FFF0F5')
rects4 = ax.bar(ind-width, Time_fpc_p_med, width,bottom=cum1,color='#FFDC7E',label="FPC+_constr",edgecolor='#FFF0F5')
rects5 = ax.bar(ind, Time_AMD_fpc_compress, width, color='#7ED0F8',edgecolor='#FFF0F5')
rects6 = ax.bar(ind, Time_AMD_precondition, width, bottom=Time_AMD_fpc_compress,color='#D4F2E7',label="AMP_FPC_preC.",edgecolor='#FFF0F5')
rects7 = ax.bar(ind, Time_AMD, width, bottom=cum2, color='#FAAA89',label="AMP_FPC_constr",edgecolor='#FFF0F5')

rects8 = ax.bar(ind+width, Time_fpzip, width, color='#7EA2ED',label="FPZIP",edgecolor='#FFF0F5')
rects9 = ax.bar(ind+2*width, Time_fpzip_p_compress, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects10 = ax.bar(ind+2*width, Time_fpc_p_precondition,width, bottom=Time_fpzip_p_compress,  color='#F0D2E6',label="FPZIP+_preC.",edgecolor='#FFF0F5')
rects11 = ax.bar(ind+2*width, Time_fpc_p_med,width, bottom=cum3,  color='#FCD3B5',label="FPZIP+_constr",edgecolor='#FFF0F5')
rects12 = ax.bar(ind+3*width, Time_AMD_fpzip_compress, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects13 = ax.bar(ind+3*width, Time_AMD_precondition, width,bottom=Time_AMD_fpzip_compress, color='#E6E6FA',label="AMP_FPZIP_preC.",edgecolor='#FFF0F5')
rects14 = ax.bar(ind+3*width, Time_AMD, width,bottom=cum4, color='#DF8D8F',label="AMP_FPZIP_constr",edgecolor='#FFF0F5')

ax.set_ylabel('Time (ms)',fontsize=32)

ax.set_xticks(ind+width/2)
ax.set_xticklabels( datalist,rotation=90 )
ax.set_xlim([-0.5,13.6])

ax.legend(loc=2,ncol=5,  prop=font,bbox_to_anchor=(-0.08, 1.26))
plt.savefig(name_hat+'Time_double_approxMD_Miranda.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#float-pointing dataset--Hurricane
fig = plt.figure(num=None,figsize=(24,6))
axis_font = {'size':'16'}
plt.rc('xtick', labelsize=24)
plt.rc('ytick', labelsize=24)
font = {'size':'22'}

ind = np.arange(len(x1))
width = 0.18

ax = fig.add_subplot(111)
cum1 =list(map(sum, zip(list(Time_fpzip_p_compress1),list(Time_fpzip_p_precondition1))))
cum2 =list(map(sum, zip(list(Time_AMD_fpzip_compress1),list(Time_AMD_precondition1))))

rects1 = ax.bar(ind-width, Time_fpzip1, width, color='#7EA2ED',label="FPZIP",edgecolor='#FFF0F5')
rects2 = ax.bar(ind,Time_fpzip_p_compress1, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects3 = ax.bar(ind, Time_fpzip_p_precondition1,width, bottom=Time_fpzip_p_compress1,  color='#F0D2E6',label="FPZIP+_preC.",edgecolor='#FFF0F5')
rects4 = ax.bar(ind, Time_fpzip_p_med1,width, bottom=cum1,color='#FCD3B5',label="FPZIP+_constr",edgecolor='#FFF0F5')
rects5 = ax.bar(ind+width, Time_AMD_fpzip_compress1, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects6 = ax.bar(ind+width, Time_AMD_precondition1, width,bottom=Time_AMD_fpzip_compress1, color='#E6E6FA',label="AMP_FPZIP_preC.",edgecolor='#FFF0F5')
rects7 = ax.bar(ind+width, Time_AMD1, width,bottom=cum2, color='#DF8D8F',label="AMP_FPZIP_constr",edgecolor='#FFF0F5')

ax.set_ylabel('Time (ms)',fontsize=24)

ax.set_xticks(ind)
ax.set_xticklabels( datalist1,rotation=90 )
ax.set_xlim([-0.5,19.6])

ax.legend(loc=1,ncol=5,  prop=font,bbox_to_anchor=(1, 1.15))
plt.savefig(name_hat+'Time_float_approxMD_Hurricane.pdf', format='pdf',bbox_inches="tight",pad_inches=0)

#float-pointing dataset--NYX
fig = plt.figure(num=None,figsize=(10,4))
axis_font = {'size':'16'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'24'}

ind = np.arange(len(x2))
width = 0.18

ax = fig.add_subplot(111)
cum1 =list(map(sum, zip(list(Time_fpzip_p_compress2),list(Time_fpzip_p_precondition2))))
cum2 =list(map(sum, zip(list(Time_AMD_fpzip_compress2),list(Time_AMD_precondition2))))

rects1 = ax.bar(ind-width, Time_fpzip2, width, color='#7EA2ED',label="FPZIP",edgecolor='#FFF0F5')
rects2 = ax.bar(ind,Time_fpzip_p_compress2, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects3 = ax.bar(ind, Time_fpzip_p_precondition2,width, bottom=Time_fpzip_p_compress2,  color='#F0D2E6',label="FPZIP+_preC.",edgecolor='#FFF0F5')
rects4 = ax.bar(ind, Time_fpzip_p_med2,width, bottom=cum1 ,color='#FCD3B5',label="FPZIP+_constr",edgecolor='#FFF0F5')
rects5 = ax.bar(ind+width, Time_AMD_fpzip_compress2, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects6 = ax.bar(ind+width, Time_AMD_precondition2, width,bottom=Time_AMD_fpzip_compress2, color='#E6E6FA',label="AMP_FPZIP_preC.",edgecolor='#FFF0F5')
rects7 = ax.bar(ind+width, Time_AMD2, width,bottom=cum2, color='#DF8D8F',label="AMP_FPZIP_constr",edgecolor='#FFF0F5')

ax.set_ylabel('Time (ms)',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels( datalist2,rotation=90 )
ax.set_xlim([-0.5,5.6])

ax.legend(loc=3,ncol=2,  prop=font,bbox_to_anchor=(-0.1, 1))
plt.savefig(name_hat+'Time_float_approxMD_NYX.pdf', format='pdf',bbox_inches="tight",pad_inches=0)



#float-pointing dataset--SCALE
fig = plt.figure(num=None,figsize=(16,6))
axis_font = {'size':'16'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'24'}

ind = np.arange(len(x3))
width = 0.18

ax = fig.add_subplot(111)
cum1 =list(map(sum, zip(list(Time_fpzip_p_compress3),list(Time_fpzip_p_precondition3))))
cum2 =list(map(sum, zip(list(Time_AMD_fpzip_compress3),list(Time_AMD_precondition3))))

rects1 = ax.bar(ind-width, Time_fpzip3, width, color='#7EA2ED',label="FPZIP",edgecolor='#FFF0F5')
rects2 = ax.bar(ind,Time_fpzip_p_compress3, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects3 = ax.bar(ind, Time_fpzip_p_precondition3,width, bottom=Time_fpzip_p_compress3,  color='#F0D2E6',label="FPZIP+_preC.",edgecolor='#FFF0F5')
rects4 = ax.bar(ind, Time_fpzip_p_med3,width, bottom=cum1, color='#FCD3B5',label="FPZIP+_constr",edgecolor='#FFF0F5')
rects5 = ax.bar(ind+width, Time_AMD_fpzip_compress3, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects6 = ax.bar(ind+width, Time_AMD_precondition3, width,bottom=Time_AMD_fpzip_compress3, color='#E6E6FA',label="AMP_FPZIP_preC.",edgecolor='#FFF0F5')
rects7 = ax.bar(ind+width, Time_AMD3, width,bottom=cum2, color='#DF8D8F',label="AMP_FPZIP_constr",edgecolor='#FFF0F5')

ax.set_ylabel('Time (ms)',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels( datalist3,rotation=90 )
ax.set_xlim([-0.5,11.6])

ax.legend(loc=2,ncol=3,  prop=font,bbox_to_anchor=(0, 1.25))
plt.savefig(name_hat+'Time_float_approxMD_SCALE.pdf', format='pdf',bbox_inches="tight",pad_inches=0)



#float-pointing dataset--CESM
fig = plt.figure(num=None,figsize=(36,6))
axis_font = {'size':'16'}
plt.rc('xtick', labelsize=32)
plt.rc('ytick', labelsize=32)
font = {'size':'28'}

ind = np.arange(len(x4))
width = 0.18

ax = fig.add_subplot(111)
cum1 =list(map(sum, zip(list(Time_fpzip_p_compress4),list(Time_fpzip_p_precondition4))))
cum2 =list(map(sum, zip(list(Time_AMD_fpzip_compress4),list(Time_AMD_precondition4))))

rects1 = ax.bar(ind-width, Time_fpzip4, width, color='#7EA2ED',label="FPZIP",edgecolor='#FFF0F5')
rects2 = ax.bar(ind,Time_fpzip_p_compress4, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects3 = ax.bar(ind, Time_fpzip_p_precondition4,width, bottom=Time_fpzip_p_compress4,  color='#F0D2E6',label="FPZIP+_preC.",edgecolor='#FFF0F5')
rects4 = ax.bar(ind, Time_fpzip_p_med4,width, bottom=cum1, color='#FCD3B5',label="FPZIP+_constr",edgecolor='#FFF0F5')
rects5 = ax.bar(ind+width, Time_AMD_fpzip_compress4, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects6 = ax.bar(ind+width, Time_AMD_precondition4, width,bottom=Time_AMD_fpzip_compress4, color='#E6E6FA',label="AMP_FPZIP_preC.",edgecolor='#FFF0F5')
rects7 = ax.bar(ind+width, Time_AMD4, width,bottom=cum2, color='#DF8D8F',label="AMP_FPZIP_constr",edgecolor='#FFF0F5')

ax.set_ylabel('Time (ms)',fontsize=32)

ax.set_xticks(ind)
ax.set_xticklabels( datalist4,rotation=90 )
ax.set_xlim([-0.5,32.6])

ax.legend(loc=1,ncol=5,  prop=font,bbox_to_anchor=(0.95, 1.2))
plt.savefig(name_hat+'Time_float_approxMD_CESM.pdf', format='pdf',bbox_inches="tight",pad_inches=0)

#float-pointing dataset--NYX+SCALE
fig = plt.figure(num=None,figsize=(24,4))
axis_font = {'size':'16'}
plt.rc('xtick', labelsize=24)
plt.rc('ytick', labelsize=24)
font = {'size':'20'}
x=range(0,18)
ind = np.arange(len(x))
width = 0.18

ax = fig.add_subplot(111)
cum1 =list(map(sum, zip(list(Time_fpzip_p_compress5),list(Time_fpzip_p_precondition5))))
cum2 =list(map(sum, zip(list(Time_AMD_fpzip_compress5),list(Time_AMD_precondition5))))

rects1 = ax.bar(ind-width, Time_fpzip5, width, color='#7EA2ED',label="FPZIP",edgecolor='#FFF0F5')
rects2 = ax.bar(ind,Time_fpzip_p_compress5, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects3 = ax.bar(ind, Time_fpzip_p_precondition5,width, bottom=Time_fpzip_p_compress5,  color='#F0D2E6',label="FPZIP+_preC.",edgecolor='#FFF0F5')
rects4 = ax.bar(ind, Time_fpzip_p_med5,width, bottom=cum1 ,color='#FCD3B5',label="FPZIP+_constr",edgecolor='#FFF0F5')
rects5 = ax.bar(ind+width, Time_AMD_fpzip_compress5, width, color='#7EA2ED',edgecolor='#FFF0F5')
rects6 = ax.bar(ind+width, Time_AMD_precondition5, width,bottom=Time_AMD_fpzip_compress5, color='#E6E6FA',label="AMP_FPZIP_preC.",edgecolor='#FFF0F5')
rects7 = ax.bar(ind+width, Time_AMD5, width,bottom=cum2, color='#DF8D8F',label="AMP_FPZIP_constr",edgecolor='#FFF0F5')

ax.set_ylabel('Time (ms)',fontsize=24)
ax.set_xticks(ind)
ax.set_xticklabels( datalist5,rotation=90 )
ax.set_xlim([-0.5,17.6])

ax.legend(loc=1,ncol=5,  prop=font,bbox_to_anchor=(1, 1.2))
plt.savefig(name_hat+'Time_float_approxMD_NYX_SCALE.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
