import matplotlib.pyplot as plt
import numpy as np

import sys
import array
import os
import re

name_hat = "/home/lifenfang/SOCC2021/src/fig/"
data = np.loadtxt("socc_float.result.dat")
data=data.reshape(-1,12)
x=range(0,26)
namelist=["CLOUD","P","PRECIP","QCLOUD","QGRAUP","QICE","QRAIN","QSNOW","QVAPOR","TC","U","V","W","CLOUD.log","PRECIP.log","QCLOUD.log","QGRAUP.log","QICE.log","QRAIN.log","QSNOW.log","density_b","density_d","temperature","velocity_x","velocity_y","velocity_z"]
y1 =data[:,0]
y2 = data[:,1]
y3= data[:,2]
y4= data[:,3]
y5 =data[:,4]
y6 = data[:,5]
y7= data[:,6]
y8= data[:,7]
y9= data[:,8]
y10= data[:,9]
y11 =data[:,10]
y12 = data[:,11]


fig = plt.figure(num=None,figsize=(24,4))
#fig = plt.figure()
print(np.shape(x))
axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

N = len(x)
print(N)
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

ax = fig.add_subplot(111)



rects1 = ax.bar(ind-width, y2, width, color='g',hatch='.',label="FPZIP+O")
rects2 = ax.bar(ind, y10, width, color='r',hatch='+',label="FPZIP+H$^+$")
rects3 = ax.bar(ind+width, y12, width, color='b',hatch='x',label="FPZIP+Z$^+$")
ax.set_ylabel('Compression ratio',font)
#ax.set_title("ZFP",axis_font)
ax.set_xticks(ind+width)
ax.set_xticklabels( namelist,rotation=90 )
ax.set_xlim([-0.5,25.5])
#ax.set_ylim([1,3])
ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(.89, 1.35))
#ax.set_xlabel("(a) ZFP",{'family' : 'Times New Roman', 'size'   : 36})
#plt.tight_layout()

plt.savefig(name_hat+'CR_float_FPZIP+.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
#plt.show()

fig = plt.figure(num=None,figsize=(24,4))
#fig = plt.figure()
print(np.shape(x))
axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

N = len(x)
print(N)
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

ax = fig.add_subplot(111)



rects1 = ax.bar(ind-width, y2, width, color='g',hatch='.',label="FPZIP+O")
rects2 = ax.bar(ind, y4, width, color='r',hatch='+',label="FPZIP+H")
rects3 = ax.bar(ind+width, y6, width, color='b',hatch='x',label="FPZIP+Z")
ax.set_ylabel('Compression ratio',font)
ax.set_xticks(ind+width)
ax.set_xticklabels( namelist,rotation=90 )
ax.set_xlim([-0.5,25.5])
ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(.89, 1.35))


plt.savefig(name_hat+'CR_float_SFCfpzip.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
#plt.show()

fig = plt.figure(num=None,figsize=(24,4))
print(np.shape(x))
axis_font = {'size':'36'}
plt.rc('xtick', labelsize=36)          # fontsize of the tick labels
plt.rc('ytick', labelsize=36)
font = {'size':'36'}

N = len(x)
print(N)
ind = np.arange(N)  # the x locations for the groups
width = 0.4       # the width of the bars

ax = fig.add_subplot(111)



rects1 = ax.bar(ind, y2, width, color='g',hatch='.',label="FPZIP")
rects2 = ax.bar(ind+width, y8, width, color='r',hatch='+',label="FPZIP$^+$")
ax.set_ylabel('Compression ratio',font)
ax.set_xticks(ind+width)
ax.set_xticklabels( namelist,rotation=90 )
ax.set_xlim([-0.4,25.8])

ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(.89, 1.37))


plt.savefig(name_hat+'CR_float+.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
#plt.show()
