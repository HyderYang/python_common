#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 字典中寻找相同点 (键值都相等)

a = dict(
    x=1,
    y=2,
    z=3,
)

b = dict(
    w=1,
    y=2,
    z=3,
)

print(a.keys() & b.keys())

print('*' * 50)

print(a.keys() - b.keys())

print('*' * 50)

print(a.items() - b.items())

print('*' * 50)

print(a.items() & b.items())

# 字典的key支持 并集 交集 差集操作
# 字典的 items 返回值也支持 三种操作





