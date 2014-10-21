# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 19:39:20 2014

@author: ozkan
"""

def writeTxtToDict():
    """this function writes the words in the words.tx text file to a 
    dictionary to be able to search words faster. in operator uses
    hash table methods and finds the desired word in O(1)"""
    fin = open('words.txt')
    d = {}
    for line in fin:
        word = line.strip()
        d[word] = ""
    return d
