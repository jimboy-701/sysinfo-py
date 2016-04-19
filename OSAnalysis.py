
import os
import subprocess


class Microsoft:
    def __init__(self,):

        import winreg
        import ctypes

        self.message_string = "This is from the Microsoft class!\n"


class Linux:
    def __init__(self,):
        print("Linux section")


class Bsd:
    def __init__(self,):
        print("BSD section")


class Unix:
    def __init__(self,):
        print("Unix section")
