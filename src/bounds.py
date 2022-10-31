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

    for i in range(len(x)): 
        if v <= x[i]:
            return i 

    return len(x)  # FIXME: Obviously the answer isn't always 0

x = [1,2,3,4,5,6]
v = 8

def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    value = 0
    for i in range(len(x)): 
        if v >= x[i]:
            value = i
    if value != 0: 
        return value 
    else: 
        return 0

    # FIXME: Obviously the answer isn't always 0

print(upper_bound(x,v))