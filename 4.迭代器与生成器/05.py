#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 反向迭代一个序列
# 使用内置的 reversed()函数

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# 反向迭代仅仅当对象大小可预先确定或者对象实现了 __reversed__
# 特殊方法才能生效
# 如果两者都不符合 那必须将对象转为一个列表才行

print('#' * 50)
for line in reversed(list(open('/etc/passwd'))):
    print(line, end='')

# 需要注意的是 如果可迭代对象元素很多 将其转为一个列表要消耗大量内存

print('#' * 50)

# 在自定义类上实现 __reversed__() 方法实现反向迭代:


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr)

print('#' * 20)

for rr in Countdown(30):
    print(rr)

# 定义一个反向迭代器可以使得代码非常高效
# 它不必转换为列表然后再去反向迭代这个列表
