#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 使用 print输出数据 但是想改变默认的分隔符或者行尾符

print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

print('#' * 50)

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')

print('#' * 50)

# 使用非空格分隔符输出数据时候 也可以使用 str.join()

print(','.join(('ACME', '50', '91.5')))

# 但是 join 问题在于仅仅适用于字符串你
# 你需要执行另外一些转换才能正常工作
