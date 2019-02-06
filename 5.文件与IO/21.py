#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 将一个python对象序列化为一个字节流 方便保存到文件 数据库 或者网络传输

# 序列化最普遍的做法就是pickle模块 保存到文件:
import pickle
import math


data = 'some object'
f = open('somefile.txt', 'wb')
pickle.dump(data, f)

# 为了将一个对象转储为一个字符串 可以使用 pickle.dumps()

s = pickle.dump(data)

# 为了从字节流中回恢复一个对象 使用 pickle.load() 或者 pickle.loads()

f = open('somefile.txt', 'rb')
data = pickle.load(f)

data = pickle.loads(s)

# 对于大多数程序来讲 dump 和 load 函数的使用就是有效使用 pickle 模块所需的全部
# 它可适用于绝大部分python数据类型和用户自定义类的对象实例 大部分在数据库或者网络传输对象底层库
# 有可能就是使用 pickle 模块

# pickle 是一种python 特有的自描述数据编码 通过自描述 被序列化后数据包含每个对象开始和结束以及
# 它的类型信息 因此 无需担心对象记录的定义


f = open('somefile.txt', 'wb')
pickle.dump([1,2,3,4], f)
pickle.dump('hello', f)
pickle.dump({'apple', 'pear', 'banana'}, f)
f.close()
f = open('somedata.txt', 'rb')
pickle.load(f)
pickle.load(f)
pickle.load(f)

# 还能序列化 函数 类 接口 但是结果数据仅仅将它们的名称编码成对应的代码对象
pickle.dumps(math.cos)

# 当数据反序列化回来的时候 先假定所有的源数据时可用的 模块 类 函数会自动按需导入进来 对于 python 数据被不同
# 机器上的解析器所共享应用程序而言 数据保存可能会有问题 因为所有机器必须访问同一个源代码

# 其他 略









