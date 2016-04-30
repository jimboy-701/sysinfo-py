
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

#    if i == 0:
#        pass
#    else:
#        cmdargs(sys.argv[0:])


def getPython():

    PY2 = sys.version[0] == '2'

    if PY2:
        input("You need Python version >= 3.4 to execute this script.")
        sys.exit([1])

    print(sys.executable)
    print(sys.version)


def getSpecs():

    print(platform.machine())
    print(platform.version())
    print(platform.platform())
    print(platform.uname())
    print(platform.system())
    print(platform.processor())
    print(platform.architecture())


# print("This is the HWInfo python script.\n")


getPython()
# getSpecs()

#Windows = Microsoft()
#print(Windows.message_string)

input()
