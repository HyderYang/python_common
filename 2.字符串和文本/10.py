#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 使用正则表达式处理文本 但关注的是 unicode 字符处理

# 默认情况下 re 模块已经对一些 unicode 字符有了基本支持
# 比如 \d已经匹配任意 unicode 数字字符

import re


num = re.compile('\d+')

print(num.match('123'))

print(num.match('\u0661\u0662\u0663'))

print('*' * 50)

# 如果想在模式中包含指定的 unicode 字符 你可以使用 unicode 字符
# 对应的转义序列

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# 当执行匹配和搜索操作的时候 最好是先标准化并且清理所有文本为标准化格式
# 但需要注意一些特殊情况 如 大小写匹配

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))

print(pat.match(s.upper()))  # Doesn't match
print(s.upper())  # Case folds


