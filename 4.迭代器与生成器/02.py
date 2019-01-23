#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 自定义容器对象 直接在新容器对象执行迭代操作

# 只需要一个 __iter__() 方法 将迭代操作代理到容器内部对象


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


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)

for ch in root:
    print(ch)

# 上面的代码中 __iter__() 方法只是简单的将迭代强求传递给
# 内部的 _children属性

# python 的迭代器协议需要 __iter__() 方法返回一个实现了
# __next__()方法的迭代器对象 如果只是迭代遍历其他容器的内容
# 无须担心底层实现 只要传递迭代请求即可

# 这里的 iter() 函数使用简化了代码 iter(s) 只是简单通过调用
# s.__iter__()方法来返回对应的迭代器对象
# 就跟 len(s) 会调用 s.__len__原理一样
