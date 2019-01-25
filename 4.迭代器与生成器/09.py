#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 迭代遍历一个集合中元素的所有可能排列或者组合

# itertools 模块提供了三个函数 其中一个是 itertools.permutations()
# 它接受一个集合并产生一个元祖序列 每个元祖由集合中所有元素的一个可能排列组成
# 也就是说 通过打乱集合中元素排列顺序生产一个元祖
from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

print('#' * 50)

# 如果想得到指定长度所有排列 可以传递一个可选长度参数:

for p in permutations(items, 2):
    print(p)

print('#' * 50)

# 使用 itertools.combinations()可得到输入集合中元素所有组合:

for c in combinations(items, 3):
    print(c)

print('#' * 50)

for c in combinations(items, 2):
    print(c)

print('#' * 50)

for c in combinations(items, 1):
    print(c)

# 对于 combinations 来说 元素顺序已经不重要了
# 也就是说  组合 (a, b) 跟 (b, a) 其实是一样的

print('#' * 50)

# 在计算组合的时候 一旦元素被选取就会从后选中剔除
# 而 函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次

for c in combinations_with_replacement(items, 3):
    print(c)
