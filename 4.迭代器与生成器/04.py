#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 构建一个能支持迭代操作的自定义对象 并找到一个实现迭代协议的简单方法

# 在一个对象上实现迭代最简单的方式是使用一个生成器函数
# 实现一个深度优先方式遍历树形节点的生成器


class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)


# 这段代码中 depth_first() 方法简单直接 它首先返回自己本身
# 并迭代每一个子节点并通过调用子节点 depth_first()
# 使用 yield from 方法返回对应元素

print('#' * 50)

# python 迭代协议要求一个 __iter__ 方法返回一个特殊的迭代对象
# 这个迭代器对象实现了 __next__ 方法并通过 stopiteration 异常
# 标识迭代完成 但是 这些通常比较繁琐
# 下面方式 使用一个关联迭代器类重新实现 depth_first()


class Node2(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    """
    Depth-first traversal
    """

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                next_child = next(self._child_iter)
                return next_child
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(
                self._children_iter
            ).depth_first()
            return next(self)

# DepthFirstIterator 类和上面使用生成器版本工作原理类似
# 但非常繁琐晦涩 因为迭代处理过程中维护大量状态信息
# 将迭代器定义为一个生成器后一切迎刃而解
