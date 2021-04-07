#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/28/2020 15:58 
# @Author : Julia
# @Version：V 0.1
# @File : temp.py
# @desc :

import math
def sieve(size):
    sieve= [True] * size
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(size)) + 1):
        k= i * 2
        while k < size:
           sieve[k] = False
           k += i
    print(sieve)
    return sum(1 for x in sieve if x)

print(sieve(20))