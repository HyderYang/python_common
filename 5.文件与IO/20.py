#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 通过串行端口读写数据典型场景就是与硬件设备通讯

# 可以使用内置 IO 模块来完成这个任务 但是对于串行通信最好选择
# 是使用 pySerial 包 这个包使用非常简单 先安装 pySerial 使用
# 类似下面的这样代码就能很容易打开一个串行端口
import serial


ser = serial.Serial('/dev/tty.usbmodem641', # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

# 设备名对于不同的设备和操作系统那个能是不一样的  比如 在windows 上可以使用 0, 1表示
# 一个设备打开通信端口 com0 com1 一旦端口打开 就可以使用 read readline write

ser.write(b'G1 X50 Y51')
resp = ser.readline()

# 尽管看起来简单 但是实际上挺麻烦的 推荐使用pyserial一个原因是它提供了对高级特性的支持 比如
# 超时 控制流 缓冲区刷新 握手协议等等

# 所有涉及到串口的 IO 都是二进制模式 因此 确保代码使用字节而不是文本
# 另外创建二进制编码的指令或者数据包时候 struct 模块也非常有用

