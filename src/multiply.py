import sys

def multiply(x, y):
    return int(x) * int(y)


if __name__ == '__main__':
    print(multiply(sys.argv[1], sys.argv[2]))