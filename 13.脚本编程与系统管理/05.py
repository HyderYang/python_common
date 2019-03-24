#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 要知道当前终端的大小以便正确的格式化输出。
# 使用 os.get_terminal_size() 函数来做到这一点。

import os
sz = os.get_terminal_size()
print(sz)
print(sz.columns)
print(sz.lines)

# 有太多方式来得知终端大小了，从读取环境变量到执行底层的 ioctl() 函数等等。 不过，为什么要去研
# 究这些复杂的办法而不是仅仅调用一个简单的函数呢？

















