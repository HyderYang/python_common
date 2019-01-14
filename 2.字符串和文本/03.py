#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 使用通配符 * 去匹配文本字符串
# fnmatch 模块提供了两个函数 -- fnmatch() 和 fnmatchcase()

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt', '?oo.txt'))

print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

print([name for name in names if fnmatch(name, 'Dat*.csv')])

# fnmatch()函数使用底层操作系统大小写敏感规则
# macos 对大小写敏感
# windows 对大小写不敏感

print('*' * 50)

# 如果需要忽略大小写 需要用 fnmatchcase
# 此函数对大小写完全能匹配

print(fnmatchcase('foo.txt', '*.TXT'))

# 通常这两个函数对非文件名字符串也很有用

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])

print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

