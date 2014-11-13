# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 17:54:34 2014

@author: ocicek
"""
from Time import *

def mul_time(time, number):
    """takes a Time object and a number and returns
    a new Time object that contains the product of the original 
    Time and the number"""
    # check data structure invariants
    assert valid_time(time) 
    assert number > 0
    return int_to_time(time_to_int(time)*number)
    
    
    
    