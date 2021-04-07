#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/15/2020 16:04 
# @Author : Julia
# @Version：V 0.1
# @File : d2.py
# @desc :

import pandas as pd

df = pd.read_excel(r'C:\Users\julizhou\Downloads\2020年终绩效考核表.xlsx',sheet_name='业务评分标准')
data = df.head()
print('获取到的所有的值：\n{0}'.format(data))
