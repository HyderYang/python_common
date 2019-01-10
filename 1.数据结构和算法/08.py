#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
字典有关的计算问题
"""

prices = dict(
    AXM=23.43,
    LPM=45.43,
    AAM=32.43,
    FDM=67.43,
    MAW=12.43
)

min_price = min(zip(prices.values(), prices.keys()))

print(min_price)

print('*' * 50)

prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(prices_sorted)

print('*' * 50)

# 注意  zip 函数创建了一个迭代器 内容只能使用一次

# 对于 min max 函数 可以使用第二形参 key 来获取字典的最大最小key值

min_key = min(prices, key=lambda k: prices[k])
max_key = max(prices, key=lambda k: prices[k])

print(min_key)
print(max_key)

print('*' * 50)

# 但是 只能获取key/value 其中一个值

# 通过zip函数 将键值对翻转 因为元祖上进行比较操作 值会先进行比较 然后才是键

# 但需要注意的是 如果value值相等 那么就会以key值作为判定结果进行排序

