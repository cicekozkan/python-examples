# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 22:25:10 2014

@author: asus
"""
import string
def ex_13_1():
    """reads a file, breaks each line into words, strips whitespace and
    punctuation from the words, and converts them to lowercase."""
    fin=open('words.txt')
    for line in fin:
        word=line.strip(string.punctuation+string.whitespace).lower()
        print word