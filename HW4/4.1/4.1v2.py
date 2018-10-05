# -*- coding: utf-8 -*-
"""
Created on APR 7 2018

@author: Ruiyu Zhang
"""
import sys
path='./'
num=0

def read_graph(name='mediumEWG.txt'):
    global num
    f,data=open(path+name,'r'),[]
    raw=f.read().splitlines()
    f.close()
    num=int(raw[0])
    link=int(raw[1])
    raw=raw[2:]
    for row in raw:
        nums=row.split(' ')
        data.append([int(nums[0]),int(nums[1]),float(nums[2])])
    return data
def dfs(node, graph, visited):
    global stack,cycle
    visited[node] = True
    stack.append(node)
    if node in graph.keys():
        for n in graph[node]:
            if n not in stack:
                dfs(n, graph, visited)
            else:
                #found cycle
                index = stack.index(n)
                cy=set(stack[index:])
                if cy not in cycle:
                    cycle.append(cy)
                return
    stack.pop(-1)
data=read_graph()
data=[[i[0],i[1]] for i in data]

graph = {}
visited = {}
stack = []
cycle=[]
for i in data:
    n1, n2 = i[0],i[1]
    if n1 not in graph.keys():
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    n2, n1 = i[0], i[1]
    if n1 not in graph.keys():
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    if n1 not in visited:
        visited[n1] = False
    if n2 not in visited:
        visited[n2] = False
for node in visited.keys():
    if not visited[node]:
        dfs(node, graph, visited)


print('\nFound at least {} cycles.'.format(len(cycle)))
f=open('.\\cycles.txt','w')
for c in cycle:
    c=list(c)
    for n in c:
        f.write(str(n)+'-')
    f.write(str(c[0])+'\n')