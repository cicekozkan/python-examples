# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 23:49:05 2014

@author: Ozkan
"""
import numpy as np

def has_duplicate(t):
    """takes a list and returns True if there is any
    element that appears more than once"""
    n = t[:]
    for i in range(len(t)):
        n.pop(0)    # remove the element
        if t[i] in n:
            return True        
    return False
        
if __name__ == "__main__":
    ages = []
    hit = 0.0
    numSimulation = 10000
    for j in range(numSimulation):        
        for i in range(23):
            age = np.random.randint(1,365)
            ages.append(age)
        if has_duplicate(ages):
            hit += 1
    probability = hit/numSimulation
    print 'The probability is', probability*100, '%' 