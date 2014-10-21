# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 21:39:16 2014

@author: ozkan
"""

def print_hist(d):
    """print the keys and their values in alphabetical order"""
    k=d.keys()
    k.sort()
    i=0
    for i in range(len(k)):
        print k[i], d[k[i]]