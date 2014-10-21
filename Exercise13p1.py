# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 16:01:06 2014

@author: cicek
"""
import string
wl=[]   # word list
fin=open('words.txt')
for line in fin:
    word = line.strip(string.whitespace+string.punctuation)
    wl.append(word.lower())
    