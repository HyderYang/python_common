#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 用正则匹配某个文本模式 但是它找到的是模式的最长可能匹配
# 而你想修改它变成查找最短的可能匹配
import re

str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
new_text = str_pat.findall(text1)

print(new_text)

text2 = 'Computer says "no." Phone says "yes."'
new_text = str_pat.findall(text2)

print(new_text)

# 上面的例子中 模式 "(.*)" 意图是匹配被双引号包含的文本 但是在正则表达式中
# * 操作符是贪婪的 因此匹配操作会查找最长的可能匹配
# 于是第二个例子中 可能并不是我们想要的

print('*' * 50)

str_pat = re.compile(r'"(.*?)"')
new_text = str_pat.findall(text2)

print(new_text)

# 加上了 ? 号 变为非贪婪模式 从而获得最短匹配 也就是我们想要的结果
