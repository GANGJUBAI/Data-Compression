import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
name_hat='/home/lifenfang/SOCC2021/src/fig/'

if len(sys.argv) < 1 :
    print('usage: python3 %s %s <file.dat' % sys.argv[0])
    sys.exit(0)
print(sys.argv[1])

data= np.loadtxt("fuzzyMedian_Distri_diffusivity.result")
x_data=pd.DataFrame(data[1,:])

f,ax=plt.subplots(figsize=(3.5,3))

axis_font = {'size':'14'}
ax.tick_params(labelsize=12)

sns.distplot(x_data,bins=40,hist=True,kde=True,color='cornflowerblue')#dodgerblue')#'firebrick')
plt.ylabel('Density',**axis_font )
plt.savefig(name_hat+sys.argv[1]+'.pdf', format='pdf',bbox_inches="tight",pad_inches=0.2)
plt.show()

