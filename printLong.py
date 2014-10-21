# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 21:13:35 2014

@author: Ozkan
"""

def printLong():
    fin = open('words.txt')
    #line = fin.readline()
    for line in fin:
        #line = fin.readline()
        word = line.strip()
        if len(word) > 20:
            print word
    