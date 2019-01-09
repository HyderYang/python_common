#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
将键映射到多个值的字典
"""
from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['a']
d['b'] = 4

print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)

print('*' * 50)

# 初始化一键多值
# 普通写法

d = {}
pairs = dict(
    a=[1, 2, 3],
    b=[5, 6, 7]
)
for key, value in pairs.items():
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)

# 较好写法
d = defaultdict(list)
for key, value in pairs.items():
    d[key].append(value)

print(dict(d))
