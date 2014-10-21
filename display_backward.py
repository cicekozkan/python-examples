# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 09:20:03 2014

@author: Ozkan
"""

def display_backward(s):
    """displays the input string's letters backward"""
    i=len(s)-1
    while i>=0:
        print s[i]
        i-=1
def display_backwards2(s):
   """displays the input string's letters backward"""
   return s[::-1]
        