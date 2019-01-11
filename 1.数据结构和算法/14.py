#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# sorted 函数有关键字参数 key 可以传入一个 callable 对象给它
# 这个对象对每个传入的参数对象返回一个值 这个值会被 sordid\ted用来排序


class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})" . format(self.user_id)


users = [User(23), User(3), User(99)]


def sort_notcompare():
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


# sort_notcompare()

print('*' * 50)

# 也可以使用 operator.attrgetter() 代替 lambda 函数:

from operator import attrgetter

print(users)
print(sorted(users, key = attrgetter('user_id')))

# attrgetter() 函数通常比lambda函数效率高点 同样和 itemgetter()函数一样 可以对
# 对象多个属性进行排序 同样可以作用于 min() max()之类的函数
