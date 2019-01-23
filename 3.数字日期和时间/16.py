#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 结合时区的日期操作

# 对于所有涉及时区的问题 都应该使用 pytz 模块
# 它主要的用途就是将 datetime 的日期本地化

from datetime import datetime

import pytz
from pytz import timezone

d = datetime(2018, 12, 21, 9, 32, 0)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

print('#' * 50)

# 一旦日期被本地化 他就可以转换为其他时区的时间了

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

print('#' * 50 )

# 如果你打算本地化日期上执行计算 需要特别注意夏令时转换
# 为了修正夏令时错误 可以使用时区对象 normalize()

from datetime import timedelta

later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

print('#' * 50)
# 为了不考虑夏令时 可以考虑转换为 UTC 时间

print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)


print('#' * 50)
# 使用了 UTC 就不用去担心夏令时问题 当想输出变为本地时间时候
# 使用合适时区转换下就行

later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

print('#' * 50)
# 涉及到时区时候 如何得到时区的名称
# 可以使用 ISO3166 国家代码作为关键字去查阅字典
# pytz.country_timezones

print(pytz.country_timezones)
