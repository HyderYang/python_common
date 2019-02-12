#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 你用 lambda 定义了一个匿名函数 并想在定义时捕获某个变量值

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(a(10))

# lambda 表达式中 x 是一个自由变量 在运行时候绑定 而不是定义时候绑定
# 这跟默认值参数是不同的 因此 在调用的时候 x 是执行时候的值
# 在调用 lambda函数时候 会寻找最后最后定义的参数变量进行赋值 然后运算

x = 15
print(a(10))
x = 3
print(a(10))

# 如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

print('#' * 50)
# 在这里列出来的问题是新手很容易犯的错误，有些新手可能会不恰当的使用lambda表达式。
# 比如，通过在一个循环或列表推导中创建一个lambda表达式列表，并期望函数能在定义时就记住每次
# 的迭代值。例如：
funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))

print('#' * 50)

funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))

# 通过使用函数默认值参数形式，lambda函数在定义时就能绑定到值。
