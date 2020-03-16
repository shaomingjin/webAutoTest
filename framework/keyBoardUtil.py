#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 0007 下午 17:15
# @Author : ShaoMingJin

class KeyBoardUtil(object):

    def __init__(self,driver):
        self.driver=driver

    '''
    #键盘操作, 回车
    :param Keys:
    '''
    def ENTER(self, element,Keys):
       element.send_keys(Keys.ENTER)

