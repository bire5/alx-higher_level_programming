#!/usr/bin/python3
#File: 5-no_c.py

def no_c(my_string):
    new_string = [x for x in my_string if x != 'c' and x != 'C']
    return("".join(new_string))

