#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 不用 for 循环遍历可迭代对象

# 手动遍历可迭代对象 可以是用哪个 next()函数 并在代码中
# 捕获 StopIteration 异常


def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


manual_iter()

print('#' * 50)

# 通常 StopIteration 用来指示迭代结尾
# 如果你手动使用 next() 还可以返回一个指定标记结尾 比如 None

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

print('#' * 50)
# 大多数情况下 会使用 for 循环语句遍历一个可迭代对象
# 但是 偶尔需要对迭代更加精确的控制

items = [1, 2, 3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

