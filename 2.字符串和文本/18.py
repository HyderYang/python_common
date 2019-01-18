#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 字符串令牌解析

# 你有一个字符串 想从左到右解析为一个令牌流
from collections import namedtuple

text = 'foo = 23 + 42 * 10'

# 为了令牌化字符串 不仅需要匹配模式 还要指定模式类型

tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# 为了执行这样的切分，第一步就是像下面这样利用命名捕获组的正则表达式来定义所有可能的令牌，包括空格：

import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# 在上面的模式中， ?P<TOKENNAME> 用于给一个模式命名，供后面使用。

# 下一步，为了令牌化，使用模式对象很少被人知道的 scanner() 方法。 这个方法会创建一个 scanner 对象， 在这个对象上不断的调用 match() 方法会一步步的扫描目标文本，每步一个匹配。 下面是演示一个 scanner 对象如何工作的交互式例子：


scanner = master_pat.scanner('foo = 42')
print(scanner.match())

print(_.lastgroup, _.group())
print(scanner.match())
print(_.lastgroup, _.group())
print(scanner.match())
print(_.lastgroup, _.group())
print(scanner.match())
print(_.lastgroup, _.group())
print(scanner.match())
print(_.lastgroup, _.group())
print(scanner.match())


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
#
