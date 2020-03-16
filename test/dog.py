#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 0009 下午 15:30 
# @Author : ShaoMingJin

class Dog(object):
    kind ="canine"
    country="China"

    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country

dog=Dog("Lili",3,"Britain")
dog.kind="xiaogou"
print(dog.name,dog.age,Dog.kind,dog.country)

print(dog.__dict__)
dog.kind="felline"
print(dog.name,dog.age,dog.kind,dog.country)
print(dog.__dict__)