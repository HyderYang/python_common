#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 对浮点数进行精确计算 并不希望存在小误差

# 浮点数普遍问题是他们不能精确的表示十进制数 并且 简单的数学运算也会产生误差

a = 4.2
b = 2.1

print(a+b)

print(a+b == 6.3)

print('#' * 50)

# python底层问题 CPU和IEEE 754标准

# 如果需要精确点 并且容忍性能损耗 可以使用 decimal 模块

from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print(a + b)
print(a + b == Decimal('6.3'))

# 上面代码有点奇怪 比如用字符串表示数字
# 但是 Decimal 对象会像普通浮点数一样工作 (支持所有常用数学运算)

print('#' * 50)

# Decimal 模块主要特征是允许你控制计算的每一方面 包括数字位数和四舍五入运算
# 为了这样做 需要先创建一个本地上下文并更改它的设置

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)


print('#' * 50)

# 如果你在做科学计算或者工程领域计算 电脑绘图 或者科学领域大多数运算
# 那么使用普通浮点类型是普遍做法
# 在真实世界中很少会要求精确到浮点数能提供的 17 位精度
# 而且 原生浮点计算要快的多



