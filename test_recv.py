#!/usr/bin/env python
# coding=utf-8

import socket

class recv(object):
    def __init__(self, sock):
        self.msg = 'HTTP/1.1 200 OK\r\n\r\n'
        self.sock = sock

    def login_yes(self):
        self.msg += 'yes\r\n'
        self.sock.send(self.msg.encode('utf-8'))

    def login_no(self):
        self.msg += 'no\r\n'
        self.sock.send(self.msg.encode('utf-8'))

    def now_data(self):
        self.msg += 't_now:'
        self.msg += 'h_now:'
        self.msg += ''
        self.sock.send(self.msg.encode('utf-8'))

