#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 有一个字节字符串 想把它转换成整数 或者 将大整数转换为字节字符串

# 如果需要处理一个拥有 128位长的16个元素字节字符

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# 为了将 bytes 解析为整数 使用 int.form_bytes()方法

print(len(data))

print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

print('#' * 50)

# 为了将一个大整数转换为一个字节字符串 使用 int.to_bytes()

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

print('#' * 50)

# 大整数和字节字符串之间的转换操作并不常见
# 但在一些特地你那个领域 如密码或者网路
# ipv6网络地址使用一个128位整数表示







