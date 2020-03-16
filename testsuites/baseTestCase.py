#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/6 0006 下午 15:28 
# @Author : ShaoMingJin
import unittest
import os
from framework.base_page import BasePage
from framework.swtichBrowsers import SelectBrowser
from framework.readInI import ReadInI
from framework.logger import Logger
import time

'定义测试用例基类'
class BaseTest(unittest.TestCase):

    '定义类变量'
    read = ReadInI()
    filePath = os.path.dirname(os.path.abspath(".")) + "\\config\\serverConfig\\config.ini"
    dict = read.readProperty(filePath, 'browserType')
    select = SelectBrowser()
    browserName = dict.get("browserName")
    url = dict.get("url")
    logger =Logger()

    #浏览器初始化
    def setUp(self):
        # 驱动浏览器
        self.driver =self.select.selectBrowser(self.browserName)
        #隐士等待10秒钟
        self.driver.implicitly_wait(10)
        #浏览器最大化
        self.driver.maximize_window()
        #打开被测网址
        base = BasePage(self.driver)
        base.open(self.url)

    #浏览器退出
    def tearDown(self):
        m = 5
        while m > 0:
            self.logger.info('还需等待%d秒钟退出浏览器' % m)
            m = m-1
            time.sleep(1)
            if m == 0:
                self.driver.quit()

if __name__ == '__main__':
    unittest.main()



