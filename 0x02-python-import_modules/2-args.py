#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1:
        print("{0:d} arguments:".format(len(argv) -1))
        for i in range(1, len(argv)):
            print("{0:d}: {1}".format(i, argv[i]))
    else:
        print("0 arguments.")
