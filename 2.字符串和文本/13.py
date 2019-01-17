#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 通过某种对齐方式格式化字符串

# 对于基本的字符串对齐操作 可以使用 ljust rjust center
text = 'hello world'
print(text.ljust(20))
print(text.rjust(20))

print(text.center(20))

print('#' * 50)

print(text.rjust(20, '='))
print(text.rjust(20, '*'))

print('#' * 50)

# 函数format也可以对齐字符串

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print('#' * 50)

print(format(text, '=>20s'))
print(format(text, '*^20s'))

print('#' * 50)

# 格式化多个值的时候 这些格式化代码也可以用在 format()方法中

print('{:>10s} {:>10s}'.format('hello', 'world'))


