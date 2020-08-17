import sys

def divide(x, y):
    return int(x) / int(y)


if __name__ == '__main__':
    print(sys.argv)
    print(divide(sys.argv[1], sys.argv[2]))