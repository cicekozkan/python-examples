# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:17:45 2014

@author: cicek
"""

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print linecount('wc.py')