# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 19:55:52 2014

@author: cicek
"""

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return True
        else:
            return False
            
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag