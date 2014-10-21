# -*- coding: utf-8 -*-
"""
Created on Wed Jun 04 00:34:46 2014

@author: Ozkan
"""

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
    
def is_palindrome(word):
    if ((len(word))==1 or len(word)==0):
        return True
    elif (len(word)>=2 and first(word)==last(word)):
        return is_palindrome(middle(word))
    else:
        return False
    