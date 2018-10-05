# -*- coding: utf-8 -*-
"""
Created on Wed APR 8 2018

@author: Ruiyu Zhang
"""
nodes=set([0,1,2,3,4,5,6,7])
weight={(5,4):0.35,
        (4,7):0.37,
        (5,7):0.28,
        (5,1):0.32,
        (4,0):0.38,
        (0,2):0.26,
        (3,7):0.39,
        (1,3):0.29,
        (7,2):0.34,
        (6,2):0.40,
        (3,6):0.52,
        (6,0):0.58,
        (6,4):0.93}
class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=[]
    def construct(self):
        global weight
        for k in weight.keys():
            if k[0]==self.val:
                new_son=Node(k[1])
                new_son.construct()
                self.next.append(new_son)
    def walk(self):
        for n in self.next:
            n._walk(0,self.val)
    def _walk(self,past_len,past_num):
        global weight,dest
        if past_num!=self.val:new_len=past_len+weight[(past_num,self.val)]
        else:new_len=past_len
        dest[self.val].append(new_len)
        for n in self.next:
            n._walk(new_len,self.val)

f=open('.\\4.3-result.txt','w')
for n in nodes:
    root=Node(n)
    root.construct()
    dest={}
    for m in nodes-set([n]):dest[m]=[]
    root.walk()
    print('\nSTART={}'.format(n))
    f.write('\nSTART={}\n'.format(n))
    for k,v in dest.items():
        print('END={}'.format(k),end=': ')
        f.write('END={}: '.format(k))
        if not len(v):
            print('No Access')
            f.write('No Access\n')
        else:
            print('Long={:.2f}  Short={:.2f}'.format(max(v),min(v)))
            f.write('Long={:.2f}  Short={:.2f}\n'.format(max(v),min(v)))
f.close()