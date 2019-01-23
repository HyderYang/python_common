#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 使用生成器创建新的迭代模式

# 实现自定义迭代模式 跟内置函数 range() reversed不一样

# 实现自定义迭代模式 使用生成器定义它


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

# 可以用 for 循环迭代它 或者使用其他可迭代对象函数
# sum list 等


for n in frange(0, 4, 0.5):
    print(n)

print('#' * 50)

print(list(frange(0, 1, 0.125)))

print('#' * 50)
# 一个函数中需要一个 yield 语句即可将其转为 生成器
# 跟普通函数不同 生成器只能用于迭代操作


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


c = countdown(3)
print(c)

print(next(c))
print(next(c))
print(next(c))
print(next(c))

# 一个生成器主要特征是它只会回应在迭代中使用 next 操作
# 一旦生成器函数返回退出 迭代终止
# 迭代中常使用for语句自动处理这些细节
