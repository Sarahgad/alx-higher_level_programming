#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    if len(tuple_a) > 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    elif len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    for i in range(2):
        new_tuple += (tuple_a[i] + tuple_b[i],)
    return (new_tuple)
