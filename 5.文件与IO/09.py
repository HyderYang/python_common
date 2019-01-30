#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 直接读取二进制数据到一个可变缓冲区中 而不需要做忍耐和中间
# 复制操作 或者你想原地修改数据并将它写回一个文件中

# 读取数据到一个可变数组中你那个 使用文件对象的 readinto方法

import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# 使用方法

with open('sample.bin', 'wb') as f:
    f.write(b'hello world')

buf = read_into_buffer('sample.bin')
print(buf)

buf[0:5] = b'hello'
print(buf)

with open('newsample.bin', 'wb') as f:
    f.write(buf)

print('#' * 50)

# 文件对象的 readinto 方法能被用来预先分配内存的数组填充数据
# 甚至包括由 array 模块或者 numpy 库创建你的数组 和普通的 read 方法不同
# readinto() 填充已存在的缓冲区而不是为新对象重新分配内存再返回他们
# 因此 可以使用它来避免大量内存分配操作
# 比如 你读取一个由相同大小的记录组成的二进制文件时候 可以写成下面这样

record_size = 32

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break

# 另外 还有一个特性就是 memoryview 它可以通过零复制的方法对已经存在缓冲区
# 执行切片操作 甚至还能修改它内容

print(buf)

m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)

m2[:] = b'WORLD'
print(buf)

# 使用 f.readinto 需要注意 必须检查它的返回值 也就是实际读取的字节数
# 如果字节数小于缓冲区大小 表明数据被截断或者破坏
# 最后 观察其他函数库和模块中 into 相关的函数 如 recv_into pack_into等

# python很多其他部分已经支持直接IO访问 这些操作用来填充或修改数组和缓冲区内容










