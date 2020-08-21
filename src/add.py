import sys
from time import sleep
import random
import os

def add(x, y):
    rdm = random.randint(1,10)
    print('sleeping for - ' + str(rdm) + ' seconds.')
    sleep(rdm)
    sum = int(x) + int(y)
    arr = os.listdir('/workspace')
    print(arr)
    f = open("/workspace/sum.txt","w+")
    f.write(str(sum))
    os.environ['results.sum'] = str(sum)
    return sum


if __name__ == '__main__':
    print(sys.argv)
    print(add(sys.argv[1], sys.argv[2]))