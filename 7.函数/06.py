#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 想为 某个函数 创建一个回调函数 但是不想使用 def 写一个单行函数

# 当一些函数很简单 仅仅是计算一个表达式值得时候 可以使用 lambda 表达式来代替


add = lambda x, y: x + y

print(add(2, 3))
print(add('hello', 'world'))


# 这里使用 lambda表达式跟下面效果一样


def add(x, y):
    return x + y


print(add(2, 3))

# 下面是在 sorted 中的使用场景:

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

# 尽管lambda表达式允许你定义简单函数，但是它的使用是有限制的。 你只能指定单个表达式，
# 它的值就是最后的返回值。也就是说不能包含其他的语言特性了， 包括多个语句、条件表达式、迭代以及异常处理等等。
#
# 你可以不使用lambda表达式就能编写大部分python代码。 但是，当有人编写大量计算表达式值的
# 短小函数或者需要用户提供回调函数的程序的时候， 你就会看到lambda表达式的身影了。
