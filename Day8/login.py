#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/20/2020 15:17 
# @Author : Julia
# @Version：V 0.1
# @File : login.py
# @desc :
import uuid
import sys
import json


class Login(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def register(self):
        temp = self.username + '|' + self.password
        json.dump(temp,open('login.md','w'))

    def login(self):
        f = json.load(open('login.md','r'))
        lists = f.split('|')
        if lists[0] == self.username and lists[1] == self.password:
            return True
        else:
            return False

    def profile(self):
        f = str(json.load(open('login.md', 'r')))
        list1 = f.split('|')
        r = self.login()
        if r:
            print('恭喜登录成功，您的账号为:{0}'.format(list1[0]))
        else:
            print('Sorry, 登录失败')

    def exit(self):
        sys.exit(1)

def main():
    per = Login('julia','admin')
    while True:
        p = int(input('1. 登录  2. 注册 3. 退出 \n'))
        if p == 1:
            per.login()
            per.profile()
        elif p == 2:
            per.register()
        elif p == 3:
            per.exit()
        else:
            break

if __name__ == '__main__':
    main()
