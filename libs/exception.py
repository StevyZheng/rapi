# -*- coding: utf-8 -*-


class MyException(Exception):
    def __init__(self, *args):
        self.args = args


class TypeException(MyException):
    def __init__(self, code=100, message="TypeError", args=('TypeError',)):
        self.args = args
        self.message = message
        self.code = code

