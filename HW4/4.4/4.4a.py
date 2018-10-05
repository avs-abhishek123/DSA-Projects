# -*- coding: utf-8 -*-
"""
Created on Wed APR 8 2018

@author: Ruiyu Zhang
"""
nodes=set([0,1,2,3,4,5,6,7])
weight={(4,5):0.35,
        (5,4):0.35,
        (5,7):0.28,
        (7,5):0.28,
        (5,1):0.32,
        (0,4):0.38,
        (0,2):0.26,
        (7,3):0.39,
        (1,3):0.29,
        (2,7):0.34,
        (6,2):-1.20,
        (3,6):0.52,
        (6,0):-1.40,
        (6,4):-1.25}
def edge(weight):
    v1,v2,w=[],[],[]
    for (i,j)in weight:
        if weight[(i,j)]!=0:
            w.append(weight[(i,j)])
            v1.append(i)
            v2.append(j)
    return v1,v2,w
def BF(v0):
    INF = 9999999
    global weight,nodes
    v1, v2, w = edge(weight)
    dis = dict((k, INF) for k in nodes)
    dis[v0] = 0
    print('\nSTART=', v0)
    for i in range(len(dis)):
        if i == v0: continue
        print(str_makeup('END=' + str(i), 10), end='')
    print('')
    for k in range(len(nodes) - 1):
        check = 0
        for i in range(len(w)):
            if dis[v1[i]] + w[i] < dis[v2[i]]:
                dis[v2[i]] = dis[v1[i]] + w[i]
                check = 1
        if check == 0: break

        track_print(dis,v0)

    flag = 0
    for i in range(len(w)):
        if dis[v1[i]] + w[i] < dis[v2[i]]:
            flag = 1
            break
    track_print(dis,v0)
    if flag == 1:
        return False
    return dis
def track_print(dis,v0):
    for i,d in sorted(dis.items()):
        if i==v0:continue
        if d>99999:
            print(str_makeup('NoAccess',10),end='')
        else:
            print(str_makeup('{:.2f}'.format(d),10),end='')
    print('\n',end='')
def str_makeup(st, length):
    st=str(st)
    if len(st) > length:return st[0:length - 1]
    while len(st) < length:
        st += ' '
    return st


for v0 in nodes:
    distance=BF(v0)
