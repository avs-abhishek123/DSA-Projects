# -*- coding: utf-8 -*-
"""
Created on APR 9 2018

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
INF=9999999
def str_makeup(st, length):
    if len(st) > length:return st[0:length - 1]
    while len(st) < length:st += ' '
    return st
def print_dis(dis):
    global INF
    for key,val in dis.items():
        if val<INF:
            print(key,str_makeup(': {:.2f}'.format(val),12),end='')
        else:
            print(key,str_makeup(': NoAcc',12),end='')
    print('')


def DJ(v0):
    global nodes,weight,INF
    dis={i:INF for i in nodes}
    dis[v0]=0
    for run in range(len(nodes)):
        for n in nodes:
            for target in nodes:
                if n==target:
                    continue
                if (n,target) in weight.keys():
                    if weight[(n, target)] + dis[n] < dis[target] and dis[n] < INF:
                        dis[target] = weight[(n, target)] + dis[n]
        print_dis(dis)


for i in nodes:
    print('\nSTART=',i)
    DJ(i)

