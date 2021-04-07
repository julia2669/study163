#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/11/2020 18:56 
# @Author : Julia
# @Version：V 0.1
# @File : jsonTest.py
# @desc :

import json
import requests

'''
序列化：把python数据类型转为str的类型的过程
反序列化：把str的类型转为python的数据类型
'''

'''字典的序列化与反序列化'''
print('''字典的序列化与反序列化''')
dic = {"age": 18, 'name': 'julia'}
# 序列化： dic-->str
dic_str = json.dumps(dic)
print('序列化后的结果：\n', dic_str, '\n', type(dic_str))
# 反序列化： str-->dic
str_dic = json.loads(dic_str)
print('反序列化后的结果：\n', str_dic, '\n', type(str_dic), '\n', '\n')

'''列表的序列化与反序列化'''
print('''列表的序列化与反序列化''')
list1 = ['julia', 'xxx', 'shiXue']
# 序列化： list1-->str
lis_str = json.dumps(list1)
print('序列化后的结果：\n', lis_str, '\n', type(lis_str))
# 反序列化： str-->list1
str_lis = json.loads(lis_str)
print('反序列化后的结果：\n', str_lis, '\n', type(str_lis), '\n', '\n')

'''元组的序列化与反序列化'''
print('''元组的序列化与反序列化''')
tup = (1, 2, 3, 4)
# 序列化： tup-->str
tup_str = json.dumps(tup)
print('序列化后的结果：\n', tup_str, '\n', type(tup_str))
# 反序列化： str-->tup
str_tup = json.loads(tup_str)
print('反序列化后的结果：\n', str_tup, '\n', type(str_tup), '\n', '\n')

'''文件的序列化与反序列化'''
print('''文件的序列化与反序列化''')
r = requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')
print(json.dumps(r.content.decode('utf-8')))
# 对文件序列化就是把服务端的响应数据写到文件中
json.dump(r.content.decode('utf-8'), open('weather.json', 'w')) ##Object of type bytes is not JSON serializableObject of type bytes is not JSON serializable
print('序列化后的结果：', '查看文件weather.json', '\n')
# 对文件的反序列化就是读取文件的内容
'''
1. 文件反序列化后---类型是Unicode
2. 进行编码，把Unicode类型转为str
3. 然后使用放序列化把str转为字典类型
'''

print('反序列化后的结果：')
dic2 = json.loads(json.load(open('weather.json', 'r')).encode('utf-8')) ##string indices must be integers
print(dic2, '\n', type(dic2))
print(dic2['weatherinfo']['city'])


r = requests.get(url='http://www.weather.com.cn/data/sk/101020100.html')
print(json.dumps(r.content.decode('utf-8')))
# 对文件序列化就是把服务端的响应数据写到文件中
json.dump(r.content.decode('utf-8'), open('weather.json', 'w'))
print('序列化后的结果：', '查看文件weather.json', '\n')
# 对文件的反序列化就是读取文件的内容
print('反序列化后的结果：')
dic2 = json.load(open('weather.json', 'r'))
print(dic2, '\n', type(dic2))
# print(dic2['weatherinfo']['city'])
