#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 读写二进制文件 如音乐 或者 图片

# 使用 rb 或者 wb 的open函数读取写入二进制数据

with open('somefile.bin', 'rb') as f:
    data = f.read()

with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

# 读取二进制数据时 需要指明所有返回的数据都是字节字符串格式
# 而不是文本字符串
# 类似的 在写入数据的时候 必须保证参数是字节形式对外暴露数据对象

print('#' * 50)

# 读取二进制数据的时候 字节字符串和文本字符串语义差异可能会导致
# 一个潜在陷阱 特别需要注意的是 索引和迭代动作返回的是字节而不是
# 字节字符串

t = 'Hello World'
print(t[0])

for c in t:
    print(c)

b = b'Hello World'
print(b[0])
for c in b:
    print(c)

print('#' * 50)

# 如果想从二进制模式中读取或者写入文本数据 必须要进行解码和编码操作

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'hello world'
    f.write(text.encode('utf-8'))

# 二进制 IO 还有一个特性就是 数组和c结构体类型能直接被写入
# 不需要中间转换为自己对象

import array

nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)

# 这个适用于任何实现了 缓冲接口 的对象
# 这个对象会直接暴露其底层的内存缓冲区给能处理它的操作
# 二进制数据写入就是这类操作之一

