#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
保存最后几个元素
"""
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)

print(q)

q.append(4)

print(q)

print('*' * 50)

"""
对于没有数量限制的 deque 可以从两端添加和弹出
"""
q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q)

q.appendleft(5)
print(q)

q.pop()
print(q)

q.popleft()
print(q)
