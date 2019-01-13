#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 需要在数据列上执行聚合函数但要先转换或者过滤数据

# 结合数据计算与转换使用一个生成表达式

nums = [1, 2, 3, 4, 5, 6]
s = sum(x * x for x in nums)

print(s)

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))


portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

print(min_shares)

print('*' * 50)

# 使用一个生成器表达式作为参数会比先创建一个临时变量更加优雅
# 尽管一个临时变量可以达到相同效果 但会多一个步骤
# 数据量小的时候还没有问题 数据量大了 生成器方案会更节省内存呢


