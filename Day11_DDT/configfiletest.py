#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/18/2021 10:34 
# @Author : Julia
# @Version：V 0.1
# @File : configfiletest.py
# @desc :

'''
 1. The only bit of magic involves the DEFAULT section which provides default values for all other sections
 2. Note also that keys in sections are case-insensitive and stored in lowercase
 3. Config parsers do not guess datatypes of values in configuration files, always storing them internally as strings
 4. config parsers also provide getboolean(). This method is case-insensitive and recognizes Boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0' 1
 5. default values have precedence over fallback values

'''


import configparser

def creat_sample():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45',
                            'Compression': 'yes',
                            'CompressionLevel': '9'}
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'     # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'
    with open('example.ini', 'w') as configfile:
        config.write(configfile)

def read_sample():
    config = configparser.ConfigParser()
    config.read('example.ini')
    config.sections()
    print(config.sections())
    print(config['DEFAULT']['Compression'])
    print(config['bitbucket.org']['Compression'])
    print(config['bitbucket.org']['PASSword'])
    topsecret = config['topsecret.server.com']
    print(topsecret['forwardx11'])
    print(topsecret.getboolean('forwardx11'),config['bitbucket.org'].getboolean('forwardx11'))
#     default values have precedence over fallback values
    print(topsecret.get('CompressionLevel', '3')) #will return default value 9
    print(config['Paths']['my_pictures'])
    print(config['Escape']['gain'])
    print(config['Escape2']['cost'])


read_sample()