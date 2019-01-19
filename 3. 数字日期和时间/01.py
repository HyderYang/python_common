#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 对浮点数执行指定精度的舍入运算

# 对于简单的舍入运算 使用内置的 round(value, ndigits) 函数即可

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.23, 1))
print(round(1.23324, 3))
print(round(1.15, 1))
print(round(2.25, 1))

# 当一个值刚好在两个便捷的中间的时候 round 函数返回离他最近的 偶数
# 也就是说 1.5 或者 2.5 舍入都会得到2

print('#' * 50)

# 传给 round() 函数的 ndigits 参数可以是负数
# 这种情况下 舍入运算会作用在 十位, 百位, 千位等上面

a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

print('#' * 50)

# 不要将舍入和格式化输出搞混淆 如果你的目的 只是简单的输出一定宽度的数
# 你不需要使用使用 round 而仅仅只需要在格式化的时候指定精度即可

x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))

print('value is {:0.3f}'.format(x))

print('#' * 50)

# 不要试着去舍入浮点值来修正表面上看起来正确的问题

b = 2.1
a = 4.2
c = a+b
print(c)

c = round(c, 2)
print(c)

# 如果需要金融领域的精度 需要使用 decimal 模块





