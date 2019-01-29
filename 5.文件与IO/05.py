#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 在文件中写入数据 但是这个文件在文件系统中不存在
# 也就是不允许覆盖存在文件内容

# 可以在 open 函数中使用 x 模式来代替 w 模式方法解决

with open('somefile', 'wt') as f:
    f.write('hello\n')

with open('somefile', 'xt') as f:
    f.write('hello\n')

# 如果文件是二进制的 使用 xb代替xt

print('#' * 50)

# 还有一种解决方案是先测试这个文件是否存在

import os

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('hello\n')
else:
    print('file already exists!')


# 使用 x 文件模式 更加简单 但是 x模式使用 python3 对open
# 函数的特有扩展 在python 旧版本是没有这个模式的
