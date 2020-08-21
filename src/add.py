import sys
from time import sleep
import random
import os

def add(x, y):
    rdm = random.randint(1,10)
    print('sleeping for - ' + str(rdm) + ' seconds.')
    sleep(rdm)
    result = int(x) + int(y)
    if (os.path.exists('/workspace/filedrop')):
        f = open("/workspace/filedrop/add.txt","w+")
        f.write(str(result))
    return result


if __name__ == '__main__':
    print(sys.argv)
    print(add(sys.argv[1], sys.argv[2]))