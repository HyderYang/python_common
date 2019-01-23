#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 查找星期中某天最后出现的日期 如星期五

# python的 datetime 模块有工具函数执行这样的计算
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(datetime.today())
print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))
print(get_previous_byday('Friday'))

# 上面的算法原理:
# 现将开始日期和目标日期映射到星期数组的位置上(星期1为0)
# 然后通过取余 计算出目标日期经过多少天才能到达开始日期
# 然后用开始日期减去那个时间差就是结果日期

# 如果执行大量日期计算 最好使用 python-dateutil



