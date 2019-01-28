#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 读写各种不同编码的文本数据 如 ascii utf8

# 使用带有 rt 模式的open 函数读取文本文件

with open('test.txt', 'rt') as f:
    data = f.read()

with open('test.txt', 'rt') as f:
    for line in f:
        print(line)

print('#' * 50)

# 类似的 为了写入一个文本文件 使用 'wt' 模式 open 函数
# 如果之前存在数据则清除并覆盖

with open('somefile.txt', 'wt') as f:
    # f.write(text1)
    # f.write(text2)
    pass

with open('somefile.txt', 'wt') as f:
    # print(line1, file=f)
    # print(line2, file=f)
    pass

# 如果在已存在文件中添加内容 使用模式为 at 的 open 函数

# 文件的读写操作默认使用系统编码 可以通过调用 sys.getdefaultencoding() 来得到
# 在大多数机器上都是 utf-8
# 如果你已经知道你要读写文本是其他编码方式 那么 可以通过传递一个可选的 encoding参数给 open 函数

with open('test.txt', 'rt', encoding='utf-8') as f:
    pass

# python 支持非常多的文本编码 常见的是 ascii latin-1 utf-8
# utf-16等等

# 读写文本文件一般比较简单 但需要注意的是 例子中with语句
# 给被使用到的文件创建了一个上下文环境 但 with 控制块结束的时候
# 文件会自动关闭

# 另外一个问题是 换行符 unix和windows 是不一样的
# python 会统一模式处理换行符 在输出时候会将换行符 \n 转为系统默认的换行符
# 如果想换别种处理方式 可以添加 open 的关键字参数 newline

# 最后就是编码问题 可能有些文件会出现编码错误
# 应该尽量以 utf-8 保存文件与读取文件
