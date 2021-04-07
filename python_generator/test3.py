#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 3/17/2021 16:55 
# @Author : Julia
# @Version：V 0.1
# @File : test3.py
# @desc :

import sys
import types
import time


class YieldManager(object):
    def __init__(self, tick_delta=0.01):
        self.generator_dict = {}

    def tick(self):
        cur = time.time()
        # print(self.generator_dict)
        for gene, t in self.generator_dict.items():
            if cur >= t:
                self._do_resume_generator(gene, cur)

    def _do_resume_generator(self, gene, cur):
        try:
            self.on_generator_execute(gene, cur)
        except StopIteration as e:
            self.remove_generator(gene)
        except Exception as e:
            print('unexpected error', type(e))
            self.remove_generator(gene)

    def add_generator(self, gen, deadline):
        self.generator_dict[gen] = deadline

    def remove_generator(self, gene):
        del self.generator_dict[gene]

    def on_generator_execute(self, gen, cur_time=None):
        t = gen.__next__()
        cur_time = cur_time or time.time()
        self.add_generator(gen, t + cur_time)


g_yield_mrg = YieldManager()


def yield_dec(func):
    def _inner_func(*args, **kwargs):
        gen = func(*args, **kwargs)
        if isinstance(gen,types.GeneratorType):
            g_yield_mrg.on_generator_execute(gen)
        return gen

    return _inner_func


@yield_dec
def do(a):
    print('do', a)
    yield 2.5
    print('post_do', a)
    yield 6
    print('post_do again', a)
    yield 10
    print('post_do again again', a)


if __name__ == '__main__':
    do(2)
    for i in range(1, 40):
        print('simulator a time, %s senconds passed' % i)
        time.sleep(1)
        g_yield_mrg.tick()
