#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 0009 下午 19:44 
# @Author : ShaoMingJin
from openpyxl import Workbook#创建文件对象
import datetime
wb =Workbook()
#获取一个sheet
sheet=wb.active

# 将数据写入到指定的单元格
sheet['A1'] = 42      #写入数字
sheet['A2'] = datetime.datetime.now()    #写入一个当前时间
sheet['B1'] = "自动化"+"automation test" #写入中文
sheet.append([1, 2, 3])    #写入多个单元格
#保存为a.xlsx
wb.save("a.xlsx")