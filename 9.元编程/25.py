#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 想通过将你的代码反编译成低级的字节码来查看它底层的工作机制。
# dis 模块可以被用来输出任何Python函数的反编译结果。例如：
import dis
import opcode


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')


print(dis.dis(countdown))

# 当你想要知道你的程序底层的运行机制的时候，dis 模块是很有用的。比如如果你想试着理解性能特征。
# 被 dis() 函数解析的原始字节码如下所示：
print(countdown.__code__.co_code)

# 如果你想自己解释这段代码，你需要使用一些在 opcode 模块中定义的常量。例如：
c = countdown.__code__.co_code

print(opcode.opname[c[0]])
print(opcode.opname[c[0]])
print(opcode.opname[c[3]])

# 奇怪的是，在 dis 模块中并没有函数让你以编程方式很容易的来处理字节码。 不过，下面的生成器函数
# 可以将原始字节码序列转换成 opcodes 和参数。
import opcode


def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)


# 使用方法如下：
for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)


# 这种方式很少有人知道，你可以利用它替换任何你想要替换的函数的原始字节码。 下面我们用一个示例来演
# 示整个过程：
def add(x, y):
    return x + y


c = add.__code__
print(c)
print(c.co_code)

# Make a completely new code object with bogus byte code
import types

newbytecode = b'xxxxxxx'
nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount,
                    c.co_nlocals, c.co_stacksize, c.co_flags, newbytecode,
                    c.co_consts,
                    c.co_names, c.co_varnames, c.co_filename, c.co_name,
                    c.co_firstlineno, c.co_lnotab)
print(nc)

add.__code__ = nc
print(add(2, 3))

print()

# 你可以像这样耍大招让解释器奔溃。但是，对于编写更高级优化和元编程工具的程序员来讲， 他们可能真的需
# 要重写字节码。本节最后的部分演示了这个是怎样做到的。
