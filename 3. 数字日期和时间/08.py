#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 分数计算
# 使用 fractions 模块
from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)

print(a + b)

print(a * b)

c = a * b
print(c.numerator)
print(c.denominator)

print(float(c))

x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)


