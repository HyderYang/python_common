#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 使用操作类文件对象的程序操作文本或者二进制字符串

# 使用 io.stringio() 或者 io.bytesio 类来创建类
# 文件对象操作字符串数据
import io

s = io.StringIO()
s.write('hello world \n')

print('this is a test', file=s)

s.getvalue()

s = io.StringIO('hello\nworld\n')
s.read(4)

s.read()

print('#' * 50)

# io.StringIO 只能用于文本 如果想操作二进制数据 要使用 io.bytesIO类来代替

s = io.BytesIO()
s.write(b'binary data')
s.getvalue()

# 当想模拟一个普通文件的时候 stringio 和 bytesio 类是很有
# 用的
# 比如 单元测试的时候 可以使用 stringio 来创建一个包含测试
# 数据的类文件对象 这个对象可以被传给某个参数为普通文件对象的函数
# 需要注意的是 stringio 和 bytesio 并没有正确的整数类型
# 文件描述符 因此 他们不能在那些需要使用真实系统文件
# 如 文件 管道 或者 套接字程序中使用
