# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:00:50 2018

@author: Ruiyu Zhang
"""
#HOMEWORK 2 QUESTION 5
import random
import time
'''
#This function picks data from file. PLZ MODIFY DATA PATH BELOW
def file_fetch(num):
    fetched=[]
    #!!!plz modify this data_path to run demo on your device!!!
    #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    data_path="G:/GoogleDrive/课件-Grad/Data Structure & Algorithms/Homework/HW2/p2"
    #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    data_file=open(data_path+'/data0.'+str(num)+'.txt','r')
    fetched.append(data_file.read().splitlines())
    data_file=open(data_path+'/data1.'+str(num)+'.txt','r')
    fetched.append(data_file.read().splitlines())
    return fetched #2-D array
'''
#merge sort
def merge(l2):  
    global cutoff
    step,insert_sorter=cutoff,0
    while insert_sorter+cutoff<len(l2):
        insert_sort(l2,insert_sorter,insert_sorter+cutoff)
        insert_sorter+=cutoff
    if insert_sorter<len(l2)-1:
        insert_sort(l2,insert_sorter,len(l2)-1)
    while step<len(l2):  
        i2=0  
        while i2+step<len(l2):  
            mid2,j2=i2+step,i2+step+step
            if j2>len(l2):j2=len(l2)  
            merge_slave(l2,i2,mid2,j2)  
            i2=j2  
        step*=2  
def merge_slave(l2,i2,mid2,j2):  
    global comp_i
    tmp=[]  
    i3,j3=i2,mid2  
    while i3<mid2 and j3<j2:  
        if l2[i3]<l2[j3]:  
            tmp.append(l2[i3])  
            i3+=1  
        else:
            tmp.append(l2[j3])  
            j3+=1 
    if i3==mid2:tmp+=l2[j3:j2]  
    else:tmp+=l2[i3:mid2]  
    l2[i2:j2]=tmp[:] 
def insert_sort(l2,start,end):
    for i2 in range(start,end):
        for i3 in range(i2,start,-1):
            if l2[i3]<l2[i3-1]: 
                l2[i3],l2[i3-1]=l2[i3-1],l2[i3]
            else:break
#quick sort
def quick(l):
    global cutoff
    less,equal,greater = [],[],[]
    if len(l) > cutoff:
        pivot = midof3(l)
        for x in l:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick(less)+equal+quick(greater)
    else:#cutoff
        for i2 in range(1,len(l)):
            for i3 in range(i2,0,-1):
                if l[i3]<l[i3-1]: 
                    l[i3],l[i3-1]=l[i3-1],l[i3]
                else:break
        return l
def midof3(l):
    a,b,c=l[0],l[len(l)-1],l[len(l)//2]
    r=max(a,b)
    if c<a and c<b:return min(a,b)
    else:return min(r,c)

#main
random_arr=random.sample(range(2147483647),300000) #Generate my array! Data from Q4 not used
print('CUTOFF QUICK-SORT  MERGE-SORT')
for cutoff in range(1,50):
    qs,ms=list(random_arr),list(random_arr)
    t1=time.clock()
    a=quick(qs)#quick sort
    t2=time.clock()
    merge(ms)#merge sort
    t3=time.clock()
    print("%-6.f"%cutoff,"%-7.2f"%(1000*(t2-t1)),'ms ',"%-7.2f"%(1000*(t3-t2)),'ms')


            

    
