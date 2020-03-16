#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 0009 下午 15:41 
# @Author : ShaoMingJin

class A(object):
 x = []
 y = 0
 def __init__(self):
    pass
 def add(self):
    self.x.append('1')
    self.y+=1

if __name__ == '__main__':

    a=A()
    print (a.x,a.y )
    print (A.x,A.y)
    a.add()
    print (a.x,a.y )
    print (A.x,A.y )
    b=A()
    print (b.x,b.y )
    print (A.x,A.y)