#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
包含N个元素的元组或者序列 分解为N个单独变量
"""

p = (4, 5)
x, y = p
print(x, y)

data = ['ABC', 23, 23.3, (222, 333, 444)]
name, share, price, new_data = data
print(name)
print(share)
print(price)
print(new_data)

"""
不仅仅元组或者列表 只要是可迭代对象 就可以分解
"""
s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)