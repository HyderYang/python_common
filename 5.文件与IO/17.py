#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 想在文本模式打开的文件中写入原始字节数据

# 将字节数据直接写入文件缓冲区即可
import sys

print(sys.stdout.write(b'write'))
print(sys.stdout.buffer.write(b'hello'))

# 类似的 能够通过读取文本文件的 buffer 属性来读取二进制数据


# IO 系统以层级结构的形式构建而成 文本文件是通过在一个拥有缓冲二进制模式文件
# 上增加一个 unicode 编码/解码 层来创建 buffer 属性指向对应的底层文件
# 如果你直接访问他的话就会绕过文本编码/解码层

# 展示的 sys.stdout 可能看起来有点特殊
# 默认下 sys.stdout 总是以文本模式打开 但是如果写一个需要打印二进制数据
# 到标准输出的脚本的话 可以用上面的方式
