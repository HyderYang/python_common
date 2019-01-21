#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 创建或测试正无穷负无穷或者NaN的浮点数

# Python并没有特殊的语法来标识这些特殊的浮点数 但是可以使用float来创建
import math

a = float('inf')
b = float('-inf')
c = float('nan')

print(a)
print(b)
print(c)

# 为了测试这些值存在 使用 math.isinf() 和 math.isnan() 函数
print(math.isinf(a))
print(math.isnan(c))

print('#' * 50)

# 有些地方需要特别注意 特别是跟比较操作符相关的时候

a = float('inf')

print(a + 54)
print(a * 10)
print(10 / a)

print('#' * 50)

# NaN值会在所有操作中传播 而不会产生异常
print(c + 23)
print(c / 2)
print(c * 23)
print(math.sqrt(c))

# NaN值的一个特别的地方是他们之间比较操作总返回 False
print('#' * 50)
d = float('nan')

print(c == d)
print(c is d)

# 测试一个NaN的值唯一安全的方法是 math.isnan()




