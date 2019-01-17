#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 使用 textwrap 模块来格式化字符串的输出。比如，假如你有下列的长字符串：
import os
import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."


print(textwrap.fill(s, 70))


print(textwrap.fill(s, 40))

print(textwrap.fill(s, 40, initial_indent='    '))

print(textwrap.fill(s, 40, subsequent_indent='    '))


# textwrap 模块对于字符串打印是非常有用的，
# 特别是当你希望输出自动匹配终端大小的时候。
# 你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸

print(os.get_terminal_size().columns)

