#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 匹配和搜索特定模式文本

# 如果想匹配字符串 只需要调用最基本的方法就好

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')

print(text.startswith('yeah'))

print(text.endswith('no'))
print(text.find('no'))

print('*' * 50)

# 复杂的匹配需要 re模块


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')


if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

print('*' * 50)

# 如果使用同一个模式去做多次匹配 应该先将模式字符串预编译为模式对象

datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')


if datepat.match(text2):
    print('yes')
else:
    print('no')


print('*' * 50)

# match 总是从字符串开始匹配 如果想要查找字符串任意部分的模板
# 可以使用findall 方法

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))



