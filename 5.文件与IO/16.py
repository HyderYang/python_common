#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 在不关闭一个已经打开文件前提下增加或改变它的unicode编码

# 给一个二进制模式打开文件添加 unicode 编码解码 可以使用 io.TextIOWrapper
# 包装他
import io
import urllib.request

u = urllib.request.urlopen('http://www.baidu.com')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

# 如果想修改一个已经打开的文本模式的文件编码方式 可以先使用 detach() 方法移除掉
# 已存在的文本编码层 并使用新编码方式代替

import sys

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)

# IO系统由一些列的层次构建而成 可以试着运行下面的例子
f = open('somefile.txt', 'w')
print(f)
print(f.buffer)
print(f.buffer.raw)

# 上面这个例子 io.TextIOWraper 是一个编码和解码unicode文本处理
# io.bufferedwriter 是一个处理二进制数据的带缓冲IO层 io.FileIO是一个表示操作系统
# 底层文件描述符的原始文件 增加或改变文本编码会涉及增加或改变最上面的 io.TextIOWrapper

# 一般来讲 上面例子这样通过访问属性值来直接操作不同的层很不安全

print(f)
f = io.TextIOWrapper(f.buffer, encoding='latin-1')
print(f)

f.write('Hello')

# 出错了 因为 f 的原始值已经被破坏了并关闭的底层文件

# detach 方法会断开文件的最顶层并返回第二层 之后顶层就什么都没了
f = open('somefile.txt', 'w')
print(f)

b = f.detach()
print(b)

f.write('hello')
# 一旦断开最顶层 就可以给返回结果添加一个新的最顶层

f = io.TextIOWrapper(b, encoding='latin-1')
print(f)

# 另外 还有一种技术可变文件处理, 错误机制,

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                            errors='xmlcharrefreplace')
print('Jalape\u00f1o')







