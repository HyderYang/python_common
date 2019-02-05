#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 执行时创建一个临时文件或者目录 并希望使用完之后可以自动销毁

# tempfile 模块中有很多的函数可以完成这个任务 为了创建
# 一个匿名临时文件 可以使用 tempfile.temporaryfile

from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory

with TemporaryFile('w+t') as f:
    f.write('hello world\n')
    f.write('Testing\n')

    f.seek(0)
    data = f.read()

# 或者 这样使用
f = TemporaryFile('w+t')
pass
f.close()

# Temporary 第一个参数是文件模式 通常来讲文本模式 使用
# w+t 二进制模式使用 w+b 这个模式同时支持读写 因为当你关闭
# 文件去改变模式的时候 文件实际上已经不存在了 TemporaryFile
# 同样支持内置 open 函数一样的参数

with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
    pass

# 在大多数 UNIX 系统上 通过 TemporaryFile 创建的文件都是匿名的 甚至连目录都没有
# 如果你想打破这个限制 可以使用 NamedTemporaryFile() 来代替

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

# 为了创建一个临时目录 可以使用 tempfile.TemporaryDirectory()

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

# 已上三个函数 应该是处理临时文件目录最简单的方式了 因为他们会自动处理所有创建
# 清理步骤 在一个更低级别 可以使用 mkstemp 和 mkdtemp 来创建文件和目录

import tempfile

print(tempfile.mkstemp())
print(tempfile.mkdtemp())

# 但是 这些函数并不会进一步管理 如 mkstemp 仅仅返回一个原始的os文件描述符
# 你需要自己将它转为一个真正的文件对象 同时还需要自己清理这些文件

# 通常来讲 临时文件在系统默认的位置被创建你 如 /vat/tmp 等等 为了获取真实位置
# 可以使用 tempfile.gettempdir() 函数

print(tempfile.gettempdir())

# 所有和临时文件相关的函数都允许你通过使用关键字参数 prefix suffix, dir 来定义
# 目录以及命名规则
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')

print(f.name)

# 要注意 尽量使用安全方式使用 tempfile 模块创建临时文件 包括仅给当前用户授权访问
# 以及在文件创建过程中采取措施避免竞态条件 要注意不同的平台可能不一样
