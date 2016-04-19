
import sys
import platform
from OSAnalysis import Microsoft


for i in range(len(sys.argv)):
    if i == 0:
        pass
    else:
        print(i, sys.argv[i])


def getPython():

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


print("This is the HWInfo python script.\n")


getPython()
# getSpecs()

Windows = Microsoft()
print(Windows.message_string)

input()
