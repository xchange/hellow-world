import sys


def hello():
    message = "Hello World!"
    print(message, end='\n', file=sys.stdout)

if __name__ == '__main__':
    hello()
