import sys
from time import sleep
import random
import os

def subtract(x, y):
    rdm = random.randint(1,10)
    print('sleeping for - ' + str(rdm) + ' seconds.')
    sleep(rdm)
    result = int(x) - int(y)
    if (os.path.exists('/workspace/filedrop')):
        arr = os.listdir('/workspace/filedrop')
        print(arr)
        f = open("/workspace/filedrop/subtract.txt","w+")
        f.write(str(result))
    return result


if __name__ == '__main__':
    print(sys.argv)
    print(subtract(sys.argv[1], sys.argv[2]))