#!/usr/bin/python3
def printalphabet():
    for i in range(ord('A'),ord('Z')+1):
        print("{0}".format(chr(i)),end ="")
    print()
