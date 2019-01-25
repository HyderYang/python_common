#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 在迭代一个序列的同时 跟踪正在被处理的元素索引

# 内置的 enumerate() 函数可以解决这个问题
from collections import defaultdict

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

print('#' * 50)

# 为了按行号输出 (行号从1开始) 可以传递一个开始参数

for idx, val in enumerate(my_list, 1):
    print(idx, val)

print('#' * 50)

# enumerate 跟踪某些值在列表出现的位置非常有用
# 如果你想讲一个文件中出现的单次映射到出现的行号上 可以利用 enumerate

word_summary = defaultdict(list)

with open('test.txt') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)
# 如果你处理完文件后打印 word_summary 会发现它是一个字典
# 对于每个单次有一个key 每个key 对应的值是一个由这个单次出现的行号组成的列表
# 如果某个单次在一行中出现过两次 那么这个行号也会出现两次 同时也可以作为文本的简单统计

print('#' * 50)

# 定义一个计数变量的时候 使用 enumerate 函数会更加简单
# enumerate 函数返回的是一个 enumerate 对象实例 它是一个迭代器
# 返回连续的包含一个计数和值得元祖 元祖中值通过在传入序列上调用 next() 返回
