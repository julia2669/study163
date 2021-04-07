#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 3/17/2021 15:37 
# @Author : Julia
# @Version：V 0.1
# @File : test2.py
# @desc :

def gen_data_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield line


def gen_words(lines):
    for word in (w for w in lines.split() if w.strip()):
        yield word


def cont_words(file_name):
    word_map = {}
    for line in gen_data_from_file(file_name):
        for word in gen_words(line):
            if word not in word_map:
                word_map[word] = 0
            word_map[word] += 1
    return word_map


def count_total_chars(file_name):
    total = 0
    for line in gen_data_from_file(file_name):
        total += len(line)
    return total


if __name__ == '__main__':
    filename = r'C:\Users\julizhou\PycharmProjects\bagspider\shenyihuanghou\books\第46章 可怜的楚天河.txt'
    print(cont_words(filename), count_total_chars(filename))
