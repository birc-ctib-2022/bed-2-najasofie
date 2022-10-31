"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    
    #low = 0 
    #up = len(x) 

    #while True: 
    #    g = (low + up)//2 
    #    if v <= x[g]:
    #        up = x[g]
    #    else: 
    #        low = x[g]
    #    if x[g] == v: 
    #            return x[g]

    for i in x: 
        if v <= i:
            return i 

    return len(x)  # FIXME: Obviously the answer isn't always 0


def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    """

    for i in x: 
        if v >= i:
            value = i
        return value
    return len(x)
    # FIXME: Obviously the answer isn't always 0
