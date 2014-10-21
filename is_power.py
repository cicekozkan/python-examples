# -*- coding: utf-8 -*-
"""
Created on Wed Jun 04 01:06:50 2014

@author: asus
"""

def is_power(a,b):
    """returns True if a is a power of b"""
    if (a%b==0 and a != b):
        return is_power(a/b,b)
    elif (a==b):
        return True
    elif (a==1):
        return True
    elif (a%b > 0):
        return False