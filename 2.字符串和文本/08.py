#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 用正则匹配一大块文本 需要跨越多行去匹配

# 当用 . 去匹配任意字符的时候 忘记了 . 不能匹配换行符号
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''

print(comment.findall(text1))
print(comment.findall(text2))

print('*' * 50)

# 修改匹配模式 增加对换行符号的支持

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

print('*' * 50)

# re.compile() 函数接受一个标志参数叫做 re.DOTALL
# 它可以让正则中的 . 匹配包括换行符在内的任意字符

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))

