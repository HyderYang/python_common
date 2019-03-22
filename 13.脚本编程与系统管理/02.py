#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 想向标准错误打印一条消息并返回某个非零状态码来终止程序运行
# 你有一个程序像下面这样终止，抛出一个 SystemExit 异常，使用错误消息作为参数。例如：

raise SystemExit('It failed!')

# 它会将消息在 sys.stderr 中打印，然后程序以状态码1退出。
# 本节虽然很短小，但是它能解决在写脚本时的一个常见问题。 也就是说，当你想要终止某个程序时，你可能
# 会像下面这样写：
import sys

sys.stderr.write('It failed!\n')
raise SystemExit(1)

# 如果你直接将消息作为参数传给 SystemExit() ，那么你可以省略其他步骤， 比如import语句或将
# 错误消息写入 sys.stderr
