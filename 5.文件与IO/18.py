#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 有一个对应操作系统上一个一打开的IO通道 比如文件/管道/套接字 的整型
# 文件描述符 想将他包装成一个更高层的python 文件对象

# 一个文件描述符 和 一个打开的普通文件是不一样的 文件描述符仅仅是一个由操作
# 系统指定的整数 用来指代某个系统的IO通道 如果你碰巧有这么一个文件描述符 你可以用
# open 函数来将其包装为一个 python 的文件对象 仅仅只需要使用这个整数值的文件
# 描述符作为第一个参数来代替文件名即可

import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'wt')
f.write('hello world')
f.close()

# 当高层文件对象被关闭或者破坏的时候 底层的文件描述符也会被关闭 如果这个并不是你想要
# 的结果 你可以给 open 函数传递一个可选的 colsefd=False

f = open(fd, 'wt', closefd=False)

# 在 UNIX 系统中 这种包装文件描述符的技术可以很方便的将一个类文件接口作用于一个以
# 不同方式打开的 IO通道上 下面是一个操作管道的例子
from socket import socket, AF_INET, SOCK_STREAM


def echo_client(client_sock, addr):
    print('got connection from', addr)

    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)
    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


# 需要强调的是 上面的例子仅仅是演示内置的 open 函数的一个特性
# 并且也只适用于基于 UNIX 的系统 如果想将一个类文件接口作用在一个套接字并希望你的代码
# 可以跨平台 应使用套接字对象的 makefile() 方法 如果不考虑可移植性的话 上面的解决方案会比
# 使用 makefile 性能好一点

# 你可以使用这种技术来构造一个别名 允许以不同第一次打开文件的方式使用它
# 下面创建一个文件对象 允许你输出二进制数据到标准输出

import sys
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()

# 尽管可以将一个存在的文件描述包装成一个正常的文件对象 但是要注意的并不是所有的文件模式都被支持
# 并且某些类型的文件描述符可能会有副作用 特别是涉及错误处理 文件结尾条件等等的时候
# 在不同的操作系统上这种行为也不一样 特别的 上面例子都不能在非unix系统上运行
