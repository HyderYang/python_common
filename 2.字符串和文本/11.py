#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 去掉文本字符串你的开头 结尾 或者中间不想要的字符串 比如空格

# strip() 方法能删除开始或者结尾的字符
# lstrip 和 rstrip 分别删除左右字符
# 默认情况下 这些方法会去除空白字符 但也可指定其他字符

s = ' hello world \n '
print(s.strip())
print(s.lstrip())
print(s.rstrip())


t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

print('#' * 50)

# 这些 strip 方法在读取和清理数据以备后续处理的时候经常被用到

# 但需要注意的是 去除操作不会对字符串的中间的文本产生影响
# 如果想处理中间的空格 就需要借助其他技术 如 replace


