#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 内存映射一个二进制文件到一个可变字节数组中 为了随机访问他的内容或在原地做些修改

# 使用mmap模块来内存映射文件 下面是一个工具函数 向你演示了如何打开一个文件
# 并以一种便捷方式内存映射这个文件

import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# 为了使用这个函数 需要有一个已创建并且内容不为空的文件
# 下面代码是初始创建一个文件并将其内容扩充到指定大小

size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# 下面呢是一个利用 memory_map() 函数类内存映射文件内容的例子

m = memory_map('data')
len(m)

print(m[0:10])
print(m[0])

# Reassign a slice
m[0:11] = b'Hello World'
m.close()

with open('data', 'rb') as f:
    print(f.read(11))

# mmap 返回的 mmap 对象同样可以作为一个上下文管理器来使用
# 这时候 底层文件会自动关闭

with memory_map('data') as m:
    print(len(m))
    print(m[0:10])

print(m.closed)

# 默认情况下 memory_map() 函数打开的文件同时支持读写操作 任何修改内容都会复制回原来
# 的文件中 如果需要只读访问模式 可以给参数 access赋值为 mmap.ACCESS_READ

# m = memory_map(filename, mmap.ACCESS_READ)
# 如果想在本地修改数据 但是 又不想将修改写回到原始文件中 可以使用 mmap.access_copy

# m = memory_map(filename, mmap.ACCESS_COPY)


# 为了随机访问文件内容 使用 mmap 将文件映射到内存中是一个高效和优雅的方法
# 无须打开一个文件并执行大量 seek read write 调用 只需要简单的映射文件并使用
# 切片访问数据即可
