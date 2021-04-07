#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/20/2020 14:26 
# @Author : Julia
# @Version：V 0.1
# @File : f10.py
# @desc :


'''
继承顺序的区别:
主要是在多重继承时才会遇到这个问题。

经典类的继承是深度优先，即从下往上搜索；新式类的继承顺序是采用C3算法（非广度优先）。
新式类的继承顺序并非是广度优先，而是C3算法，只是在部分情况下，C3算法的结果恰巧与广度优先的结果相同。
对新式类的继承搜索顺序进行代码验证，新式类中，可以使用mro函数来查看类的搜索顺序(这也算是一个区别)，
如SubNewStyleClass.mro()。

'''

'''
https://www.cnblogs.com/blackmatrix/p/5594109.html
python 3 之后类即类型 类型即类
isinstance(object, type)==True
isinstance(type, object)==True
'''


"""---------------"""
"""
class ClassicClassA():
    var = 'Classic Class A'


class ClassicClassB(ClassicClassA):
    pass


class ClassicClassC():
    var = 'Classic Class C'


class SubClassicClass(ClassicClassB, ClassicClassC):
    pass


if __name__ == '__main__':
    print(SubClassicClass.mro())
    print(SubClassicClass.var)
"""


"""--------------------"""

"""
class A():pass
class B():pass

a = A()
b = B()

if __name__ == '__main__':
    print(type(a))
    print(type(b))
    print(type(a) == type(b))
    print(a.__class__)
    print(b.__class__)
    print(a.__class__ == b.__class__)

"""


class D:
    pass
class E:
    pass
class F:
    pass
class B(D,E):
    pass
class C(E,F):
    pass
class A(B,C):
    pass

print("从A开始查找：")
for s in A.__mro__:
	print(s)

print("从B开始查找：")
for s in B.__mro__:
	print(s)

print("从C开始查找：")
for s in C.__mro__:
	print(s)