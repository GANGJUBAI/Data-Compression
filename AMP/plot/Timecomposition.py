#Timecomposition.py
#Author: Fenfang Li
#@Time: 2022/12

import matplotlib.pyplot as plt
import numpy as np


#load data
name_hat = "./fig/"
data1 = np.loadtxt("../src/results/rawCompress.result1.dat")#Miranda
data1 = data1.reshape(-1,10)
data2 = np.loadtxt("../src/results/rawCompress.result2.dat")#astro+wave
data2 = data2.reshape(-1,10)

data3 = np.loadtxt("../src/results/rawCompress_float.result1.dat")#Hurricane
data3 = data3.reshape(-1,6)
data4 = np.loadtxt("../src/results/rawCompress_float.result2.dat")#NYX
data4 = data4.reshape(-1,6)
data5 = np.loadtxt("../src/results/rawCompress_float.result3.dat")#SCALE
data5 = data5.reshape(-1,6)
data6 = np.loadtxt("../src/results/rawCompress_float.result4.dat")#CESM
data6 = data6.reshape(-1,6)


#double-FPC
data_diffusivity=[data1[0,4],data1[0,5],data1[0,6]]
data_astropt=[data2[0,4],data2[0,5],data2[0,6]]
data_wave=[data2[1,4],data2[1,5],data2[1,6]]


#float-FPZIP
data_cloud=[data3[0,2],data3[0,3],data3[0,4]]
data_U=[data6[4,2],data6[4,3],data6[4,4]]
data_densityd=[data5[1,2],data5[1,3],data5[1,4]]

label1=['constr','preC.','FPC']
label2=['constr','preC.','FPZIP']


#For diffusivity
fig = plt.figure(num=None,figsize=(6,6))
ax = fig.add_subplot(111)

ax.pie(data_diffusivity,
        colors=['#FFDC7E','#B0E0E6','#7ED0F8'],
        autopct='%1.2f%%',
        pctdistance=0.85,
        textprops = {'fontsize':16},
        wedgeprops=dict(width=0.3, edgecolor='w'))

#plt.legend(loc='upper right',labels=label1,fontsize=14)
plt.axis('equal')

plt.savefig(name_hat+'Timecomposition_diffusivity.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#For astro_pt
fig = plt.figure(num=None,figsize=(6,6))
ax = fig.add_subplot(111)

ax.pie(data_astropt,
        colors=['#FFDC7E','#B0E0E6','#7ED0F8'],
        autopct='%1.2f%%',
        pctdistance=0.85,
        textprops = {'fontsize':16},
        wedgeprops=dict(width=0.3, edgecolor='w'))

#plt.legend(loc='upper right',labels=label1,fontsize=14)
plt.axis('equal')

plt.savefig(name_hat+'Timecomposition_astro.pdf', format='pdf',bbox_inches="tight",pad_inches=0)



#For wave
fig = plt.figure(num=None,figsize=(6,6))
ax = fig.add_subplot(111)

ax.pie(data_wave,
        colors=['#FFDC7E','#B0E0E6','#7ED0F8'],
        autopct='%1.2f%%',
        pctdistance=0.85,
        textprops = {'fontsize':16},
        wedgeprops=dict(width=0.3, edgecolor='w'))

plt.legend(loc='upper right',labels=label1,fontsize=16)
plt.axis('equal')

plt.savefig(name_hat+'Timecomposition_wave.pdf', format='pdf',bbox_inches="tight",pad_inches=0)



#For CLOUD
fig = plt.figure(num=None,figsize=(6,6))
ax = fig.add_subplot(111)

ax.pie(data_cloud,
        colors=['#FFDC7E','#B0E0E6','#7ED0F8'],
        autopct='%1.2f%%',
        pctdistance=0.85,
        textprops = {'fontsize':16},
        wedgeprops=dict(width=0.3, edgecolor='w'))

#plt.legend(loc='lower right',labels=label2,fontsize=14)
plt.axis('equal')

plt.savefig(name_hat+'Timecomposition_CLOUD.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#For U
fig = plt.figure(num=None,figsize=(6,6))
ax = fig.add_subplot(111)

ax.pie(data_U,
        colors=['#FFDC7E','#B0E0E6','#7ED0F8'],
        autopct='%1.2f%%',
        pctdistance=0.85,
        textprops = {'fontsize':16},
        wedgeprops=dict(width=0.3, edgecolor='w'))

#plt.legend(loc='lower right',labels=label2,fontsize=14)
plt.axis('equal')

plt.savefig(name_hat+'Timecomposition_U.pdf', format='pdf',bbox_inches="tight",pad_inches=0)


#For densityd
fig = plt.figure(num=None,figsize=(6,6))
ax = fig.add_subplot(111)

ax.pie(data_densityd,
        colors=['#FFDC7E','#B0E0E6','#7ED0F8'],
        autopct='%1.2f%%',
        pctdistance=0.85,
        textprops = {'fontsize':16},
        wedgeprops=dict(width=0.3, edgecolor='w'))

plt.legend(loc='lower right',labels=label2,fontsize=16)
plt.axis('equal')

plt.savefig(name_hat+'Timecomposition_densityd.pdf', format='pdf',bbox_inches="tight",pad_inches=0)

