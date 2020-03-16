#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/6 0006 下午 15:30 
# @Author : ShaoMingJin
import time
from framework.base_page import BasePage
from framework.logger import Logger
from framework.readInI import ReadInI
import os

class Cloud(BasePage):
    '实例化'
    logger = Logger()
    read = ReadInI()
    filePath = os.path.dirname(os.path.abspath(".")) + "\\config\\obj\\searchPageElement.ini"
    dict = read.readProperty(filePath, 'WebElement')

    '构造函数初始化'
    def __init__(self,driver):
        super(Cloud, self).__init__(driver)

    '获取输入框元素'
    def getInputBoxElement(self):
        return self.getElementObject(self.dict.get('inputbox'))

    '获取搜索按钮元素'
    def getSearchBtnElement(self):
        return self.getElementObject(self.dict.get('searchbutton'))

    '搜索输入框输入内容'
    def value_input(self, text):
        if self.isDisplay(self.getInputBoxElement()):
          self.send_keys(self.getInputBoxElement(), text)

    '点击搜索'
    def submit_btn(self):
        self.click(self.getSearchBtnElement())
        time.sleep(2)

    def scroll_screen(self):
        self.scroll_screen_down()



