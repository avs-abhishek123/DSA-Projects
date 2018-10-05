# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:34:26 2018
Homework 3 Question 4
@author:  Ruiyu Zhang
"""

class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil
class RBTreeNode(object):
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size=None

def LeftRotate( T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
def RightRotate( T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
def RBInsert( T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'red'
    RBInsertFixup(T, z)
    return z.key, 'color=', z.color
def RBInsertFixup( T, z):
    while z.parent.color == 'red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    LeftRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                RightRotate(T,z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    RightRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                LeftRotate(T, z.parent.parent)
    T.root.color = 'black'
def RBTransplant( T, u, v):
    if u.parent == T.nil:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent
def TreeMinimum( x):
    while x.left != T.nil:
        x = x.left
    return x
def Midsort(x):
    global count
    if x!= None:
        Midsort(x.left)
        #if x.key!=0:
            #if x.color == 'red':
                #count+=1
        Midsort(x.right)
def Search(T, key, x=False):
    "find node according to key, return self.nil if not found"
    global count
    if x is False:
        x = T.root
    while (x is not T.nil) and (key != x.key):
        if key < x.key:
            x = x.left
            count+=1
        else:
            x = x.right
            count+=1
    return x
def readlist(name):
    global path
    fetched=[]
    f=open(path+name,'r')
    fetched=(f.read().splitlines())
    #print(fetched)
    return fetched
def average(list):
    all=0
    for i in list:
        all+=float(i)
    return (all/len(list))
def str_makeup(str,length):
    #modify a string to given length
    if len(str)>length:
        str=str[0:length-1]
    while len(str)<length:
        str+=' '
    return str
def random_list(length,seed=65):
    import random
    random.seed(seed)
    list=[]
    while len(list)<length:
        newint=int(random.random()*1000000)
        if newint not in list:
            list.append(newint)
    return list



#!!!plz modify this data_path to run demo on your device!!!
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
path='./'
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
count=0
trials=1000
N_min=9701
N_max=10000
#l=readlist('select-data.txt')
l=[]
def main():
    import random
    import numpy as np
    import time
    global trials, count, N_max,l,path
    start=time.time()
    print(str_makeup('N',10)+str_makeup('AVERAGE',15)+'STD-DEVIATION'+'\n')
    f=open(path+'3.4_result_9701-10000.txt','w')
    f.write(str_makeup('N',10)+str_makeup('AVERAGE',15)+str_makeup('STD-DEVIATION',15)+'     AV: COUNT / N'+'\n\n')
    for n in range(N_min,N_max+1):
        val,val2=[],[]
        t=RBTree()
        for trial in range(trials):
            #keys=random_list(n,n*trial)
            random.seed(n*trial)
            keys=random.sample(range(1000000),n)
            t=RBTree()
            for key in keys:
                RBInsert(t,RBTreeNode(key))
            count=0
            #random.seed(n,n*trial*(-3))
            target=keys[random.randrange(0,len(keys),1)]
            Search(t,target)
            val.append(count)
            val2.append(count/n)
        print(str_makeup(str(n),10)+str_makeup(str(average(val)),15)+str(np.std(val)))
        f.write(str_makeup(str(n),10)+str_makeup(str(average(val)),15)+str_makeup(str(np.std(val)),15)+'     '+str_makeup(str(average(val2)),15)+'\n')
    f.close()
    elapsed=time.time()-start
    m, s = divmod(elapsed, 60)
    h, m = divmod(m, 60)
    print('\nTime elapsed:',"%02d:%02d:%02d" % (h, m, s))

if __name__=='__main__':
    main()




