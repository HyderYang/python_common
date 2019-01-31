#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 测试一个文件或者目录是否存在

# 使用 os.path 模块测试文件或者目录是否存在
import os

print(os.path.exists('/etc/passwd'))

print(os.path.exists('/tmp/spam'))

print('#' * 50)
# 还可以进一步测试文件是什么类型的

print(os.path.isfile('/etc/passwd'))    # 是否文件
print(os.path.isdir('/etc/passwd'))     # 是否目录
print(os.path.islink('/etc/passwd'))    # 是否连接
print(os.path.realpath('/etc/passwd'))    # 是否真实链接(硬链接?)

print('#' * 50)

# 还可以获取元数据 比如文件大小或者修改日期 也可以使用 os.path模块 解决

print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))

import time
time.ctime(os.path.getmtime('/etc/passwd'))


# 使用 os.path 进行文件测试非常简单 在写脚本时候 可能唯一需要注意的是文件权限问题
# 特别是获取元数据时候
