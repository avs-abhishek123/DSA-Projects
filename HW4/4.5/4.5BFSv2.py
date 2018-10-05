# -*- coding: utf-8 -*-
"""
Created on APR 9 2018

@author: Ruiyu Zhang
"""
import sys
import time
path='./'

def read_graph(name='NYC.txt'):
    f,data=open(path+name,'r'),[]
    raw=f.read().splitlines()
    f.close()
    raw=raw[2:]
    for row in raw:
        nums=row.split(' ')
        data.append([int(nums[0]),int(nums[1]),int(nums[2])])
    return data
data=read_graph()
g={}#graph
for row in data:
    if row[0] not in g.keys():
        g[row[0]]=[row[1]]
    else:
        g[row[0]].append(row[1])
    if row[1] not in g.keys():
        g[row[1]]=[row[0]]
    else:
        g[row[1]].append(row[0])
for k,v in g.items():
    g[k]=sorted(v)

def bfs(graph, start):
   explored = []
   queue = [start]
   process = 0
   while queue:
       node = queue.pop(0)
       if node not in explored:
           explored.append(node)
           neighbours = graph[node]
           for neighbour in neighbours:
               queue.append(neighbour)
       if (len(explored)) / 2643.46 >= process:
           process += 1
           sys.stdout.write('\rBFS Process:{}%'.format(process))
   return explored
t1=time.clock()
result=bfs(g,0)
t2=time.clock()
print(result)

f=open('./4.5-BFS-Result.txt','w')
for d in result:
    f.write(str(d)+'\n')
f.close()
print('>>>Done\n>>>BFS Result recorded.')
print('>Time taken:{:.5f} sec'.format(t2-t1))
