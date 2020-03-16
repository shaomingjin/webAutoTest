#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/12 0012 下午 13:06 
# @Author : ShaoMingJin
from view import View
import time

def main():
    view=View()
    if view.printAdminView()==-1:
        return -1

    while True:
        #等待用户输入操作业务编号
        view.printSysFunctionView()
        option=input("请输入您的业务操作编号：")
        if option=="1":
            print("执行开户操作")
        elif option=="2":
            print("执行查询操作")
        elif option=="3":
            print("执行取款操作")
        elif option=="4":
            print("执行存款操作")
        elif option=="5":
            print("执行转账操作")
        elif option=="6":
            print("执行改密操作")
        elif option=="7":
            print("执行锁定操作")
        elif option=="8":
            print("执行解锁操作")
        elif option=="9":
            print("执行补卡操作")
        elif option=="0":
            print("执行注销操作")
        elif option=="t":
            print("执行退出操作")

        time.sleep(2)
if __name__ == '__main__':
    main()


