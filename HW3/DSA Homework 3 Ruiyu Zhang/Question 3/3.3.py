# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:12:56 2018
Homework 3 Question 3
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
        if x.key!=0:
            if x.color == 'red':
                count+=1
        Midsort(x.right)
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
def readlist(name):
    global path
    fetched=[]
    f=open(path+name)
    fetched=(f.read().splitlines())
    #print(fetched)
    return fetched


#!!!plz modify this data_path to run demo on your device!!!
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
path='./'
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
trial=100
count=0
perc_all=[]
def main():
    global count, trial
    import random
    n=[10000,100000,1000000]
    l=readlist('select-data.txt')
    l=list(set(l))
    for ni in n:
        for p in range(trial):
            t=RBTree()
            keys=l[:ni]
            random.shuffle(keys)
            for key in keys:
                RBInsert(t,RBTreeNode(key))
            Midsort(t.root)
            perc=count/ni
            count=0
            perc_all.append(perc)
        av=average(perc_all)
        print('\n',str_makeup('N='+str(ni),10),', percentage=',av)

    print('\n Trial=',trial)




if __name__ == '__main__':
    main()