#!/usr/bin/python3

for x in range(0, 100):
    if (x % 10) > (x // 10) and x != 89:
        print("{:02d}, ".format(x), end='')
print("89")
