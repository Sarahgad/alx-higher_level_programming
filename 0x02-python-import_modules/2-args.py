#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) > 2:
        print("{0:d} arguments:".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{0:d} argument:".format(len(argv) - 1))
    else:
        print("0 arguments.")

    for i in range(1, len(argv)):
        print("{0:d}: {1}".format(i, argv[i]))
