#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 遍历一个可迭代对象 但是它开始的某些元素你并不感兴趣
# itertools 模块有些函数可以完成这个任务
# 首先 itertools.dropwhile() 函数
# 它需要一个函数对象和一个可迭代对象 它返回一个迭代器对象 丢弃原有序列中直到函数
# 返回 False 之前的所有元素 然后返回后面所有元素
from itertools import dropwhile, islice

with open('/etc/passwd') as f:
    for line in f:
        print(line, end='')


print('#' * 50)

# 如果想跳过开头的注释部分 可以这样做
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# 这个例子是基于根据某个测试函数跳过开始的元素
# 如果已经明确知道了要跳过的元素个数 可以使用 itertools.islice()

print('#' * 50)

items = ['a', 'b', 'c', 1, 4, 10, 15]

for x in islice(items, 3, None):
    print(x)

# 这个例子中 islice() 函数最后 None 参数指定了你要获取从第三个到最后的
# 所有元素 如果 None 和 3 对调 意思就是仅仅获取前三个元素 [3:]/[:3]

print('#' * 50)

# 函数 dropwhile() 和 islice() 其实就是两个帮助函数 为了就是避免下面这种冗余代码

with open('/etc/passwd') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    while line:
        print(line, end='')
        line = next(f, None)

print('#' * 50)

# 跳过一个可迭代对象开始部分跟通常的过滤是不同的
# 比如 上述代码第一个部分可能会这样重写

with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

# 这样写确实可以跳过开始部分的注释行 但是同样会跳过文件中其他所有注释行
# 但需要仅仅是跳过开始部分满足测试条件的行 在那以后 所有元素不再进行测试和过滤

# 本节方案适用于所有可迭代对象 包括那些不能确定大小的 比如生成器 文件等等




