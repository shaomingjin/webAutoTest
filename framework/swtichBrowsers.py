#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/7 0007 上午 11:41 
# @Author : ShaoMingJin
from selenium import webdriver
from framework.logger import Logger
class SelectBrowser(object):

    logger =Logger()
    '根据传入参数，选择浏览器'
    def selectBrowser(self, browserName):
        try:
            if browserName == 'Chrome':
                driver = webdriver.Chrome()
                return driver
            elif browserName == 'IE' or browserName=='ie' or browserName=='internet explorer':
                driver = webdriver.Ie()
                return driver
            elif browserName == 'Firefox':
                driver = webdriver.Firefox()
                return driver
            elif browserName=='edge' or browserName=='Edge':
                driver=webdriver.Edge()
                return driver
        except:
            self.logger.info("没有找到 %s 浏览器"%browserName)



