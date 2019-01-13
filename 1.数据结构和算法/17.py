#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 从字典中提取子集
# 构造一个字典 它是另一个字典的子集

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print(prices)

p1 = {key: value for key, value in prices.items() if value > 200}

print(p1)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}

p2 = {key: value for key, value in prices.items() if key in tech_names}

print(p2)

print('*' * 50)

# 通常 字典推导式能做到的 通过创建一个元祖然后传给dict函数也能做到

p3 = dict((key, value) for key, value in prices.items() if value > 200)

# 但是 这种方法效率低 且不如字典推导式易读
