#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 忽略大小写方式搜索和替换你文本

# 在文本操作的时候忽略大小写 需要在使用 re 模块的时候提供标识参数
# re.IGNORECASE
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
new_text = re.findall('python', text, flags=re.IGNORECASE)

print(new_text)

new_text = re.sub('python', 'snake', text, flags=re.IGNORECASE)

print(new_text)


