# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:58:35 2018

@author: Ruiyu Zhang
"""
#HOMEWORK 2 QUESTION 3
import random
#Now generate the set
generator=[[1024,1],[2048,11],[4096,111],[1024,1111]]
data=[]
for i in range(len(generator)):
    for i2 in range(generator[i][0]):
        data.append(generator[i][1])
random.shuffle(data)

#Now sort
temp_1,temp_11,temp_111,temp_1111=[],[],[],[]
i3=len(data)-1
while len(data)>4096:#once len==4096, means only '111' left in data
    tp_data=data[i3]
    if tp_data==1:
        temp_1.append(data.pop(i3))
    elif tp_data==11:
        temp_11.append(data.pop(i3))
    elif tp_data==1111:
        temp_1111.append(data.pop(i3))
    #if data==111, loop is skipped
    i3-=1

temp=[]
temp.extend(temp_1)
temp.extend(temp_11)
temp.extend(data)
temp.extend(temp_1111)
data=temp

#Now test
#print(data)