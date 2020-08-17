import sys

def multiply(x, y):
    return int(x) * int(y)


if __name__ == '__main__':
    print(sys.argv)
    print(multiply(sys.argv[1], sys.argv[2]))