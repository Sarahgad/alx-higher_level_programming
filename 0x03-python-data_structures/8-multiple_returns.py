#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = ()
    if sentence is None:
        tuple_a = (len(sentence), None)
    else:
        tuple_a = (len(sentence), sentence[0])
    return (tuple_a)
