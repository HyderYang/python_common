#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 将数字格式化输出 并控制数字位数 对齐 千位分割

# 格式化单个数字的时候 使用内置 format函数

x = 1234.56789

print(format(x, '0.2f'))

print(format(x, ','))

print(format(x, '0,.1f'))

print('#' * 50)

# 指数计数法

print(format(x, 'e'))
print(format(x, '0.2E'))

print('#' * 50)

# 数字格式化输出通常比较简单 上面演示的同时适用于浮点数和 decimal对象
# 当指定数字位数后 结果会根据 round() 函数同样的规则进行四舍五入

print(x)
print(format(x, '0.1f'))
print(format(-x, '0.1f'))


