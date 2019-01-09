#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
队列优先级
"""
import heapq


class PriorityQueue(object):

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

"""
使用 heapq的 heappush 和 heappop 方法实现从列表 PriorityQueue._queue 的推入取出

队列以(-priority, index, item)形式存储

priority取负值是为了让队列以优先级从高到低排列 因为一般情况下堆按照从小到大排列

存储 index 是为了将相同优先级以适当的顺序排列 因为传入的优先级 priority 可能相同
这样 维护一个自增类变量加以区分优先级使得比较操作得以进行
"""
