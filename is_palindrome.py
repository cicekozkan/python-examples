# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 19:50:22 2014

@author: cicek
"""

def is_palindrome(str):
    if (str[::-1]==str):
        return True
    else:
        return False