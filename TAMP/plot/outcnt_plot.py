import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
import sys
import array
import os
import gc
name_hat = "/home/luo/Nutstore/Nutstore/"

if len(sys.argv) < 1 :
    print 'usage: python %s <file.dat' % sys.argv[0]
    sys.exit(0)

print sys.argv[1]

vals =np.loadtxt("ori.count", comments="#", delimiter=",", unpack=False) 
vals1 =np.loadtxt("temp_h+.count", comments="#", delimiter=",", unpack=False) 
vals2 =np.loadtxt("temp_z+.count", comments="#", delimiter=",", unpack=False) 

print vals

x=range(0,len(vals))

x1=0;
x2=int(len(vals));
plt.figure(num=None,figsize=(7.5,3))
plt.rc('xtick', labelsize=12)          # fontsize of the tick labels
plt.rc('ytick', labelsize=12)
#plt.ylim(-10000,10000)   
#plt.xticks(np.arange(0,260000,50000))
#plt.yticks(np.linspace(y1,y2,5));
plt.xticks(np.linspace(x1,x2,4));

axis_font = {'size':'14'}
axes = plt.gca()
#plt.xlabel('Data point ID', **axis_font)
plt.xlabel('Segment ID', **axis_font)

plt.ylabel('Bytes of output',**axis_font )
#plt.ylabel('Frequency',**axis_font )
#title_name="MAC="+str(mad).split('.')[0] + '.' + str(mad).split('.')[1][:2]
#plt.title(title_name, **axis_font)
#n, bins, patches=plt.hist(vals,bins=10,density=True,stacked=True, histtype='bar', label='png', color='black')
#n, bins, patches=plt.hist(vals,bins=1000,normed=True,histtype='step', cumulative=True, label='cdf',color='black')

plt.plot(x,vals,'b-',label="Baseline");

plt.plot(x,vals1,'r+',label="H$^+$")
plt.plot(x,vals2,'g.',label="Z$^+$")
plt.legend(loc=1,ncol=4, bbox_to_anchor=(.8, 1.35),prop={'size': 12} )

plt.tight_layout()
#plt.savefig('/home/luo/Dropbox/SC2019_Huizhang/AMR2019/figures/fig_frequency_zordering.pdf', format='pdf')
plt.savefig(name_hat+sys.argv[1]+".png", format='png',bbox_inches="tight",pad_inches=0)
plt.show()
