#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 序列中值是可哈希的 那么可以通过集合和生成器解决
# 可哈希对象 在生命周期中是不可变的 它有一个 __hash__()方法
# 整数 浮点 字符串 元祖都是不可变的


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 34, 7, 1, 2, 2, 25, 34]

for i in dedupe(a):
    print(i)

print('*' * 50)

# 以上是序列元素是可哈希对象 如果不是可哈希对象去除重复项 则需要修改


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [
    dict(
        x=1,
        y=2,
    ),
    dict(
        x=1,
        y=3,
    ),
    dict(
        x=1,
        y=2,
    ),
    dict(
        x=2,
        y=4,
    ),
]

print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))

print('*' * 50)

print(list(dedupe(a, key=lambda d: d['x'])))







