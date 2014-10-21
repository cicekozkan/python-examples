# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 21:48:56 2014

@author: OZkan  
"""

def eval_loop():
    while True:
        i=raw_input('->')
        if i=='done':
            break
        e=eval(i)
        #print e
    return e