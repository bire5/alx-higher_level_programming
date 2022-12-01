#!/usr/bin/python3

def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= ord('a') and ord(str[x]) <= ord('z'):
            upp = ord(str[x]) + (ord('A') - ord('a'))
        else:
            upp = ord(str[x])
            print("{}".format(chr(upp)), end='')
    print()
