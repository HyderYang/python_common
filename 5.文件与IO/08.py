#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 想在一个固定长度记录或者数据块的集合上迭代 而不是在一个文件中一行一行迭代

# 使用 iter 和 functools.partial()

from functools import partial

RECORD_SIZE = 32

with open('somefile.data', 'rb') as f:
    record = iter(partial(f.read, RECORD_SIZE), b'')
    for r in record:
        pass

# 这个例子中你那个 records 对象是一个可迭代对象 它会不断产生固定大小的数据块
# 知道文件末尾 要注意的是 如果总记录大小不是块大小的整数倍 最后一个返回元素的字节会比
# 期望值少

# iter() 函数有个特性就是 如果传递一个可调用对象和一个标记值 它会创建一个迭代器
# 这个迭代器会一直调用传入的可调用对象直到它返回标记值为止 这时候迭代终止

# 上面的例子中 functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的
# 可调用对象 标记值 b'' 就是当到达文件结尾的时候返回值

# 上面的例子用二进制模式打开 如果是读取固定大小记录 通常是最普遍的情况
# 对于文本文件 一行一行的读取 更普遍点
