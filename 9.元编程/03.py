#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 一个装饰器已经作用在一个函数上了 想撤销装饰器作用 直接访问原始未包装
# 那个函数
from functools import wraps


# 假设装饰器通过 @wraps 来实现 那么可以通过访问 __wrapped__ 属性来访问原始函数

# @somedecorator
def add(x, y):
    return x + y


orig_add = add.__wrapped__
orig_add(3, 4)


# 直接访问未包装的原始函数在调试、内省和其他函数操作时是很有用的。 但是我们这里的方案仅仅适用于在
# 包装器中正确使用了 @wraps 或者直接设置了
# __wrapped__ 属性的情况。
#
# 如果有多个包装器，那么访问 __wrapped__ 属性的行为是不可预知的，应该避免这样做。
# 在Python3.3中，它会略过所有的包装层，比如，假如你有如下的代码：


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


# 下面我们在Python3.3下测试：
add(2, 3)
# Decorator 1
# Decorator 2
# 5
add.__wrapped__(2, 3)

# 下面我们在Python3.4下测试：

add(2, 3)
# Decorator 1
# Decorator 2
# 5
add.__wrapped__(2, 3)
# Decorator 2
# 5

# 最后要说的是，并不是所有的装饰器都使用了 @wraps ，因此这里的方案并不全部适用。 特别的，内置的
# 装饰器 @staticmethod 和 @classmethod 就没有遵循这个约定 (它们把原始函数存储在属性 __func__ 中)。
