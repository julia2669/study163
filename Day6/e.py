#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/13/2020 15:06 
# @Author : Julia
# @Version：V 0.1
# @File : e.py
# @desc :

import sys


def main(input):
    stack_number = []
    task = set()
    count = 0
    for line in input:
        if "_".join([str(s) for s in line]) in task:
            continue
        else:
            task.add("_".join([str(s) for s in line]))


        print("---")
        print(line,count)
        print("---")
        print(task)
        for item in line:
            stack_number.append(item)
        print(stack_number)
        if len(stack_number) > 3:
            if stack_number[-2] == stack_number[-3]:
                count +=1
    return count + 1
input = eval(sys.stdin.readline())
output = main(input)
print(output)