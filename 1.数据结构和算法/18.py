#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 下标访问数组或元祖通常难以阅读
# collections.namedtuple 函数使用一个元祖对象管理数据
# namedtuple 返回一个python标准元祖子类的工厂方法
# 它会返回一个类 然后为这个类初始化并为字段传值
from collections import namedtuple

subscriber = namedtuple("subscriber", ['addr', 'joined'])
sub = subscriber('111@qq.com', '2018-12-03')
print(sub)
print(sub.addr)
print(sub.joined)

print('*' * 50)

# 尽管 namedtuple 实例看起来像一个普通类 但是跟元祖类型可交换
# 支持所有普通元祖操作

print(len(sub))

addr, joined = sub

print(addr)
print(joined)

print('*' * 50)

# 命名元祖另一个作用是字典的代替 因为字典会占用更多的内存
# 如果需要构建一个大字典 那么使用命名元组会更高效
# 但要注意 命名元祖一般不可更改
# 如果非要更改属性 可以使用 _replace()函数
# 它会返回一个新的命名元组并将对应的字段用新值取代

print(sub)
new_sub = sub._replace(addr='222@qq.com')
print(new_sub)


print('*' * 50)

# _replace()还有一个有用的特性就是拥有可选或者缺失字段的时候
# 它是一个非常方便的填充数据的方法

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}

print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}

print(dict_to_stock(b))


