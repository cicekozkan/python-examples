# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 15:50:11 2014

@author: asus
"""
from random import random

def sort_by_length(words):
    """sorts a list of words from longest to shortest"""
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res
    
def sort_by_length_random(words):
    """Sort a list of words in reverse order by length.

    This is the solution to the exercise.  It is unstable in the
    sense that if two words have the same length, their order in
    the output list is random.

    It works by extending the list of tuples with a column of
    random numbers; when there is a tie in the first column,
    the random column determines the output order.

    words: list of strings

    Returns: list of strings
    """
    t = []
    for word in words:
       t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res