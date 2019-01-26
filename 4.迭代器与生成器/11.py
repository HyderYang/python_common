#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 同时迭代多个序列就每次分别从一个序列中取出一个元素

# 同时迭代多个序列 使用 zip 函数
from itertools import zip_longest

xpts = [1, 5, 6, 7, 8, 10]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

print('#' * 50)

# zip(a, b) 会生成一个可返回元祖 (x, y) 其中 x来自a, y来自b 一旦其中某个序列到底结尾
# 迭代结束 因此迭代长度跟参数中最短序列长度一致

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

print('#' * 50)

# 如果上面的结果不符合需求 还可以使用 itertools.zip_longest()
for i in zip_longest(a, b):
    print(i)

print('#' * 50)

# 默认填充:

for i in zip_longest(a, b, fillvalue=0):
    print(i)

print('#' * 50)

# 当你想对成对处理数据的时候 zip是很有用的
# 比如 头列表和一个值列表
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)

print('#' * 50)
# 也可以这样输出
for name, val in zip(headers, values):
    print(name, '=', val)

print('#' * 50)

# 尽管不常见 但是 zip也可以接受多个序列参数
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

print('#' * 50)

# zip 会创建一个迭代器作为结果返回 如果需要将结对的值存储在列表中 要使用 list()函数
print(zip(a, b))
print(list(zip(a, b)))
