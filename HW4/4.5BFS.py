# -*- coding: utf-8 -*-
"""
Created on APR 9 2018

@author: Ruiyu Zhang
"""
import sys
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


def BFS(g):
    start=sorted(g.keys())[0]
    se,qu=[],[start]#sequence,stack
    sys.stdout.write('BFS Process:0')
    process=0
    while qu:
        this=qu.pop(0)
        if this not in se:
            se.append(this)
            new=g[this]
            for ne in new:
                if ne in se:
                    new.remove(ne)
            qu.extend(new)
        if (len(se)*100)/264346>=process:
            process+=0.1
            sys.stdout.write('\rBFS Process:{:.1f}%'.format(process))
    return se

result = BFS(g)
f = open('./4.5-BFS-Result.txt', 'w')
for d in result:
    f.write(str(d) + '\n')
f.close()
sys.stdout.write('\r>>>Done\n>>>BFS Result recorded.')
