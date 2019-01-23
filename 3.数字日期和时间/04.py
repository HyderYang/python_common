#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 需要转换或者输出使用二进制 八进制 十六进制表示的整数

# 将整数转为 二进制/八进制/十六进制 需要分别使用 bin oct hex 函数

x = 1234

print(bin(x))
print(oct(x))
print(hex(x))

print('#' * 50)
# 另外 不想输出 0b 0o 或者 0x 前缀的话 可以使用format 函数

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

print('#' * 50)

# 整数是有符号的 所以如果你在处理负数的时候输出结果会包含一个负号
x = -1234

print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))

print('#' * 50)

# 为了以不同进制转换整数字符串 简单的使用带有进制的 int 函数即可

print(int('402', 16))
print(int('100011010010', 2))

print('#' * 50)

# 大多数情况下处理 二进制 八进制 十六进制整数是很简单
# 只要记住这些转换属于整数和其对应的文本表示之间的转换即可

# 八进制需要注意一下 八进制前缀是 0o

print(int('0o755', 8))




