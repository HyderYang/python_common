#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 字符串中搜索和匹配指定的文本模式
# 对于简单的字面模式 直接使用 str.replace()

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

print(text)

print('*' * 50)

# 对于复杂的模式 应该使用 re 模式 sub()函数

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(new_text)

print('*' * 30)











