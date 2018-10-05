# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 14:08:53 2018
Homework 3 Question 5
@author:  Ruiyu Zhang
"""
#!!!plz modify these to run demo on your device!!!
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
path='./'
test_tag=[7]#could be random, just for sample tests
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

def readlist(name):
    global path
    fetched=[]
    f=open(path+name)
    fetched=(f.read().splitlines())
    #print(fetched)
    int_fetched=[int(i) for i in fetched]
    return int_fetched



def main():
    #import random
    global path, test_tag
    #initialize
    keys=readlist('select-data.txt')
    t=BST()
    for key in keys:
        #if t.search(key)<0:#avoid repeat
            t.insert(key)
    #test
    for r in test_tag:
        print('-------------------','\n1.RANK KEY=',r)
        print('1.RANKED  =',t.rank(r))
        print ('2.SELECT RANK=',r)
        print('2.SELECTED   =',t.select(r))
    print('-------------------')


if __name__=='__main__':
    main()


