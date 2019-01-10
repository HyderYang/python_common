#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 找出一个序列中出现次数最多的元素
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

word_counts = Counter(words)

top_three = word_counts.most_common(3)
print(top_three)

print('*' * 50)

# 计数器相加操作
word_counts.update(morewords)
print(word_counts)

print('*' * 50)

# 计数器可以很和数学运算联系起来

a = Counter(word_counts)
b = Counter(morewords)

c = a + b
print(c)

d = a - b
print(d)





