#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 根据一个或多个字段对字典列表进行排序
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

print('*' * 50)

# itemgetter()也支持多个 keys
rows_by_more = sorted(rows, key=itemgetter('lname', 'fname'))

print(rows_by_more)


# 多个字段情况下 itemgetter 会返回一个包含元素值的元祖 然后根据元祖排序

# 同样 lamdba 也可替代itemgetter() 但是效率会差点
# 同样的 min() max()方法同样适用该操作
