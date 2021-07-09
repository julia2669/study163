#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 6/30/2021 18:09 
# @Author : Julia
# @Version：V 0.1
# @File : namecheck.py
# @desc :
import re
'''小美是美团的前端工程师，为了防止系统被恶意攻击，小美必须要在用户输入用户名之前做一个合法性检查，一个合法的用户名必须满足以下几个要求：

用户名的首字符必须是大写或者小写字母。
用户名只能包含大小写字母，数字。
用户名需要包含至少一个字母和一个数字。
如果用户名合法，请输出 "Accept"，反之输出 "Wrong"。
格式：

输入：
- 输入第一行包含一个正整数 T，表示需要检验的用户名数量。
- 接下来有 T 行，每行一个字符串 s，表示输入的用户名。
输出：
- 对于每一个输入的用户名 s，请输出一行，即按题目要求输出一个字符串。
'''

pattern = '^[a-zA-Z](?=\w*\d+\w*)[a-zA-Z0-9]{1,19}'

ms = re.search(pattern,'ab2ei2s333asdgfhjkkk3')
mm = re.match(pattern,'ab2ei2s333asdgfhjkkk3')

print(ms)
print(mm)

def nameCheck():
    num = input("please input the num of names need to check: ")
    names= [0 for i in range(0,int(num))]
    for i in range(0,int(num)):
        prompt = "please input the "+str(i)+" name:"
        names[i] = input(prompt)

    for i in names:
        m = re.match(pattern,i)
        if m is not None:
            print("Accept")
        else:
            print("Wrong")

nameCheck()