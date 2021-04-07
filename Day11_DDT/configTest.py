#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/18/2021 10:03 
# @Author : Julia
# @Version：V 0.1
# @File : configTest.py
# @desc :

import configparser
import os

def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__),filename)

def getLinux():
    config = configparser.ConfigParser()
    cp = config.read(base_dir('config.ini'))
    print(cp)

print(base_dir('config.ini'))