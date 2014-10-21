# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 20:57:21 2014

@author: ozkan
"""

def histogram(s):
    """Dictionaries have a method called get that takes a key and a default 
    value. If the key appears in the dictionary, get returns the 
    corresponding value; otherwise it returns the default value.
    Use get to write histogram"""
    d = {}    
    for c in s:
        d[c] = d.get(c,0) + 1
    return d