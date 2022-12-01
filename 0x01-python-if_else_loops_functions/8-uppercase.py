#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            upp = ord(str[i]) + (ord('A') - ord('a'))
        else:
            upp = ord(str[i])
            print("{}".format(chr(upp)), end='')
    print()
