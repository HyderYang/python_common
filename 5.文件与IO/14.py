#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 使用原始文件名执行文件IO操作 也就是说文件名并没有经过系统默认编码去解码或编码

# 默认情况下 文件名都会根据 sys.getfilesystemencoding() 返回的文本编码
# 或解码
import sys

print(sys.getfilesystemencoding())

# 如果因为某种原因想忽略这种编码 可以使用原始字节字符串指定一个文件名即可

# Wrte a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')


import os
os.listdir('.')

os.listdir(b'.') # Note: byte string

# Open file with raw filename
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())

# 在最后两个操作中 你给文件相关函数 如 open 和 os.listdir() 传递
# 字节字符串时候 文件名的处理方式会稍有不同

# 通常来讲 你不需要担心文件名的编码和解码 普通文件名操作应该就没有问题
# 但是 有些操作系统允许用户通过偶然或者恶意方式区创建名字不符合默认编码的文件
# 这可能会中断需要处理大量文件的python程序

# 读取目录并通过原始未解码方式处理文件名可以有效的避免这个问题
