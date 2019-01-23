#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 使用复数空间或者使用复数来执行计算操作
# 复数可以使用函数 complex(real. imag)

a = complex(2, 4)
b = 3 - 5
print(a)
print(b)

print('#' * 50)

print(a.real)
print(a.imag)
print(a.conjugate())

print('#' * 50)

# 常见的数学运算都可以工作

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

print('#' * 50)

# 如果执行其他的复数函数 如 正弦 余弦或者平方根 使用 cmath 模块

import cmath
cmath.sin(a)
cmath.cos(a)
cmath.exp(a)

print('#' * 50)

# python 中大部分数学相关的模块都能处理复数 比如 numpy

# python标准数学函数并不能产生复数值 因此
# 你的代码中不可能会出现复数返回值
# 如果需要生成一个复数返回结果 你必须显示使用 cmath模块

print(cmath.sqrt(-1))


