#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 随机选择
# 从一个序列中随机抽取若干元素 或者想生成几个随机数

# random模块有大量函数用来产生随机数和随机选择元素
# 想要从一个序列中随机的抽取一个元素 可以使用 random.choice()

import random

values = [1, 2, 4, 5, 6, 7]

print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print('#' * 50)
# 为了提取出N个不同元素的眼你根本用来做进一步操作 可以使用 random.sample()

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 3))

print('#' * 50)
# 如果仅仅是打乱序列中元素的顺序 可以使用 random.shuffle()
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)


print('#' * 50)
# 生成随机整数 需要使用 random.randint()
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))


print('#' * 50)
# 生成 0-1范围内均匀分布的浮点数 使用 random.random()

print(random.random())
print(random.random())
print(random.random())
print(random.random())


print('#' * 50)
# 如果要获取N位随机位(二进制)整数 使用 random.getrandbits()
print(random.getrandbits(200))


# random函数可以使用 random.seed()函数修改初始化种子

