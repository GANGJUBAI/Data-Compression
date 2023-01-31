import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
import sys
import array
import os
import gc
name_hat = "/home/lff/SC2021src/src/SPCtest/"

if len(sys.argv) < 1 :
    print('usage: python %s <file.dat' % sys.argv[0])
    sys.exit(0)

print(sys.argv[1])

statinfo=os.stat(sys.argv[1])
fsize=statinfo.st_size
print(fsize/4)
fin = open(sys.argv[1], 'rb')
vals = array.array('d',(int(fsize/4))*[0])

fin.readinto(vals)
fin.close()


deltas = array.array('d',(int(fsize/4))*[0])
for i in range(1,len(vals)):
    deltas[i]=abs(vals[i]-vals[i-1])
    if deltas[i]> 10000:
       deltas[i]=10000


mad=sum(deltas)/len(deltas)
del deltas

gc.collect()
x1=0;
x2=int(fsize/4);
y1=min(vals)
y2=max(vals)
plt.figure(num=None,figsize=(3.5,2))
plt.rc('xtick', labelsize=12)          # fontsize of the tick labels
plt.rc('ytick', labelsize=12)
#plt.ylim(-10000,10000)   
#plt.xticks(np.arange(0,260000,50000))
#plt.yticks(np.linspace(y1,y2,5));
plt.xticks(np.linspace(x1,x2,4));
print( y2)

axis_font = {'size':'14'}
axes = plt.gca()
plt.xlabel('Data point ID', **axis_font)
#plt.xlabel('Data value', **axis_font)

plt.ylabel('Data value',**axis_font )
#plt.ylabel('Data frequency',**axis_font )

title_name="MAC="+str('%.2e' % mad)
plt.title(title_name, **axis_font)
#n, bins, patches=plt.hist(vals,bins=100,normed=True,histtype='bar', label='pdf', color='black')
#n, bins, patches=plt.hist(vals,bins=1000,normed=True,histtype='step', cumulative=True, label='cdf',color='black')

plt.plot(vals,color='#7EA2ED');

#plt.plot(vals,'b')


plt.tight_layout()
#plt.savefig('/home/luo/Dropbox/SC2019_Huizhang/AMR2019/figures/fig_frequency_zordering.pdf', format='pdf')
plt.savefig(name_hat+sys.argv[1]+".pdf", format='pdf',bbox_inches="tight",pad_inches=0)
#plt.show()
