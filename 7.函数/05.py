#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 定义一个函数或者方法 它的一个或多个参数是可选的 并且有一个默认值

# 定义一个有可选参数的函数直接在函数定义中给参数指定一个默认值 并放到参数列表最后就行了


def spam(a, b=42):
    print(a, b)


print(spam(1))
print(spam(1, 2))


# 如果默认参数是一个可修改的容器 比如列表 集合 字典 可使用 None 作为默认值


def spam(a, b=None):
    if b is None:
        b = []


# 如果并不想提供一个默认值 而是仅仅测试某个默认参数是不是传递进来

_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


spam(1)
spam(1, 2)
spam(1, None)
# 传递None 和 不传值是有区别的

# 默认参数的值仅仅在函数定义的时候赋值一次

x = 42


def spam(a, b=x):
    print(a, b)


print(spam(1))

x = 23
print(spam(1))

print('@' * 50)


# 当我们改变x的值时候 默认参数值并没有影响 因为在函数定义的时候就已经确定了默认值

# 其次 默认参数的值 应该是不可变的对象 比如 None True False 数字或者字符
# 不要像下面一样:


def spam(a, b=[]):  # 不规范的定义
    print(b)
    return b


x = spam(1)
print(x)

x.append(99)
x.append('yow!')

print(x)
print(spam(1))


# 这样的结果并不是想要的 为了避免这种情况发生 最好将默认值设为 None 然后
# 在函数里面检查他
# 在测试None值得时候 使用 is 操作符很重要 也是这种方案的关键点


def spam(a, b=None):
    if not b:  # NO! Use 'b is None' instead
        b = []
        print('应该是None')


# 这么写问题在于 尽管 None 确实被当成False 但还是有其他的对象(空字符串 空列表/元祖/字典等)
# 都会被当做 False 因此 上面代码会误将一些其他输入也当成没有输入

print(spam(1))

x = []
print(spam(1, x))
print(spam(1, 0))
print(spam(1, ''))

# 最后一个问题比较微妙，那就是一个函数需要测试某个可选参数是否被使用者传递进来。 这时候需要
# 小心的是你不能用某个默认值比如None、 0或者False值来测试用户提供的值(因为这些值都
# 是合法的值，是可能被用户传递进来的)。 因此，你需要其他的解决方案了。
#
# 为了解决这个问题，你可以创建一个独一无二的私有对象实例，就像上面的_no_value变量那样。
# 在函数里面，你可以通过检查被传递参数值跟这个实例是否一样来判断。 这里的思路是用户不
# 可能去传递这个_no_value实例作为输入。 因此，这里通过检查这个值就能确定某个参数是否被传递进来了。
#
# 这里对 object() 的使用看上去有点不太常见。object 是python中所有类的基类。
# 你可以创建 object 类的实例，但是这些实例没什么实际用处，因为它并没有任何有用的方法，
# 也没有任何实例数据(因为它没有任何的实例字典，你甚至都不能设置任何属性值)。
# 你唯一能做的就是测试同一性。这个刚好符合我的要求，因为我在函数中就只是需要一个同一性的测试而已。
