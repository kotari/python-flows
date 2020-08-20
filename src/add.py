import sys
from time import sleep
import random

def add(x, y):
    rdm = random.randint(1,10)
    print('sleeping for - ' + str(rdm) + ' seconds.')
    sleep(rdm)
    return int(x) + int(y)


if __name__ == '__main__':
    print(sys.argv)
    print(add(sys.argv[1], sys.argv[2]))