#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/12 0012 下午 13:07 
# @Author : ShaoMingJin
import time
class View(object):

    #类属性
    admin="1"
    passWord="1"

    def printAdminView(self):
        print("*****************************************************")
        print("*                                                   *")
        print("*                                                   *")
        print("*                 欢迎登录中国光大银行                *")
        print("*                                                   *")
        print("*                                                   *")
        print("*****************************************************")
        inputAdmin=input("请输入管理员账号：")
        if self.admin!=inputAdmin:
            print("账号输入错误！")
            return -1
        inputWord=input("请输入管理密码：")
        if self.passWord!=inputWord:
            print("密码输入错误！")
            return -1
        print("登录成功！请稍后......")
        time.sleep(2)
        return 0

    def printSysFunctionView(self):
        print("*****************************************************")
        print("*    开户(1)                              查询(2)    *")
        print("*    取款(3)                              存款(4)    *")
        print("*    转账(5)                              改密(6)    *")
        print("*    锁定(7)                              解锁(8)    *")
        print("*    补卡(9)                              注销(0)    *")
        print("*    开户(1)                              查询(2)    *")
        print("*                          退出(t)                   *")
        print("*****************************************************")

