
# http://www.python-course.eu/sys_module.php

import sys
import platform
from OSAnalysis import Microsoft


def cmdargs(*args):
    '''
    Let's try to expand this by mapping arguments to variables
    that can be stored in a dictionary... '''
    arglist = list(args)
    print(arglist)


if (len(sys.argv)) > 0:
    '''
    In sys.argv[0], that 0 outputs the script name,
    anything after that will be command line arguments. '''
    for i in range(1, (len(sys.argv))):
        cmdargs(sys.argv[i])


def getPython():
    PY2 = sys.version[0] == '2'

    if PY2:
        input("You need Python version >= 3.4 to execute this script.")
        sys.exit([1])

    print(sys.executable)
    print(sys.version)


def getSpecs():

    p = platform.uname()
    a = platform.architecture()
    # uname() is a namedtuple and [1] is positional for the "node" or hostname
    # attribute
    print("hostname:", p[1])
    print("OS:", p[0], p[2], a[0])

    # [0]system='Windows', [1]node='blackchrome', [2]release='8', [3]version='6.2.9200'
    # [4]machine='AMD64'
    # [5]processor='Intel64 Family 6 Model 23 Stepping 10, GenuineIntel'

    print(platform.machine())
    print(platform.version())
    print(platform.platform())
    print(platform.system())
    print(platform.processor())
    print(platform.architecture())


getPython()
getSpecs()

if platform.system() == 'Windows':
    Windows = Microsoft()
    print(Windows.message_string)

input()
