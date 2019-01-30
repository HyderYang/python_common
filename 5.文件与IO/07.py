#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 读写一个 gzip 或者 bz2 格式的压缩文件

# gzip 和 bz2 模块可以很容易处理这些文件
# 两个模块都为 open 函数提供了另外的实现来解决这个问题

import gzip, bz2

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()


with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# 类似的 为了写入压缩数据 需要这样做
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# 所有的IO操作都使用文本模式并执行 unicode的编码解码
# 类似的 如果你想操作二进制数据 使用 rb 或者 wb 文件
# 模式即可

print('#' * 50)

# 大部分情况下 读写压缩数据都是非常简单的 但是要注意选择
# 一个正确的文件模式是非常重要的
# 如果你不指定模式 那么 默认的就是二进制模式 如果这时候想要
# 接受文本数据 那么就会出错
# gzip.open 和 bz2.open 接受跟内置的 open() 函数
# 一样的参数 包括 encoding errors newline 等等

# 写入压缩数据时候 可以使用 compresslevel 这个可选
# 关键字参数指定一个压缩级别

with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# 默认等级是9 也就是最高压缩等级 压缩等级越低 性能越好 压缩程度越低

# 最后一点 gzip.open 和 bz2.open 还有一个特性
# 他们可以作用在一个已经存在并以二进制模式打开的文件上

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

# 这样 就允许 gzip bz2 模块工作在许多类文件对象上
# 比如套接字 管道和内存中文件等



