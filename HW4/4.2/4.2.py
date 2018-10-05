# -*- coding: utf-8 -*-
"""
Created on Tue APR 7 2018

@author: Ruiyu Zhang
"""
from random import choice
import time
path='./'

def read_graph(name='mediumEWG.txt'):
    f,data=open(path+name,'r'),[]
    raw=f.read().splitlines()
    f.close()
    num=int(raw[0])
    link=int(raw[1])
    raw=raw[2:]
    for row in raw:
        nums=row.split(' ')
        data.append([int(nums[0]),int(nums[1]),float(nums[2])])
    return data#[[0,0,0.0000],]
def near(this):
    global degree,weight,mst_
    neighbor=list(degree[this])
    neighbor=remove_duplicate(neighbor,mst_)#avoid going back
    all_weight=[weight[(i,this)]for i in neighbor]
    if len(all_weight)==0:
        return (this,this)
    return (this,neighbor[all_weight.index(min(all_weight))])
def remove_duplicate(l1,l2):
    return list(set(l1)-set(l2))
def length(l):
    length=0
    global weight
    for link in l:
        if link in weight.keys():
            length+=weight[link]
        else:
            length+=weight[(link[1],link[0])]
    return length
def makes_cycle(s,g):
    union={}
    if len(g)<2:
        return False
    for link in g:
        if link[0] not in union:
            union[link[0]] = link[0]
        if link[1] not in union:
            union[link[1]] = link[1]
    for i in range(len(g)//5):
        for link in g:
            if union[link[0]]>union[link[1]]:
                union[link[0]],union[link[1]]=union[link[1]],union[link[1]]
            else:
                union[link[0]], union[link[1]] = union[link[0]], union[link[0]]
    if s[0] in union.keys() and s[1] in union.keys():
        if union[s[0]]==union[s[1]]:
            return True
    return False

data=read_graph()
degree,weight,node={},{},set([])
for link in data:
    if link[0] in degree.keys():
        degree[link[0]].add(link[1])
    else:
        degree[link[0]] = set([link[1]])
    if link[1] in degree.keys():
        degree[link[1]].add(link[0])
    else:
        degree[link[1]] = set([link[0]])
    weight[(link[0],link[1])]=link[2]
    weight[(link[1],link[0])]=link[2]
    node.add(link[0])
    node.add(link[1])

#prim's algorithm
mst,mst_=[],set([])
size=len(node)
start = choice(list(node))
mst_.add(start)
t1=time.clock()
while len(mst_)<size:
    candidate, candidate_weight = [], []
    for i in mst_:
        near_i=near(i)
        if near_i[1]!=i:
            candidate.append(near_i)
    for k in candidate:
        candidate_weight.append(weight[k])
    new_friend_link=candidate[candidate_weight.index(min(candidate_weight))]
    mst.append(new_friend_link)
    mst_.add(new_friend_link[1])
    #print('>working',len(mst_),'out of',size)
t2=time.clock()
prim=list(mst)
#kruskal's algorithm
mst,mst_=[],set([])
side,weight_=[],[]
size=len(node)
t3=time.clock()
for s,w in sorted(weight.items(),key=lambda item:item[1]):
    #print(s,w)
    s=(min(s),max(s))
    if s not in side:#no repeating
        side.append(s)
        weight_.append(w)

for i,s in enumerate(side):
    #print(i,'out of',len(side))
    if makes_cycle(s,mst):
        continue
    mst_.add(s[0])
    mst_.add(s[1])
    mst.append(s)
    t4=time.clock()
kruskal=list(mst)

#conclude
#print('\n\nPrim tree is like:\n\n',sorted(prim))
#print('\n\nKruskal tree is like:\n\n',sorted(kruskal))
print('\nPrim tree length={:.5f}'.format(length(prim)))
print('Time used:{:.5f}s'.format(t2-t1))
print('\nKruskal tree length={:.5f}'.format(length(kruskal)))
print('Time used:{:.5f}s'.format(t4-t3))





