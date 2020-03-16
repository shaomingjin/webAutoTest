#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/14 0006 下午 21:58
# @Author : ShaoMingJin
import os
from configobj import ConfigObj

class ReadInI(object):

    '读取配置文件，返回一个字典'
    def readProperty(self,filePath,str):
        config = ConfigObj(filePath, encoding='UTF8')
        # 读配置文件
        dict =config[str]
        return dict

if __name__ == '__main__':
    filePath = os.path.dirname(os.path.abspath(".")) + "\\config\\serverConfig\\config.ini"
    read =ReadInI()
    dict =read.readProperty(filePath,'browserType')
    print(dict)
    print( dict.get('browserName'))
