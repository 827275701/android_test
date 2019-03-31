#!/usr/bin/env python3
# coding=utf-8

# 导入 socket、sys 模块
import socket
import sys
import test_recv

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 设置端口复用
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()  

    buf = clientsocket.recv(1024)
    print(buf)

    m = test_recv.recv(clientsocket)
    #m.login_yes()
    #m.login_no()
    #m.login_other()
    m.person_info()
    clientsocket.close()










