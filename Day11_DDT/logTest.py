#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/26/2021 15:53 
# @Author : Julia
# @Version：V 0.1
# @File : logTest.py
# @desc :

import logging

def log(log_conent):
    logFile = logging.FileHandler('log.md','a',encoding='utf-8')
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
    logFile.setFormatter(fmt)
    logger1=logging.Logger('logTest1name',level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_conent)

log('你好2')