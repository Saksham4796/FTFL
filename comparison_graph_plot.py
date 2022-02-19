import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.legend_handler import HandlerLine2D

tb = []
tw = []
sb = []
sw = []
ub = []
uw = []
usb = []
usw = []
y = []
count =0
with open('ftfl1.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		if (count==0):
			count=count+1
		else:
			print(row)
			tb.append(float(row[0]))
			tw.append(float(row[1]))
			sb.append(float(row[2]))
			sw.append(float(row[3]))
			ub.append(float(row[4]))
			uw.append(float(row[5]))
			usb.append(float(row[6]))
			usw.append(float(row[7]))
			y.append(float(row[8]))



'''plt.plot(fb, y, 'k-*',color='black',markeredgecolor ='black',label="FTFL(Best)",linewidth=2, markersize=7)
plt.plot(fw, y, 'k-o',color='black',markeredgecolor ='black',label="FTFL(Worst)",linewidth=2, markersize=5)
plt.plot(ab, y, 'k-v',color='grey',markeredgecolor ='grey',label="Ample(Best)",linewidth=2, markersize=5)
plt.plot(aw, y, 'k--',color='grey',markeredgecolor ='grey',label="Ample(Worst)",linewidth=2, markersize=5)'''

plt.plot(fb, y, 'k-*',color='black',markeredgecolor ='black',label="FTFL(Best)",linewidth=2, markersize=7)
plt.plot(fw, y, 'k-o',color='black',markeredgecolor ='black',label="FTFL(Worst)",linewidth=2, markersize=5)
plt.plot(tb, y, 'k-v',color='grey',markeredgecolor ='grey',label="Tarantula(Best)",linewidth=2, markersize=5)
plt.plot(tw, y, 'k--',color='grey',markeredgecolor ='grey',label="Tarantula(Worst)",linewidth=2, markersize=5)


plt.ylim(0, 100)
plt.xlim(0, 90)
plt.xlabel('%  statements examined')
plt.ylabel('% faulty versions')
#plt.title('Improvement in Minus for SEIMENS Suite using HWN scoring')
plt.legend(loc='best')
plt.savefig('Minus_all.eps')
plt.show()



