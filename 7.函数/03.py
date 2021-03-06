#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 给函数参数增加一些额外的信息
# 函数参数注解 提示应该怎么正确使用这个函数


def add(x: int, y: int) -> int:
    return x + y


# python 解释器不会对这些注解添加任何语义 他们不会类型检查 运行时跟没有加注解之前效果没有
# 任何差别 但是对程序员和IDE 就非常有意义

print(help(add))

# 尽管你可以使用任意类型的对象给函数添加注解(例如数字，字符串，对象实例等等)，不过通常来讲
# 使用类或者字符串会比较好点。

# 函数注解只存储在函数的 __annotations__ 属性中。例如：

print(add.__annotations__)

# 尽管注解的使用方法可能有很多种，但是它们的主要用途还是文档。 因为python并没有类型声明，
# 通常来讲仅仅通过阅读源码很难知道应该传递什么样的参数给这个函数。 这时候使用注解就
# 能给程序员更多的提示，让他们可以正确的使用函数。
