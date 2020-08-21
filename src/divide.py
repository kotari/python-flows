import sys
from time import sleep
import random
import os

def divide(x, y):
    rdm = random.randint(1,10)
    print('sleeping for - ' + str(rdm) + ' seconds.')
    sleep(rdm)
    result = int(x) / int(y)
    if (os.path.exists('/workspace/filedrop')):
        f = open("/workspace/filedrop/add.txt","r")
        x = f.read()
        print('x : ' + x)
        f = open("/workspace/filedrop/subtract.txt","r")
        y = f.read()
        print('y : ' + y)
        result = int(x) / int(y)
        f = open("/workspace/filedrop/divide.txt","w")
        f.write(str(result))
    return result


if __name__ == '__main__':
    print(divide(sys.argv[1], sys.argv[2]))