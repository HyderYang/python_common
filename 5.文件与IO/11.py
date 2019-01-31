#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 需要使用路径名来获取文件名 目录名 绝对路径等等

# 使用 os.path 模块中的函数来操作路径名

import os
path = "/Users/hyder/Work_Beach/Python/python_common/data.csv"

# 文件名
print(os.path.basename(path))

# 目录地址
print(os.path.dirname(path))

# 添加目录路径
print(os.path.join('tmp', 'data', os.path.basename(path)))

# 补全绝对路径
path = '~/Work_Beach/Python/python_common'
print(os.path.expanduser(path))

# 分割文件后缀
print(os.path.splitext(path))

# 对于任何文件名操作 你都应该使用 os.path 模块 而不是使用标准字符串操作
# 构造自己的代码 特别是为了可移植性考虑的时候更应该如此
# 因为 os.path 模块知道 UNIX 和 windows 系统之间差异并且能够可靠的处理类似
# data/data.csv 和 data\data.csv 这样的文件名
# 要注意的是 os.path 还有更多功能并没有列举出来 可以查阅官方文档来获取更多内容
