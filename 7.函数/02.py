#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 函数的某些参数强制使用关键字参数传递

# 将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果


def recv(maxsize, *, block):
    """Receives a message"""
    pass


recv(1024, True)  # TypeError
recv(1024, block=True)  # Ok


# 利用这种机制 还能接受任意多个位置参数的函数中指定关键字参数


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


minimum(1, 5, 2, -5, 10)  # Returns -5
minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0

# 很多情况下 使用强制关键字参数会比使用位置参数表意更加清晰 程序也更加具有可读性


msg = recv(1024, False)

# 另外 使用强制关键字参数也会比使用 **kwargs 参数更好 因为在使用函数 help 的时候输出也会
# 更容易理解

help(recv)

# 强制关键字参数在一些更高级场合同样也很有用。 例如，它们可以被用来在使用*args和**kwargs
# 参数作为输入的函数中插入参数，
