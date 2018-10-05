# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:22:53 2018
Homework 3 Question 1
@author:  Ruiyu Zhang
"""
def cmp(x,y):
     #x,y=float(x),float(y)
     if x<y:return -1
     elif x>y:return 1
     else:return 0
def str_makeup(st,length):
    #modify a string to given length
    st=str(st)
    if len(st)>length:
        st=st[0:length-1]
    while len(st)<length:
        st+=' '
    return st

class RBT(object):

    class Node(object):
        def __init__(self,key,value=None,color=False,N=1):
            self.key = key
            self.val = value
            self.color = color   #False for Black, True for Red
            self.N = N           #Total numbers of nodes in this subtree
            self.left = None
            self.right = None
        def __cmp__(l,r):
            return cmp(l.key,r.key)
        def __eq__(l,r):
            return True if l.key == r.key else False
        def __add__(l,r):
            l.value + r.value
        def reduce(self,new_val):
            self.val.extend(new_val)

    def __init__(self):
        self.root = None

    def get(self,key):
        return  self.__get(self.root,key)

    def put(self,key,val):
        self.root = self.__put(self.root,key,val)
        self.root.color = False

    def append(self,key,val):
        self.root = self.__append(self.root,key,val)
        self.root.color = False

    def delete(self,key):
        if not self.contains(key):
            raise LookupError('No such keys in rbtree. Fail to Delete')
            return False
        if self.__is_black(self.root.left) and self.__is_black(self.root.right):
            self.root.color = True
        self.root = self.__delete(self.root,key)
        if not self.is_empty():
            self.root.color = False
        return True

    def del_min(self):
        if self.is_empty():
            raise LookupError('Empty dictionary.')
        if self.__is_black(self.root.left) and self.__is_black(self.root.right):
            self.root.color = True
        self.root = self.__del_min(self.root)
        if not self.is_empty(): self.root.color = False

    def del_max(self):
        if self.is_empty():
            raise LookupError('Empty dictionary.')
        if self.__is_black(self.root.left) and self.__is_black(self.root.right):
            self.root.color = True
        self.root = self.__del_max(self.root)
        if not self.is_empty(): self.root.color = False

    def size(self):
        return self.__size(self.root)

    def is_empty(self):
        return not self.root

    def contains(self,key):
        return bool(self.get(key))



    def min(self):
        if self.is_empty():
            return None
        return self.__min(self.root).key

    def max(self):
        if self.is_empty():
            return None
        return self.__max(self.root).key

    def floor(self,key):
        x = self.__floor(self.root,key)
        if x:
            return x.key,x.val
        else:
            return None,None

    def ceil(self,key):
        x = self.__ceil(self.root,key)
        if x:
            return x.key,x.val
        else:
            return None,None

    def below(self,key):
        index = self.index(key)
        if not 0 <= index - 1 < self.size():
            return None,None    #Return None if out of range
        x = self.__select(self.root,index - 1)
        return x.key,x.val

    def above(self,key):
        index = self.index(key)
        if self.contains(key):
            if not 0 <= index + 1 < self.size():
                return None,None    #Return None if out of range
            else:
                x = self.__select(self.root,index+1)
                return x.key,x.val
        else:#if key is not in tree. then select(i) is what we need
            if not 0 <= index < self.size():
                return None,None    #Return None if out of range
            else:
                x = self.__select(self.root,index)
                return x.key,x.val

    def index(self,key):
        return self.__index(self.root,key)

    def keys(self):
        '''All Keys in the tree '''
        return self.range(self.min(),self.max())

    def range(self,lo,hi):
        '''Take two keys. return keys between them'''
        q = []
        self.__range(self.root,q,lo,hi)
        return q

    def select(self,index):
        '''Given Index Return Corresponding key'''
        if not 0 <= index < self.size():
            return None
        return self.__select(self.root,index).key

    def width(self,lo,hi):
        '''Return the numbers of keys between lo and hi '''
        if lo > hi:
            return 0
        if self.contains(hi):
            return self.index(hi) - self.index(lo) + 1
        else:
            return self.index(hi) - self.index(lo)

    def __get(self,x,key):
        while x:
            tag = cmp(key,x.key)
            if tag < 0 : x = x.left
            elif tag > 0 :x = x.right
            else: return x.val

    def __put(self,h,key,val):
        if not h:
            return self.Node(key,val,True,1)
        tag = cmp(key,h.key)
        if tag < 0:
            h.left = self.__put(h.left,key,val)
        elif tag > 0:
            h.right = self.__put(h.right,key,val)
        else:
            h.val = val   #Update
        if self.__is_black(h.left) and self.__is_red(h.right):
            h = self.__rotate_left(h)
        if self.__is_red(h.left) and self.__is_red(h.left.left):
            h = self.__rotate_right(h)
        if self.__is_red(h.left) and self.__is_red(h.right):
            self.__flip_colors(h)
        h.N = self.__size(h.left) + self.__size(h.right) + 1
        return h
    def __append(self,h,key,val):
        if not h:
            return self.Node(key,val,True,1)
        tag = cmp(key,h.key)
        if tag < 0:
            h.left = self.__append(h.left,key,val)
        elif tag > 0:
            h.right = self.__append(h.right,key,val)
        else:
            h.reduce(val)   #append.
        if self.__is_black(h.left) and self.__is_red(h.right):
            h = self.__rotate_left(h)
        if self.__is_red(h.left) and self.__is_red(h.left.left):
            h = self.__rotate_right(h)
        if self.__is_red(h.left) and self.__is_red(h.right):
            self.__flip_colors(h)
        h.N = self.__size(h.left) + self.__size(h.right) + 1
        return h
    def __del_min(self,h):
        if not h.left: #if h is empty:return None
            return None
        if self.__is_black(h.left) and self.__is_black(h.left.left):
            self.__move_red_left(h)
        h.left = self.__del_min(h.left) #Del recursive
        return self.__balance(h)
    def __del_max(self,h):
        if self.__is_red(h.left):
            h = self.__rotate_right(h)
        if not h.right:
            return None
        if self.__is_black(h.right) and self.__is_black(h.right.left):
            h = self.__move_red_right(h)
        h.right = self.__del_max(h.right)
        return self.__balance(h)
    def __delete(self,h,key):
        if key < h.key:
            if self.__is_black(h.left) and self.__is_black(h.left.left):
                h = self.__move_red_left(h)
            h.left = self.__delete(h.left,key)
        else:
            if self.__is_red(h.left):
                h = self.__rotate_right(h)
            if key == h.key and not h.right:
                return None
            if self.__is_black(h.right) and self.__is_black(h.right.left):
                h = self.__move_red_right(h)
            if key == h.key:#replace h with min of right subtree
                x = self.__min(h.right)
                h.key = x.key
                h.val = x.val
                h.right = self.__del_min(h.right)
            else:
                h.right = self.__delete(h.right,key)
        h = self.__balance(h)
        return h

    def __min(self,h):
        if not h.left:
            return h
        else:
            return self.__min(h.left)

    def __max(self,h):
        if not h.right:
            return h
        else:
            return self.__max(h.right)

    def __floor(self,h,key):
        '''Find the NODE with key <= given key in the tree rooted at h '''
        if not h:
            return None
        tag = cmp(key,h.key)
        if tag == 0:
            return h
        if tag < 0:
            return self.__floor(h.left,key)
        t = self.__floor(h.right,key)
        if t:#if find in right tree
            return t
        else:#else return itself
            return h

    def __ceil(self,h,key):
        '''Find the NODE with key >= given key in the tree rooted at h '''
        if not h:
            return None
        tag = cmp(key,h.key)
        if tag == 0:
            return h
        if tag > 0: # key is bigger
            return self.__ceil(h.right,key)
        t = self.__ceil(h.left,key)#key is lower.Try to find ceil left
        if t:#if find in left tree
            return t
        else:#else return itself
            return h

    def __index(self,h,key):
        if not h:
            return 0
        tag = cmp(key,h.key)
        if tag < 0:
            return self.__index(h.left,key)
        elif tag > 0:   #Key is bigger
            return self.__index(h.right,key) + 1 + self.__size(h.left)
        else:   #Eq
            return self.__size(h.left)

    def __select(self,h,index):
        '''assert h. assert 0 <= index < size(tree) '''
        l_size = self.__size(h.left)
        if l_size > index:
            return self.__select(h.left,index)
        elif l_size < index:
            return self.__select(h.right,index - l_size - 1)
        else:
            return h

    def __range(self,h,q,lo,hi):
        if not h:
            return
        tag_lo = cmp(lo,h.key)
        tag_hi = cmp(hi,h.key)
        if tag_lo < 0:#lo key is lower than h.key
            self.__range(h.left,q,lo,hi)
        if tag_lo <= 0 and tag_hi >= 0:
            q.append(h.key)
        if tag_hi > 0 :# hi key is bigger than h.key
            self.__range(h.right,q,lo,hi)



    def __rotate_right(self,h):
        x = h.left
        h.left,x.right = x.right,h
        x.color,x.N = h.color,h.N
        h.color,h.N = True,self.__size(h.left) + self.__size(h.right) + 1
        return x

    def __rotate_left(self,h):
        x = h.right
        h.right,x.left = x.left,h
        x.color,x.N = h.color,h.N
        h.color,h.N = True,self.__size(h.left) + self.__size(h.right) + 1
        return x

    def __flip_colors(self,h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def __move_red_left(self,h):
        self.__flip_colors(h)
        if self.__is_red(h.right.left):
            h = self.__rotate_left(h)
        return h

    def __move_red_right(self,h):
        self.__flip_colors(h)
        if self.__is_red(h.left.left):
            h = self.__rotate_right(h)
        return h

    def __balance(self,h):
        if self.__is_red(h.right):
            h = self.__rotate_left(h)
        if self.__is_red(h.left) and self.__is_red(h.left.left):
            h = self.__rotate_right(h)
        if self.__is_red(h.left) and self.__is_red(h.right):
            self.__flip_colors(h)
        h.N = self.__size(h.left) + self.__size(h.right) + 1
        return h

     #Class Method

    @staticmethod
    def __is_red(x):
        return False if not x else x.color

    @staticmethod
    def __is_black(x):
        return True  if not x else not x.color

    @staticmethod
    def __size(x):
        return 0 if not x else x.N


class ST(object):
    def __init__(self):
        self.size=0
        self.table=RBT()
    def add(self,key,val):
        self.table.put(key,val)
        self.size+=1
    def remove(self,key):
        re=table.delete(key)
        if re is False:
            raise LookupError('Key not found.')
        else:
            size-=1
    def get(self,key):
        return self.table.get(key)
    def isEmpty(self):
        return not bool(self.size)
    def contains(self,key):
        val=table.get(key)
        if val is not None:
            return True
        else:
            return False
    def size(self):
        return size
    def floor(self,key):
        return table.floor(key)
    def ceil(self,key):
        return table.ceil(key)
    def removemax(self):
        self.table.del_max()
    def removemin(self):
        self.table.del_min()
    def keys(self):
        return self.table.keys()
    def summary(self):
        print('\nSize=',self.size)
        print('isEmpty=',self.isEmpty())
        print('----------------------------------')
        print(str_makeup('NUM', 5) + str_makeup('KEY', 20) + str_makeup('VALUE', 20)+'\n')
        for tag,key in enumerate(self.keys()):
            print(str_makeup(tag,5)+str_makeup(key,20)+str_makeup(self.table.get(key),20))
        print('----------------------------------')

def main():

    StarTrailer=ST()
    StarTrailer.add('Chengdu','DuskPiper')
    StarTrailer.add('Beijing','BigXhead')
    StarTrailer.add('Chongqing','CharlieQ')
    StarTrailer.summary()

if __name__=='__main__':
    main()