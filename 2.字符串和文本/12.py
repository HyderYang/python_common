#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 审查清理文本字符串
# 清除非法字符

# 文本清理问题会涉及到包括文本解析与数据处理等问题
# 比如先将字符串标准化 然后使用 replace 等函数替换或者删除字符
import sys
import unicodedata

s = 'pýtĥöñ\fis\tawesome\r\n'

print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}

a = s.translate(remap)
print(a)

print('#' * 50)

# 然年进一步构建更强大的表格 比如删除所有和音符

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)

print(b.translate(cmb_chrs))

# 上面的例子中 使用 dict.fromkeys 方法构建一个字典 每个 unicode和音符作为键对应的值全部为 None

# 然后使用 unicodedata.normalize() 将原始输入标准化为分解形式字符
# 然后再调用 translate 函数删除所有重音符?


