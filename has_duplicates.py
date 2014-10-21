# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 16:06:12 2014

@author: asus
"""
def has_duplicate(t):
    """takes a list and returns True if there is any
    element that appears more than once"""
    n = t[:]
    for i in range(len(t)):
        n.pop(0)    # remove the element
        if t[i] in n:
            return True        
    return False
    
def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print has_duplicates(t)
    t.append(1)
    print has_duplicates(t)

    t = [1, 2, 3]
    print has_duplicates2(t)
    t.append(1)
    print has_duplicates2(t)
        

