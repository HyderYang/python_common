#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
从可迭代对象中分解出N个元素
"""
from audioop import avg

record = ('dave', '111@qq.com', 1233, 4432)

name, email, *number = record
print(number)


def drop_first_last(grades):
    """
    掐头去尾 中间数取平均值
    """
    first, *middle, last = grades
    return avg(middle)


print('*' * 50)


record = [
    ('foo1', 1, 2),
    ('foo2', 3, 4),
    ('foo3', 5, 6)
]

for tag, *num in record:
    print(num)


print('*' * 50)

# 拆分字符串
line = 'nobody:*:2:-2:Unprivileged User:/var/empty:/user/bin/false'
uname, *field, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

print('*' * 50)


# 递归求和
items = [i for i in range(100)]
print(items)


def sum_list(items):
    head, *tail = items
    return head + sum_list(tail) if tail else head


print(sum_list(items))

