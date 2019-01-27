#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 有一系列排序序列 想将他们合并后得到一个排序序列并在上面迭代遍历

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)

print('#' * 50)

# heapq.merge 可迭代特性意味着它不会马上读取所有序列
# 也说明 可以从非常长的的序列中使用它 而不会有太大开销

with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)

# 有一点 heapq.merge 需要所有输入序列必须是排过序的
# 特别的 他不会预先读取所有数据到堆栈中或者预先排序
# 也不会对输入做任何排序检查 它仅仅是检查所有序列开始部分并
# 返回最小那个 这个过程会持续到所有输入序列中元素便利完
