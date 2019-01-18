#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 转换HTML或者XML实体如 &entity &#code 替换为对应的文本

# 如果你想替换文本字符串中的 < > 使用 html.escape 函数可以很容易的完成

s = 'Elements are written as <tag>text</tag>'

import html

print(s)

print(html.escape(s))

print(html.escape(s, quote=False))

print('#' * 50)

# 如果你处理的是 ASCII 文本 并且将 ASCII文本对应的编码实体嵌入进去
# 可以使用函数传递参数 errors = 'xmlcharrefreplace'

s = 'Spicy &quot;Jalape&#241;o&quot'

from html.parser import HTMLParser

p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape

print(unescape(t))
