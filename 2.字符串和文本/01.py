#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 将字符串分割为多个字段 但是分隔符并不是固定的

# string 对象的 split 方法只适用于简单的字符串分割
# 当需要更加灵活的切割的时候 最好使用 re.split()

line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
text = re.split(r'[.;,\s]\s*', line)
print(text)

# 上面的例子中 分隔符可以是 逗号 分号 或者空格 并且后面紧跟着任意空格

