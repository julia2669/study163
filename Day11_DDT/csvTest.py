#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/21/2021 11:17 
# @Author : Julia
# @Version：V 0.1
# @File : csvTest.py
# @desc :

import csv

def readCsvList():
    with open('csvTest.csv','r') as f:
        reader = csv.reader(f)
        next(reader)
        data = reader


data = [
    ("测试1",'软件测试工程师'),
    ("测试2",'软件测试工程师'),
    ("测试3",'软件测试工程师'),
    ("测试4",'软件测试工程师'),
    ("测试5",'软件测试工程师'),
]
def writeCsv(data):
    with open('csvTest.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in data:
            writer.writerow(i)

writeCsv(data)