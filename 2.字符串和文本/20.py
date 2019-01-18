#!/usr/bin/env python
# -*- encoding: utf-8 -*-

data = b'hello world'

print(data[0:5])

print(data.startswith(b'hello'))

print(data.split())

print(data.replace(b'Hello', b'hello cruel'))

print('#' * 50)

# 这些操作同样也适用于字节数组

data = bytearray(b'hello world')
print(data[0:5])

print(data.startswith(b'hello'))

print(data.split())

print(data.replace(b'hello', b'hello cruel'))

print('#' * 50)

# 大多数情况下 在文本字符串上的操作均可用于字节字符串
# 然而 这里也是需要注意不同点
# 字节字符串的索引操作返回整数而不是单独字符

a = 'hello world'

print(a[0])

b = b'hello world'
print(b[0])
print(b[1])

print('#' * 50)
# 第二点 字节字符串不会提供一个美观的字符串表示 除非它们被解码
# 成为一个文本字符串

s = b'hello world'
print(s)

print(s.decode('ascii'))

# 类似 也不存在任何使用于字节字符串的格式化操作

# 如果你想格式化字节字符串 需要先使用标准的文本字符串
# 然后将其编码为字节字符串







