import sys
from time import sleep
import random
import os

def multiply(x, y):
    rdm = random.randint(1,10)
    print('sleeping for - ' + str(rdm) + ' seconds.')
    sleep(rdm)
    result = int(x) * int(y)
    if (os.path.exists('/workspace/filedrop')):
        f = open("/workspace/filedrop/add.txt","r")
        x = f.read()
        print(x)
        f = open("/workspace/filedrop/subtract.txt","r")
        y = f.read()
        print(y)
        result = int(x) * int(y)

    return result


if __name__ == '__main__':
    print(sys.argv)
    print(multiply(sys.argv[1], sys.argv[2]))