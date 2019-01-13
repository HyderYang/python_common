#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 多个字典或者映射 从逻辑上合为一个 并执行某些操作
# 假如需要从两个字典中执行查找操作
# 可以使用 collections.ChainMap
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

print('*' * 50)

# 一个ChainMap 接受多个字典并将它们 逻辑合并
# 注意 ChainMap 并不是真正意义上的合并 它只是在内部创建了一个容纳这些字典的列表
# 并重新定义了一些常见的字典操作

print(len(c))
print(list(c.keys()))
print(list(c.values()))

print('*' * 50)

# 如果出现重复键 那么第一次出现的映射值会被返回 因此
# c['z'] 总是返回 3 而不是返回 b['z'] 的 值 4

c['z'] = 10
c['w'] = 40  # 变量a没有 w 元素 因此会新增

del c['x']

print(a)

# del c['y'] 报错 变量a 没有 y元素

# 使用字典方法 update() 也可以合并两个字典
# 但是 这是一个新的字典对象 而且对新字典最想进行赋值 也不会影响到原单个字典

# 使用 ChainMap 则只是逻辑上合并 对 chainmap 进行赋值 会影响原有的第一个
# 单一字典对象
