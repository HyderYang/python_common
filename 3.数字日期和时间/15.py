#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 字符串转为 datetime对象

from datetime import datetime


text = '2012-09-23'

y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()

diff = z - y
print(diff)

print('#' * 50)

# 有一个datetime对象 转为字符串

print(z)

z_str = datetime.strftime(z, '%A %B %d, %Y')

print(z_str)



