#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 基本日期与时间转换
# 需要执行简单的时间转换 比如 天到秒 小时到分钟

# 执行不同的时间单位转换和计算 应该使用 datetime
# 表示一个时间段 可以创建一个 timedelta 实例
from datetime import timedelta, datetime

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)

c = a + b

print(c.days)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

print('#' * 50)

# 如果想表示指定日期和时间 先创建一个 datetime 实例 然后使用标准的数学运算操作他们

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

print('#' * 50)
# 计算的时候 datetime会自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
print((a - b).days)

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)

print('#' * 50)
# 大多数基本日期和时间处理 datetime 足够了
# 如果执行更加复杂的日期操作 可以使用dateutil

# 许多类似时间计算可以使用 dateutil.relativedelta()代替
# 需要注意的是 他会在处理月份(还有天数差距)的时候填充空隙




