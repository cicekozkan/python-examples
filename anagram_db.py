# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:57:31 2014

@author: cicek
"""

from anagram_sets import all_anagrams
import shelve

def store_anagrams(s,d):
    """stores the anagram dictionary in a shelf
    s: shelf
    d: dictionary"""
    for key in d.keys():
        s[key] = d[key]

def read_anagrams(s,key):
    """looks up a word and returns a list of its anagrams
    s: shelf
    key: look up word"""
    t=s[key]
    return t
    
    
if __name__ == "__main__":
    d=all_anagrams('words.txt')
    s=shelve.open('dictShelf')
    store_anagrams(s,d)
    
    
    
    