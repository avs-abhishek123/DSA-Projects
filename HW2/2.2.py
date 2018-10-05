# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:39:56 2018

@author: Ruiyu Zhang
"""
#HOMEWORK 2 QUESTION 2

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

#This function gets data ready and call Merge Sort function 'mymerge'
def get_inv(n):
    column=1#this time we deal with unsorted list
    data=file_fetch(n)#get data
    sarr=[]#to be sorted
    for reader in range(len(data[column])):
        sarr.append(int(data[column][reader]))
    mymerge(sarr)

#This is a merge sort function with a tracker of invs 
def mymerge(l):
    global inv
    if len(l)>1:
        mid = len(l)//2
        left,right = l[:mid],l[mid:]
        mymerge(left)#recursion: left
        mymerge(right)#recursion: right
        i,j,k=0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k]=left[i]
                i+=1
            else:
                l[k]=right[j]
                j+=1
                inv+=(len(left)-i)#!!!real tracker!!!
            k+=1
        while i < len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            l[k]=right[j]
            j+=1
            k+=1

#main
runner_queue=[1024,2048,4096,8192,16384,32768]
print('\n\nDATA-SIZE   INVs-FOUND')
for runner in range(6):
    inv=0 #tracker, global invariant
    get_inv(runner_queue[runner])
    print("%-11.f"%runner_queue[runner],inv)
    


