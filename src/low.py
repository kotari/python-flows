import sys
from time import sleep
import random
import os

def low():
    rdm = random.randint(1,10)
    print('sleeping for - ' + str(rdm) + ' seconds.')
    sleep(rdm)
    result = "multiplication wins"
    if (os.path.exists('/workspace/filedrop')):
        f = open("/workspace/filedrop/divide.txt","r")
        x = f.read()
        print(x)
        f = open("/workspace/filedrop/multiply.txt","r")
        y = f.read()
        print(y)
        if x<=y:
            result = "division wins"
        f = open("/workspace/filedrop/result.txt","w")
        f.write(str(result))
    return result


if __name__ == '__main__':
    print(sys.argv)
    print(low())