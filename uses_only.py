# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 22:43:22 2014

@author: Ozkan
"""

def uses_only(word, string):
    """takes a word and a string of letters, and
    that returns True if the word contains only letters 
    in the list."""
    for letter in word:
        if (letter in string) == False:
            return False
    return True