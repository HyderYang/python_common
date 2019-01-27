#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 在代码中使用 while 循环来迭代处理数据 因为它需要调用某个函数
# 或者和一般迭代模式不同的测试条件

# 常见的 IO 操作程序可能像下面这样

CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        # process_data(data)

# 这种代码可以是用哪个 iter()代替


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process_data(data)


# 测试一下

import sys
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)


# iter 函数 鲜为人知的特性是它接受一个可选的 callable对象和
# 一个标记值作为输入参数
# 当以这种方式使用的时候 它会创建一个迭代器
# 这个迭代器会不断调用 callable 对象直到返回值和标记值相等

# 这种特殊方法对于一些特定会被重复调用函数很有效果
# 比如 IO 调用函数
# 从套接字或者文件中数据块的方式读取数据 通常
# 要不断重复执行 read()或者recv()
# 这里只需要使用一个简单iter调用就可以将两者结合起来


