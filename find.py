# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 11:05:13 2014

@author: Ozkan
"""

def find(word,letter,index):
    """finds the index of letter in word, starts searching
    from index"""
    i=0
    s=word[index:]
    while i<len(s):
        if s[i]==letter:
            return i+index
        i+=1
    return -1