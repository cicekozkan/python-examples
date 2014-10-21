# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 23:23:28 2014

@author: Ozkan
"""

def is_sorted(t):
    """takes a list as a parameter and returns True
    if the list is sorted in ascending order and False otherwise."""
    i = 0
    for i in range(len(t) - 1):
        if t[i] > t[i+1]:
            return False
    return True