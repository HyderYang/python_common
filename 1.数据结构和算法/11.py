#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 避免切片硬编码 对切片进行命名
# 内置的 slice() 函数会创建一个切片对象 允许进行切片操作

items = [0, 1, 2, 3, 4, 5, 6, 7]
a = slice(2, 4)

print(items[2:4])

print(items[a])

items[a] = [20, 30]

print(items)

print('*' * 50)

# slice()函数返回的切片对象 可以分别设置他的 起始 结束 步长

a = slice(5, 50, 2)

print(a.start)
print(a.stop)
print(a.step)

print('*' * 50)

# 还可以调用切片对象的 indices(size) 方法
# 这个切片对象会自适应序列边界 不会出现 IndexError

s = 'HelloWorld'
a = slice(5, 50, 2)

print(a.indices(len(s)))

print('*' * 50)

for i in range(*a.indices(len(s))):
    print(s[i])








