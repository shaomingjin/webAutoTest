#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 0009 下午 14:59 
# @Author : ShaoMingJin

#此处是全局变量
name="这是全局变量"
class Person(object):
    #此处为类变量
    name="这是类变量"
    def __init__(self,newPersonName):
        #self.name=newPersonName
        name=newPersonName
    def sayYourName(self):
        #此处name是类变量
        print("My name is %s" %self.name)
        print("全局变量的名字是：%s"%name)
        print("此处是类的name是：%s" %Person.name)

if __name__ == '__main__':
    person=Person("邵伟宸")
    #person.sayYourName()
    #print(person.name)
    Person.sayYourName(person)


