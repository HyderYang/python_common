#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 字符串中插入变量
# 创建一个内嵌变量的字符串 变量被他的值替换掉

# python 并没有对在字符串中简单替换变量提供直接支持
# 但是通过 String的format 方法来解决这个问题

s = '{name} has {n} messages'

print(s.format(name='Guido', n=37))

print('#' * 50)

# 如果要被替换的变量域中找到 那么可以结合使用 format_map()和 vars()

name = 'Guido'
n = 37

print(s.format_map(vars()))

print('#' * 50)

# vars()也适用于对象实例


class Info(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))


print('#' * 50)

# format 和 format_map 一个缺陷是不能很好处理变量缺失的情况
# 可以使用 __missing__()魔术方法


class safesub(dict):

    def __missing__(self, key):
        return '{' + key + '}'

del n

print(s.format_map(safesub(vars())))



