# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:37:31 2014

@author: Ozkan
"""

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(t):
    if not isinstance(t,list):
        print 'The input must be a list'
        return None
    res = []
    for s in t:
        res.append(capitalize_all(s))
    return res
            