#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 写了个脚本，运行时需要一个密码。此脚本是交互式的，因此不能将密码在脚本中硬编码， 而是需要弹出一
# 个密码输入提示，让用户自己输入。
# 这时候Python的 getpass 模块正是你所需要的。你可以让你很轻松的弹出密码输入提示， 并且不会在
# 用户终端回显密码。下面是具体代码：

import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):    # You must write svc_login()
   print('Yay!')
else:
   print('Boo!')


# 在此代码中，svc_login() 是你要实现的处理密码的函数，具体的处理过程你自己决定。
# 注意在前面代码中 getpass.getuser() 不会弹出用户名的输入提示。 它会根据该用户的shell环境或者会依据本地系统的密码库（支持
# pwd 模块的平台）来使用当前用户的登录名，
#
# 如果你想显示的弹出用户名输入提示，使用内置的 input 函数：
#
user = input('Enter your username: ')
# 还有一点很重要，有些系统可能不支持 getpass() 方法隐藏输入密码。
# 这种情况下，Python会提前警告你这些问题（例如它会警告你说密码会以明文形式显示）










