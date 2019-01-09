#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
有序字典

有序字典占用内存比普通字典大2倍多

数据量小不易测出
"""
import json
from collections import OrderedDict

d = {'foo': 1, 'bar': 2, 'spam': 3, 'grok': 4, 'vacation': 5}

print(json.dumps(d))

print('*' * 50)

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d['vacation'] = 5

print(json.dumps(d))
