# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 17:36:27 2014

@author: cicek
"""

from read_dictionary import read_dictionary

if __name__ == '__main__':
    d = read_dictionary() # keys are the words, values are pronouncations
    for key in d:   # loop keys
        if len(key) == 5:
            if key[1:] in d and key[0]+key[2:] in d:
                if d[key] == d[key[1:]] and d[key] == d[key[0]+key[2:]]:
                    print key
        
        
    
