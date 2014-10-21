# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 22:30:06 2014

@author: ozkan
"""

def invert_dict(d):
    """inverts the dictionary d"""
    inverse = dict()
    for key in d:
        val = d[key]    # get the value
        # setdefault method will return the value  
        # that key maps to; and if the key-value pair
        # is not present it will add them to the dictionary     
        if inverse.setdefault(val,[key]) != [key]:   
           inverse.setdefault(val,[key]).append(key) 
    return inverse
