# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 23:35:08 2014

@author: Ozkan
"""

def is_anagram(word1, word2):
    """takes two strings and returns True if they are anagrams"""
    for letter in word1:
        if not letter in word2:
            return False
    return True