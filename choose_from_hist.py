# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:51:19 2014

@author: cicek
"""
import random

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(histogram):
    """takes a histogram and returns a random value from the histogram, 
    chosen with probability in proportion to frequency"""
    keys=[]#key list. used to parse to random.choice method
    total=0
    for key in histogram:
        keys.append(key)
        total += histogram[key]
    key=random.choice(keys)
    return key,(float)(histogram[key])/total