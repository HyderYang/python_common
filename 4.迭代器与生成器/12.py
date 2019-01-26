#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 多个对象中执行相同操作 这些对象在不同容器中 不失可读性避免重复循环
# itertools.chain 方法简化这个任务
# 接受一个可迭代对象列表作为输入 返回一个迭代器 有效屏蔽多个容器中迭代希捷
from itertools import chain

active_items = [1, 2, 3, 4, 5]
inactive_items = ['a', 'b', 'c', 'd']

# 普通版本
for item in active_items:
    print(item)

for item in inactive_items:
    print(item)

print('#' * 50)

# 简化版
for x in chain(active_items, inactive_items):
    print(x)


print('#' * 50)

# itertools.chain()接受一个或者多个可迭代对象作为输入参数 然后创建一个迭代器 依次连续的返回每个
# 可迭代对象中的元素 这种方式比先将序列合并再迭代要高效

# 因为 合并序列会创建一个新的序列 并且要求 两个序列类型一致
# chain 不会有这一步 所以 如果输入序列非常大会很节省内存
# 并且当可迭代对象类型不一样的时候 chain 同样可以很好工作

