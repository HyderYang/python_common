#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 获取系统中某个目录下的所有文件列表

# 使用 os.listdir 函数来获取某个目录中的文件列表

import os

names = os.listdir('/')
print(names)

# 结果会返回目录中所有文件列表 包括所有文件 子目录 符号链接等
# 如果你需要通过某种方式过滤数据 可以考虑os.path 库中一些函数来使用列表推导式

import os.path

names = [name for name in os.listdir('/')
         if os.path.isfile(os.path.join('somedir', name))]

print(names)

dirnames = [name for name in os.listdir('/')
            if os.path.isdir(os.path.join('somedir', name))]

# 字符串的 startswith() 和 endswith() 方法对于过滤一个目录的内容也很有用

pyfile = [name for name in os.listdir('/') if name.endswith('.py')]

# 对于文件名匹配 可以考虑使用 glob 或者 fnmatch 模块
import glob


pyfile = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('/') if fnmatch(name, '*.py')]


# 获取目录中列表很容易 但是其返回结果只是目录中实体名列表而已
# 如果你还想获取其他元信息 比如文件大小 修改时间等等 你或许还需要使用 os.path 模块中
# 函数或者 os.stat 函数收集信息

import os
import os.path
import glob

pyfile = glob.glob('*.py')

name_sz_data = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfile]

for name, size, mtime in name_sz_data:
    print(name, size, mtime)

file_metadata = [(name, os.stat(name)) for name in  pyfile]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)

# 还有一点 需要注意 有时候在处理文件名编码时候会出现一些问题 通常讲 函数 os.listdir
# 返回的实体列表会根据系统默认的文件名编码来解码
# 但有时候会碰到一些不能正常解码的文件名



