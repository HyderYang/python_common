#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 将多层迁到薛烈展开成一个单层嵌套
# 可以写一个包含 yield from 语句递归器
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x)


print('#' * 50)


# 上面代码中 isinstance(x, iterable) 检查某个元素是否可以迭代 如果是 yield from 就返回所有子例程的值
# 最终返回结果实一个没有嵌套的简单序列

# 额外的参数 ignore_types 和 检测语句 isinstace(x, ignore_type)用来将字符串和字节排除在可迭代对象外
# 防止他们再展开成单个字符
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)

# 语句 yield from 在你想在生成器中掉用哪个其他生成器作为子例程非常有用
# 如果你不使用它 那么就必须使用额外的 for 循环了


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x

"""
尽管只改了一点点，但是 yield from 语句看上去感觉更好，并且也使得代码更简洁清爽。

之前提到的对于字符串和字节的额外检查是为了防止将它们再展开成单个字符。 如果还有其他你不想展开的类型，修改参数 ignore_types 即可。

最后要注意的一点是， yield from 在涉及到基于协程和生成器的并发编程中扮演着更加重要的角色
"""
