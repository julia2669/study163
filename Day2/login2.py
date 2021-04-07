#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/2/2020 13:36 
# @Author : Julia
# @Version：V 0.1
# @File : login2.py
# @desc :

import json

'''
1.实现用户登录功能
2.实现查看用户信息
3.实现用户注册功能
'''


def typeusername():
    username = input('请输入注册用户名：\n')
    return username


def typepassword():
    password = input('请输入注册用户名密码：\n')
    return password


def register(username, password):
    """
    实现注册功能
    :param username:
    :param password:
    :return:
    """
    temp = username + '|' + password
    # with open('login.md','w') as f:
    #     f.write(temp)
    json.dump(temp, open('login.md', 'w'))


def login(username, password):
    '''
    实现登录功能
    '''
    # with open('login.md','r') as f:
    #     for line in f:
    #         lis = line.split('|')
    #         if lis[0] == username and lis[1] == password:
    #             return True
    #         else:
    #             return False
    f = str(json.load(open('login.md', 'r')))
    lis = f.split('|')
    if lis[0] == username and lis[1] == password:
        return True
    else:
        return False


def info(username, password):
    """
    系统登录后的用户信息
    :param username:
    :param password:
    :return:
    """
    with open('login.md', 'r') as f:
        for line in f:
            list = line.split('|')
    r = login(username, password)
    if r:
        print('恭喜{0}进入到系统'.format(list[0]))
    else:
        print('很遗憾，输入的账号或密码错误')


def exit():
    '''用户退出系统'''
    import sys
    sys.exit()


def main():
    '''
    主函数
    :return:
    '''
    while True:
        t = int(input('1.注册， 2. 登录， 3.退出\n'))
        if t == 1:
            username = typeusername()
            password = typepassword()
            register(username, password)
        elif t == 2:
            username = typeusername()
            password = typepassword()
            login(username, password)
            info(username, password)
        elif t == 3:
            print('恭喜您成功退出系统！')
            exit()
        else:
            print('输入错误请重新输入')


if __name__ == '__main__':
    main()
