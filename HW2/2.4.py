# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:39:56 2018

@author: Ruiyu Zhang
"""
#HOMEWORK 2 QUESTION 4
#Origins from modification of my own HOMEWORK 2 QUESTION 2

#This function picks data from file. PLZ MODIFY DATA PATH BELOW
def file_fetch(num):
    fetched,raw_fetched=[],[]
    #!!!plz modify this data_path to run demo on your device!!!
    #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    data_path="G:/GoogleDrive/课件-Grad/Data Structure & Algorithms/Homework/HW2/p2"
    #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    data_file=open(data_path+'/data1.'+str(num)+'.txt','r')
    raw_fetched.append(data_file.read().splitlines())
    for i in range(len(raw_fetched[0])):
        fetched.append(int(raw_fetched[0][i]))
    return fetched #list

#This is a recursive mergesort function with a tracker of comparisons
def merge_recurse(l):
    global comp_r
    if len(l)>1:
        mid = len(l)//2
        left,right = l[:mid],l[mid:]
        merge_recurse(left)#recursion: left
        merge_recurse(right)#recursion: right
        i,j,k=0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k]=left[i]
                i+=1
            else:
                l[k]=right[j]
                j+=1
            k+=1
            comp_r+=1#comparison tracker
        while i < len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            l[k]=right[j]
            j+=1
            k+=1
#This is a iterative mergesort function with a tracker of comparisons
def merge_iter8(l2):  
    step=1  
    while step<len(l2):  
        i2=0  
        while i2+step<len(l2):  
            mid2,j2=i2+step,i2+step+step
            if j2>len(l2):j2=len(l2)  
            merge_iter8_slave(l2,i2,mid2,j2)  
            i2=j2  
        step*=2  
def merge_iter8_slave(l2,i2,mid2,j2):  
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
        comp_i+=1#comparison tracker
    if i3==mid2:tmp+=l2[j3:j2]  
    else:tmp+=l2[i3:mid2]  
    l2[i2:j2]=tmp[:] 

#main
runner_queue=[1024,2048,4096,8192,16384,32768]
print('\n\nDATA-SIZE   ITERATE-COMPs  RECURSE-COMPs')
for runner in range(6):
    comp_r,comp_i=0,0#clear global counter
    #fetch file
    current_file=runner_queue[runner]
    it=file_fetch(current_file)
    re=file_fetch(current_file)
    #calculate
    merge_iter8(it)
    merge_recurse(re)
    print("%-11.f"%current_file,"%-14.f"%comp_i,comp_r)

