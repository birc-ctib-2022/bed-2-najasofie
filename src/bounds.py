"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    
    low = 0
    up = len(x)
    while low < up:
        g = (low + up) // 2
        if x[g] < v:
            low = g + 1
        else:
            up = g
    return low




    #for i in range(len(x)): 
    #    if v <= x[i]:
    #        return i 

    #return len(x)  # FIXME: Obviously the answer isn't always 0



def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    return lower_bound(x, v+1)

    # FIXME: Obviously the answer isn't always 0

