#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 有一个CIDR网络地址比如“123.45.67.89/27”，你想将其转换成它所代表的所有IP （比如，
# “123.45.67.64”, “123.45.67.65”, …, “123.45.67.95”)）

# 可以使用 ipaddress 模块很容易的实现这样的计算。例如：
import ipaddress
from socket import socket, AF_INET, SOCK_STREAM

net = ipaddress.ip_network('123.45.67.64/27')
for a in net:
    print(a)

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for a in net6:
    print(a)

# Network 也允许像数组一样的索引取值，例如：
print(net.num_addresses)
print(net[0])
print(net[1])
print(net[-1])
print(net[-2])

# 另外，你还可以执行网络成员检查之类的操作：
a = ipaddress.ip_address('123.45.67.69')
print(a in net)

b = ipaddress.ip_address('123.45.67.123')
print(b in net)

# 一个IP地址和网络地址能通过一个IP接口来指定，例如：
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)

# ipaddress 模块有很多类可以表示IP地址、网络和接口。 当你需要操作网络地址（比如解析、打印、
# 验证等）的时候会很有用。
#
# 要注意的是，ipaddress 模块跟其他一些和网络相关的模块比如 socket 库交集很少。 所以，你不能
# 使用 IPv4Address
# 的实例来代替一个地址字符串，你首先得显式的使用 str() 转换它。例如：

a = ipaddress.ip_address('127.0.0.1')
s = socket(AF_INET, SOCK_STREAM)
s.connect((a, 8080))
s.connect((str(a), 8080))
