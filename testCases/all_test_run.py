#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/26/2020 15:58 
# @Author : Julia
# @Version：V 0.1
# @File : all_test_run.py
# @desc :

import unittest
import os


def allTests():
    start_dir = os.path.dirname(__file__)

    suite = unittest.TestLoader().discover(start_dir=start_dir,
                                         pattern='test_*.py',
                                         top_level_dir=None)
    return suite

def run():
    unittest.TextTestRunner(verbosity=2).run(allTests())

if __name__ == '__main__':
    run()