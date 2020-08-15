import sys

def subtract(x, y):
    return int(x) - int(y)


if __name__ == '__main__':
    print(subtract(sys.argv[1], sys.argv[2]))