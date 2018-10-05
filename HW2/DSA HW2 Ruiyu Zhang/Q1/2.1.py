# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:13:23 2018

@author: Ruiyu Zhang rz213
"""
#HOMEWORK 2 QUESTION 1

import random
import time

#define functions
def my_insertsort(a):
    swap,comp=0,0
    t1=time.clock()
    for i in range(1,len(a)):
        for j in range(i,0,-1):
            comp+=1
            if a[j]<a[j-1]: 
                a[j],a[j-1]=a[j-1],a[j]
                swap+=1
            else:break
        t2=time.clock()
    print("%-11.f"%len(a),"%-9.f"%swap,"%-9.f"%comp,str("%.5f" %(1000*(t2-t1))).zfill(10),'ms')
    return

def my_shellsort(b):
    swap2,comp2=0,0
    gap_raw=(7,3,1)
    t3=time.clock()
    for n in range (0,3):
        gap = gap_raw[n]
        for j2 in range(gap, len(b)):
            i2 = j2
            while (i2 - gap) >= 0 :
                comp2+=1
                if b[i2] < b[i2 - gap]:
                    b[i2], b[i2 - gap] = b[i2 - gap], b[i2]
                    i2 -= gap
                    swap2+=1
                else:
                    break
    t4=time.clock()
    print("%-11.f"%len(b),"%-9.f"%swap2,"%-9.f"%comp2,str("%.5f" %(1000*(t4-t3))).zfill(10),'ms')

#generate test data
print('Now generating random data...\n')
i1=random.sample(range(16384),512)
i2=random.sample(range(16384),1024)
i3=random.sample(range(16384),2048)
i4=random.sample(range(16384),4096)
i5=random.sample(range(16384),8192)
i6=random.sample(range(16384),16384)
s1=list(i1)
s2=list(i2)
s3=list(i3)
s4=list(i4)
s5=list(i5)
s6=list(i6)
#run data

print('Now run tests in sequence...\n')
print('SHELL SORT')
print('DATA-SIZE   COMPs     SWAPs     TIME')
my_shellsort(s1)
my_shellsort(s2)
my_shellsort(s3)
my_shellsort(s4) 
my_shellsort(s5)
my_shellsort(s6) 
print('\nINSERTION SORT')
print('DATA-SIZE   COMPs     SWAPs     TIME')
my_insertsort(i1)
my_insertsort(i2)
my_insertsort(i3)
my_insertsort(i4)
my_insertsort(i5)
my_insertsort(i6)
