#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 处理一个很大的数据集并需要计算数据总和或其他统计量。

# 对于任何涉及到统计、时间序列以及其他相关技术的数据分析问题，都可以考虑使用 Pandas库 。
#
# 为了让你先体验下，下面是一个使用Pandas来分析芝加哥城市的 老鼠和啮齿类动物数据库 的例子。
# 在我写这篇文章的时候，这个数据库是一个拥有大概74,000行数据的CSV文件。
import pandas

# Read a CSV file, skipping last line
rats = pandas.read_csv('rats.csv', skip_footer=1)
print(rats)

# Investigate range of values for a certain field
print(rats['Current Activity'].unique())
# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
print(len(crew_dispatched))

print(crew_dispatched['ZIP Code'].value_counts()[:10])

dates = crew_dispatched.groupby('Completion Date')
print(dates)
print(len(dates))

date_counts = dates.size()
print(date_counts[0:10])

date_counts.sort()
print(date_counts[-10:])

# Pandas是一个拥有很多特性的大型函数库，我在这里不可能介绍完。 但是只要你需要去分析大型数据集合、
# 对数据分组、计算各种统计量或其他类似任务的话，这个函数库真的值得你去看一看。
