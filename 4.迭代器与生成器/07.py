#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 由迭代器生成的切片 但是标准切片操作并不能做到

# 函数 itertools.islice() 适合在迭代器和生成器上做切片操作


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# print(c[10:20])


import itertools


for x in itertools.islice(c, 10, 20):
    print(x)


# 迭代器和生成器不能使用标准的切片操作
# 因为他们长度并不知道 也没有实现索引位置的所有元素
# 函数 islice() 返回一个可以生成指定元素的迭代器
# 他通过遍历并丢弃知道切片开始索引位置所有元素 然后才开始一个个
# 返回元素 直到切片结束索引位置

# 需要强调的是 islice 会消耗掉 传入的迭代器中数据
# 必须考虑到迭代器是不可逆的 如果需要再次访问这个迭代器
# 那么 先将他里面的数据放入一个列表中



