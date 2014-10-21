# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 11:48:03 2014

@author: cicek
"""
from bisect import bisect_left

def make_word_list():
    word_list = []
    pin = open('words.txt')
    for line in pin:
        word = line.strip()
        word_list.append(word)
    return word_list       

def bisect_local(t, word):
    """that takes a sorted list and a target value and returns the index of
    the value in the list, if it’s there, or None if it’s not."""
    i = bisect_left(t, word)
    if i != len(t) and t[i] == word:
        return i
    else:
        return None
        
if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in ['alien', 'allen', 'ozkan']:
        print word, 'in list', bisect_local(word_list, word)
    