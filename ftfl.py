# This code is used for implementing the FTFL technique for single fault localization
import sys
import time
from datetime import datetime
start_time=datetime.now()
import pandas as pd
import numpy as np
import math
import os
import csv


cwd =os.getcwd()
version=cwd.split("/")[-1]
program_name=cwd.split("/")[-2]
path1=cwd.replace("/"+version, "")
path1=path1.replace("/"+program_name, "")


#print(str_cwd)
f_l=0

start_time=datetime.now()

with open('faultyLine.txt') as f:
    f_l = f.readline()

print("**************")
print(f_l)
print("**************")

f_l=int(f_l)

df_train=pd.read_csv('statementResult.csv')

y = np.array([df_train['Result']]).T
y=y.tolist()

n= len(y) # Total number of test cases present for this program
n_f=np.count_nonzero(y) # Total number of failed test cases for this program
n_s= n-n_f #Total number of passed test cases 

'''print("Total test cases: "+str(n))
print("Total Successful test cases: "+str(n_s))
print("Total failed test cases: "+str(n_f))'''

df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
x=x.tolist()
suspicious=[]
n_es=len(x[0]) # Total number of executable statements in the program
#print("Total number execuatble statements in the program: "+str(len(x[0])))
n_c=1
n_u=1
n_uf=1
n_us=1
sus_score=0
m_w=0
chi_w_num=0
chi_w_den=0
chi_w=0
for i in range(0,len(x[0])):
	n_cf=0
	n_cs=0
	for j in range(0,len(y)):
		#print x[j][i],y[j][0]
		if x[j][i]==1 and y[j][0]==0:
			n_cs=n_cs+1
		elif x[j][i]==1 and y[j][0]==1:
			n_cf=n_cf+1
	#print("statement covered by number of succesful test cases:"+ str(n_cs))
	#print("statement covered by number of failed test cases: "+str(n_cf))
	n_c=n_cs+n_cf
	#print("statement covered by number of test cases: "+ str(n_c))
	n_u=n-n_c
	#print("statement not covered by number of test cases: "+ str(n_u))
	n_uf=n_f-n_cf
	#print("statement not covered by number of failed test cases: "+ str(n_uf))
	n_us=n_s-n_cs
	#print("statement not covered by number of sucessful test cases: "+ str(n_us))
	try:	
		if n_c==n:
			n_u=1
		factor1=n_c*n_u
		#print("ncs: "+str(n_cs)+" ncf: "+str(n_cf)+" nus: "+str(n_us)+" nuf: "+str(n_uf))
		if n_cs+n_cf==n:
			n_us=1
			n_uf=1
		if n_uf==0:
			n_uf=1
		if n_cs==0 and n_cf==n_f:
			n_cs=1
		factor2=n_cs*n_cf*n_us*n_uf
		#print("Line number: "+str(i)+" Suspicioussness:   "+str(factor1)+"  "+str(factor2))
		m_w=float(factor1)/factor2
		print("Line number: "+str(i)+" Suspicioussness: "+str(m_w)+"   "+str(factor1)+"  "+str(factor2))
		chi_w=0
		if n_f!=0:
			chi_w_num= float(n_cf)/n_f
		if n_s!=0:
			chi_w_den= float(n_cs)/n_s
		if chi_w_den!=0:
			chi_w= float(chi_w_num)/chi_w_den
		if chi_w>1:
                	sus_score=m_w
		elif chi_w==1:
			sus_score=0
		else: 
			sus_score= -m_w
		suspicious.append(sus_score)
		print(str(i)+"   "+str(sus_score))				
		print(str(i)+"nc:   "+str(n_c)+" n_u  "+str(n_u))
		print("ncs: "+str(n_cs)+" ncf: "+str(n_cf)+" nus: "+str(n_us)+" nuf: "+str(n_uf))
		
	except ZeroDivisionError:
		suspicious.append(0)

#print(suspicious[0])
d = {}
for i in range(0,len(suspicious)):
	key = float(suspicious[i])
	#print key
	if key not in d:
		d[key] = []
	d[key].append(i)

ct1=0
ct2=0
ct3=0
fct=0
for x in sorted(d):
	print (x,len(d[x]))
	if f_l not in d[x] and fct==0:
		ct1=ct1+len(d[x])
	elif f_l not in d[x] and fct==1:
		ct3=ct3+len(d[x])
	else: 
		fct=1
		ct2=len(d[x])
print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))


end_time=datetime.now()
csvfile=open(path1+"/Fisherjourn.csv", "a+")
spamwriter1 = csv.writer(csvfile, delimiter=',')
stmt_complex=[]
stmt_complex.append(program_name);
stmt_complex.append(str(version));
stmt_complex.append(f_l);
stmt_complex.append(str(ct3+1));
stmt_complex.append(ct2+ct3);
stmt_complex.append(end_time-start_time);
spamwriter1.writerow(stmt_complex);


