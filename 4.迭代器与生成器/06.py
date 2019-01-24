#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 定义一个生成器函数 但是会调用某个你想暴露给用用户使用的外部状态值

# 如果想让生成器暴露外部状态给用户 先简单实现一个类 然后
# 将生成器函数放到 __iter__ 方法中
from collections import deque


class LineHistory(object):

    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('01.py') as f:
    lines = LineHistory(f)
    for line in lines:
        for lineno, hline in lines.history:
            print('{}:{}'.format(lineno, hline), end='')

print('#' * 50)

# 如果 迭代操作不适用for循环 那么首先调用 iter() 函数

lines = LineHistory(open('01.py'))
it = iter(lines)

next(it)
next(it)
next(it)
next(it)
next(it)
next(it)
next(it)




