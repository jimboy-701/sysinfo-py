#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import platform
from typing import List

errors: List[str] = []
try: import psutil
except Exception as e: errors.append(f'{e}')

VERSION: str = "0.5.0"
SYSTEM: str

if "windows" in sys.platform: SYSTEM = "Windows"
elif "linux" in sys.platform: SYSTEM = "Linux"
elif "bsd" in sys.platform: SYSTEM = "BSD"
elif "darwin" in sys.platform: SYSTEM = "MacOS"
elif "sunos" in sys.platform: SYSTEM = "SunOS"
else: SYSTEM = "Other"

if errors:
    print("ERROR!")
    for error in errors:
        print(error)
    if SYSTEM == "Other":
        print("\nUnsupported platform!\n")
    else:
        print("\nInstall required modules!\n")
    quit(1)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if not arg in ["-c", "--cores", "-v", "--version", "-h", "--help"]:
            print(f'Unrecognized argument: {arg}\n'
                  f'Use argument -h or --help for help')
            raise SystemExit(1)

if "-h" in sys.argv or "--help" in sys.argv:
    print(f'USAGE: {sys.argv[0]} [argument]\n\n'
          f'Arguments:\n'
          f'    -c, --cores           Display the number of cpu cores available\n'
          f'    -v, --version         Show version info\n'
          f'    -h, --help            Show this help message\n')
    raise SystemExit(0)

elif "-v" in sys.argv or "--version" in sys.argv:
    print(f'hwinfo version: {VERSION}\n'
            f'psutil version: {".".join(str(x) for x in psutil.version_info)}')
    raise SystemExit(0)

if "-c" or "--cores" in sys.argv:
    print("Number of cores in system:", psutil.cpu_count())
    raise SystemExit(0)


def getPython():

    print(sys.executable)
    print(sys.version)


def getSpecs():

    p = platform.uname()
    a = platform.architecture()

    # uname() is a namedtuple and [1] is positional for the "node" or hostname
    # attribute
    print("hostname:", p[1])
    print("Platform:", p[0], p[2])
    print("Bits:", a[0])
    print("Arch:", p[4])

    # [0]system='Windows', [1]node='blackchrome', [2]release='8', [3]version='6.2.9200'
    # [4]machine='AMD64'
    # [5]processor='Intel64 Family 6 Model 23 Stepping 10, GenuineIntel'

    # print(platform.machine())
    # print(platform.version())
    # print(platform.platform())
    # print(platform.system())
    # print(platform.processor())
    # print(platform.architecture())


class Linux:
    def __init__(self,):

        self.message_string = "This is a Linux machine!\n"


class Windows:
    def __init__(self,):

        self.message_string = "This is a Microsoft Windows machine!\n"


getPython()
getSpecs()

if 'Windows' in SYSTEM:
    Windows = Microsoft()
    print(Windows.message_string)

elif 'Linux' in SYSTEM:
    Gnu = Linux()
    print(Gnu.message_string)

elif 'BSD' in SYSTEM:
    BsdUnix = Bsd()
    print(BsdUnix.message_string)

elif 'SunOS' in SYSTEM:
    Sun = Solaris()
    print(Sun.message_string)

elif 'Darwin' in SYSTEM:
    Mac = OSX()
    print(Mac.message_string)

elif 'Android' in SYSTEM:
    Droid = Android()
    print(Droid.message_string)

elif 'iPhone' in SYSTEM:
    Apple = Iphone()
    print(Apple.message_string)

os._exit(0)
