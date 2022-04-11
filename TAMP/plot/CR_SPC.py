import matplotlib.pyplot as plt
import numpy as np

import sys
import array
import os
import re

name_hat = "/home/lifenfang/SOCC2021/src/fig/"
data = np.loadtxt("SPC.result.txt.dat")
data=data.reshape(-1,6)
x=range(0,15)

namelist=["temp.", "density","diffusivity", "pressure",   "velocityx", "velocityy","velocityz","viscocity","density\'", "diffusivity\'", "pressure\'", "velocityx\'", "velocityy\'","velocityz\'","viscocity\'"]

y1 =data[:,0]
y2 = data[:,1]
y3= data[:,2]
y4= data[:,3]
y5 =data[:,4]
y6 = data[:,5]

fig = plt.figure(num=None,figsize=(16,4))
print np.shape(x)
axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

N = len(x)
print N
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

ax = fig.add_subplot(111)



rects1 = ax.bar(ind-width, y1, width, color='g',hatch='.',label="FPZIP+O")
rects2 = ax.bar(ind, y4, width, color='r',hatch='+',label="FPZIP+H")
rects3 = ax.bar(ind+width, y2, width, color='b',hatch='x',label="FPZIP+Z")
ax.set_ylabel('Compression ratio',font)
ax.set_xticks(ind+width)
ax.set_xticklabels( namelist,rotation=90 )
ax.set_xlim([-0.5,14.6])
ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(1, 1.35))


plt.savefig(name_hat+'CR_SPCfpzip.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
plt.show()

fig = plt.figure(num=None,figsize=(16,4))
print np.shape(x)
axis_font = {'size':'32'}
plt.rc('xtick', labelsize=32)          # fontsize of the tick labels
plt.rc('ytick', labelsize=32)
font = {'size':'32'}

N = len(x)
print N
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

ax = fig.add_subplot(111)



rects1 = ax.bar(ind-width, y1, width, color='g',hatch='.',label="FPC+O")
rects2 = ax.bar(ind, y5, width, color='r',hatch='+',label="FPC+H")
rects3 = ax.bar(ind+width, y3, width, color='b',hatch='x',label="FPC+Z")
ax.set_ylabel('Compression ratio',font)

ax.set_xticks(ind+width)
ax.set_xticklabels( namelist,rotation=90 )
ax.set_xlim([-0.5,14.6])

ax.legend(loc=1,ncol=3,  prop=font,bbox_to_anchor=(1, 1.35))


plt.savefig(name_hat+'CR_SPCfpc.pdf', format='pdf',bbox_inches="tight",pad_inches=0)
plt.show()

