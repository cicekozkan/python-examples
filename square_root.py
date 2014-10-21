# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 20:53:02 2014

@author: Ozkan
"""
from math import sqrt

def square_root(a):
    e=a/2.0
    while True:
        #print e
        s=(e+a/e)/2.0
        if (abs(e-s)<0.000000001):
            break
        e=s
    return s
        
def test_square_root(a):
    sr1=square_root(a)
    sr2=sqrt(a)
    diff=abs(sr1-sr2)
    print a, sr1, sr2, diff
    
    