#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 数据序列过滤元素

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 最简单的就是列表推导式

lis = [n for n in mylist if n > 0]
print(lis)

print('*' * 50)

# 列表推导式缺陷在于如果序列很大占用很高内存
# 可以用生成式过滤

pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

print('*' * 50)

# 如果比较复杂 可以使用 filter 函数

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))

print(ivals)

# filter 创建了一个迭代器 如果想得到一个列表的话 需要强转

print('*' * 50)

# 列表推导式和生成器表达式通常是最简单的过滤数据方法 它们还可以过滤的时候转换数据

import math
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
covert = [math.sqrt(n) for n in mylist if n > 0]
print(covert)


print('*' * 50)

# 另一个操作是将不符合条件的值用新值代替

clip = [n if n > 0 else 0 for n in mylist]
print(clip)

print('*' * 50)

# 还有 itertools.compress() 它以一个iterable对象和一个相对应的 布尔 选择器序列作为
# 输入参数 然后输出 iterable 对象中对应选择器为 True 的元素

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
show_compress = list(compress(addresses, more5))
print(show_compress)
