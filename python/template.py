#!/usr/bin/env python3.7
from sys import exc_info
from traceback import print_exception

if __name__ == '__main__':
    try:
        pass
    except Exception:
        print(print_exception(*exc_info()))
