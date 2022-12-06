#!/usr/bin/python3
#File: 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + tuple_c
    if len(tuple_b) < 2:
        tuple_b = tuple_b + tuple_c   
    result1 = tuple_a[0] + tuple_b[0]
    result2 = tuple_a[1] + tuple_b[1]
    tuple_d = (result1, result2)
    return(tuple_d)
