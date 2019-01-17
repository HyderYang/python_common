#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 将几个小的字符串合并为一个大字符串

# 如果合并的字符串在一个序列或者 iterable 中
# 最快的方式是使用join方法

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

print('*' * 50)

# 尽管看上去比较怪异 但是 join 被指定为字符串的一个方法
# 部分原因是想去连接的对象肯能来自各自不同的数据序列
# 因此 只需要指定想要的分割字符串并调用他的 join 方法组合起来就行

# 如果仅仅只是合并少数几个字符串 使用 + 号通常已经足够了

a = 'Is Chicago'
b = 'Not Chicago'

print(a + ' ' + b)

# 如果只想将两个字面字符串合并 只需要简单的放在一起 不需要 + 号

a = 'Hello' 'world'
print(a)


print('*' * 50)

# 永远不要使用循环 和 + 号来拼接字符串
# 因为每次循环都会创建一个新的字符串 最好是先收集所有字符串片段
# 然后连接起来

# 相对好点的是用生成器表达式
data = ['ACME', 50, 91.9]
print(',' . join(str(d) for d in data))


print('*' * 50)

# 同样还要注意不必要的字符串连接操作

print(a + ':' + b + ':' + '呵呵')
print(':' . join([a, b, '呵呵']))
print(a, b, 'hehe', sep=':')


print('*' * 50)

# 当混合使用 IO 和字符串连接的时候 需要权衡

# Version 1 (string concatenation)
# f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
# f.write(chunk1)
# f.write(chunk2)

# 如果两个字符串很小 那么 version1 性能会很好
# 如果两个字符串很大 那么 version2 性能会很好
# 因为 version 避免创建一个很大的临时结果并复制大量的内存块数据

# 最后 如果准备构建大量小字符串的输出代码时候 建议使用生成器
# 如下

# def combine(source, maxsize):
#     parts = []
#     size = 0
#     for part in source:
#         parts.append(part)
#         size += len(part)
#         if size > maxsize:
#             yield ''.join(parts)
#             parts = []
#             size = 0
#     yield ''.join(parts)
#
# # 结合文件操作
# with open('filename', 'w') as f:
#     for part in combine(sample(), 32768):
#         f.write(part)

