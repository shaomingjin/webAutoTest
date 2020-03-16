#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/6 0006 下午 21:38 
# @Author : ShaoMingJin
# import configparser
import os
filePath=os.path.dirname(os.path.abspath("."))+"\\config\\obj\\searchPageElement.ini"
print(filePath)
# config = configparser.ConfigParser()
# config.read(open(filePath))
# test_value = config.get("browserType","browserName")

from configobj import ConfigObj
config = ConfigObj(filePath,encoding='UTF8')

# 读配置文件
dict=config['WebElement']
print(dict)
subStr=dict.get('inputbox')
key=subStr.split('->')[0]
value=subStr.split("->")[1]
print(subStr)
print(key)
print(value)
# print (config['browserType']  )
# print (config['browserType']['browserName'] )
