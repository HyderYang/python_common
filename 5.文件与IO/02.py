#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 将 print 函数输出重定向到一个文件中

# 在print函数指定file 关键字参数:
with open('test.txt') as f:
    print('perl', file=f)


# 需要注意的是 文件必须是文本模式打开 如果是二进制打开 打印会出错
