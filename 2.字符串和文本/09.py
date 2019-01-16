#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#处理 unicode 字符串 需要确保所有字符串在底层有相同表示
import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)

print(s1 == s2)
print(s1 == s2)

print(len(s1))
print(len(s2))

print('*' * 50)

# 需要比较字符串的程序中使用字符多种表示可能会产生问题
# 需要先将文本标准化

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)

print(t3 == t4)
print(ascii(t3))

# normalize 第一个参数指定字符串标准化的方式 NFC 表示字符串应该是整体组成
# 而 NFD 表示字符应该分解为多个组合字符表示



