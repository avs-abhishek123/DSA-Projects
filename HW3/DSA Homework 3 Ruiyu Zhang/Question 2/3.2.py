# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:08:51 2018
Homework 3 Question 2
@author:  Ruiyu Zhang
"""
#!!!plz modify these to run demo on your device!!!
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
rounds=9 #run with N= 2 to 2^rounds #eg: N=2,4,8,16,32
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

class Node(object):
    def __init__(self,key,parent=None,left=None,right=None):
        self.key=key
        self.left=left
        self.right=right
        self.parent=parent

class BST(object):
    def __init__(self):
        self.size=0
        self.root=None
    def size(self):
        return self.size
    def subtree_size(self,thisNode):
        if thisNode is None:
            return 0
        if thisNode.left is not None:
            l=self.subtree_size(thisNode.left)
        else:
            l=0
        if thisNode.right is not None:
            r=self.subtree_size(thisNode.right)
        else:
            r=0
        return l+r+1
    def insert(self,key):
        if self.root:#not empty
            self._insert(key,self.root)
        else:#empty
            self.root=Node(key)
        self.size+=1
        return self.root
    def _insert(self,key,thisNode):
        if key<thisNode.key:#left
            if thisNode.left:#has left child
                self._insert(key,thisNode.left)
            else:#no left child
                thisNode.left=Node(key,parent=thisNode)
        elif key>thisNode.key:#right
            if thisNode.right:#has right child
                self._insert(key,thisNode.right)
            else:#no right child
                thisNode.right=Node(key,parent=thisNode)
        else:#found, already exists
            #print('!!!warning: New node already exists.')
            pass
    def search(self,key):
        if self.root:
            depth=self._search(key,self.root)
            return depth
        else:#empty tree
            return -9999999999
    def _search(self,key,thisNode):#search for depth
        if thisNode is None:#not found
            return -9999999999
        elif key==thisNode.key:#found
            return 0
        elif key>thisNode.key:
            return 1+self._search(key,thisNode.right)
        else:#key<
            return 1+self._search(key,thisNode.left)
    def rank(self,key):
        if self.root:
            return self._rank(key,self.root)
        else:#empty
            return -1
    def _rank(self,key,thisNode):
        if thisNode is None:
            return -1
        if key<thisNode.key:
            return self._rank(key,thisNode.left)
        if key>thisNode.key:
            return 1+self.subtree_size(thisNode.left)+self._rank(key,thisNode.right)
        else:#==
            if thisNode.left is not None:
                return self.subtree_size(thisNode.left)
            else:#no left child
                return 0
    def select(self,rank):
        if self.root:
            return self._select(rank,self.root)
        else:
            return None
    def _select(self,rank,thisNode):
        if thisNode is None:
            return None
        if self.rank(thisNode.key)==rank:
            return thisNode.key
        elif self.rank(thisNode.key)<rank:
            return self._select(rank,thisNode.right)
        else:#>
            return self._select(rank,thisNode.left)

def str_makeup(str,length):
    #modify a string to given length
    if len(str)>length:
        str=str[0:length-1]
    while len(str)<length:
        str+=' '
    return str
def str_make0(str,length):
    if len(str)>length:
        str=str[0:length-1]
    while len(str)<length:
        str='0'+str
    return str
def average(list):
    all=0
    for i in list:
        all+=float(i)
    return (all/len(list))

def main():
    import random
    global rounds
    print(str_makeup('N', 10) + str_makeup('N-RANDOM', 15) + 'N-SORTED' + '\n')
    for round in range(1,rounds+1):
        n=2**round
        lr=random.sample(range(1000000000),n)
        ls=sorted(lr)
        tr,ts=BST(),BST()
        for r in lr:
            tr.insert(r)
        for s in ls:
            ts.insert(s)
        len_r,len_s=[],[]
        for r in lr:
            leng=tr.search(r)
            len_r.append(leng)
        for s in ls:
            leng=ts.search(s)
            len_s.append(leng)
        print(str_makeup(str(n), 10) + str_makeup(str(average(len_r)), 15) + str_makeup(str(average(len_s)), 15))



if __name__ == '__main__':
    main()
