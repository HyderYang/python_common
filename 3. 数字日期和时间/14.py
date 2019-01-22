#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 代码需要在当前月份循环每一天
# 这样的日期上循环并需要事件构建一个包含所有日期的列表
# 先计算出开始日期和结束日期 然后步进的时候使用 datetime.timedelta
# 对象递增这个日期变量即可
import calendar
from datetime import date, timedelta, datetime


def get_mouth_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)

    _, days_in_month = calendar.monthrange(
        start_date.year,
        start_date.month
    )

    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


a_day = timedelta(days=1)

first_day, last_day = get_mouth_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day


# 上面的代码先计算出一个对应月份第一天日期
# 一个快速的方法就是使用 date 或者 datetime 对象的 replace
# 将days属性设置为1
# replace 方法好处就是它会创建一个和传入对象类型相同的方法
# 然后 使用 calendar.monthrange() 找出该月份总天数
# 任何时候想获取日历信息 calendar 模块就非常有用
# monthrange 函数会返回包含星期和该月天数的元祖

# 得知了该月的天数 就可以通过开始日期加上天数获得结束日期
# 需要注意的是 结束日期并不包含日期范围内

# 然后 使用 timedelta 实例来递增日期


# 生成器写法

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1),
                    datetime(2012, 10, 1),
                    timedelta(hours=6)):
    print(d)
