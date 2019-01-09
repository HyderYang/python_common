#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
找出最大最小的与元素
"""
import heapq

nums = [1, 8, 4, 23, -3, 56, 77, 3]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(2, nums))

print('*' * 50)

# 复杂对象排序比较
profiles = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAP', 'shares': 50, 'price': 543.1},
    {'name': 'BBA', 'shares': 202, 'price': 23.1},
    {'name': 'HFQ', 'shares': 35, 'price': 14.1},
    {'name': 'YHO', 'shares': 67, 'price': 31.1},
    {'name': 'ACME', 'shares': 98, 'price': 115.1},
]

cheap = heapq.nsmallest(3, profiles, key=lambda s: s['price'])
expensive = heapq.nlargest(3, profiles, key=lambda s: s['price'])

print(cheap)
print(expensive)
