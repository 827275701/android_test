#!/usr/bin/env python
# coding=utf-8

import socket

class recv(object):
    def __init__(self, sock):
        self.msg = '' 
        self.msg = 'HTTP/1.1 200 OK\r\n\r\n'
        self.sock = sock

    def login_yes(self):
        self.msg += 'yes\r\n'
        self.sock.send(self.msg.encode('utf-8'))

    def login_no(self):
        self.msg += 'no\r\n'
        self.sock.send(self.msg.encode('utf-8'))

    def login_other(self):
        self.msg += 'other\r\n'
        self.sock.send(self.msg.encode('utf-8'))

    def now_data(self):
        self.msg += 't_now:'
        self.msg += 'h_now:'
        self.msg += ''
        self.sock.send(self.msg.encode('utf-8'))

    def person_info(self):
        self.msg += 'name=lhwie,id=001,age=20,date=2015-2-14,berthday=1777-10-21,motto=xxxxxxxxxi\0\r\n'
        self.sock.send(self.msg.encode('utf-8'))
