
import os
import sys
import platform
from OSAnalysis import Microsoft


def getPython():

    print(platform.python_version())


def getSpecs():

    print(platform.machine())
    print(platform.version())
    print(platform.platform())
    print(platform.uname())
    print(platform.system())
    print(platform.processor())
    print(platform.architecture())


print("This is the HWInfo python script.\n")


getPython()
getSpecs()

Windows = Microsoft()
print(Windows.message_string)

input()
