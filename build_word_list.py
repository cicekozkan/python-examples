# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 20:11:37 2014

@author: cicek
"""
from time import time
def build_word_list1():
    """reads the file words.txt and builds a list with one element
    per word"""
    startTime = time()
    t = []
    pin = open('words.txt')
    for line in pin:
        word = line.strip()
        t.append(word)
    elapsedTime = time() - startTime
    print 'Elapsed time = ', elapsedTime
    return elapsedTime

def build_word_list2():
    """reads the file words.txt and builds a list with one element
    per word"""
    startTime = time()
    t = []
    pin = open('words.txt')
    for line in pin:
        word = line.strip()
        t = t + [word]
    elapsedTime = time() - startTime
    print 'Elapsed time = ', elapsedTime
    return elapsedTime