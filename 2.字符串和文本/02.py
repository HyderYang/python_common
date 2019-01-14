#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 检查字符串的开头或者结尾 比如 url等等

filename = 'spam.txt'
print(filename.endswith('.txt'))

print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

print('*' * 50)

# 如果想匹配多种可能 只需要将所有匹配项放到一个元祖中
# 然后传给 startwith()或者endwith()中

import os

filenames = os.listdir('.')
print(filenames)

print([name for name in filenames if name.endswith(('.py', '.txt'))])

# 同样的 你可以使用 切片或者 re.match 实现
