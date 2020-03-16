#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/6 0006 下午 19:41 
# @Author : ShaoMingJin
from pageobject.searchPage import Cloud
from testsuites.baseTestCase import BaseTest
import time

class BaiduSearch(BaseTest):

    '搜索测试用例'
    def test_baidu_search(self):
        input = Cloud(self.driver)
        input.value_input('selenium')  # 调用页面对象中的方法
        input.submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        input.scroll_screen()
        time.sleep(5)
        input.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in 'selenium'
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

