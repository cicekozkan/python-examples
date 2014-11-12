# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 10:20:44 2014

@author: asus
"""

def is_after(t1,t2):
    """takes two Time objects, t1 and t2, and returns True if t1 
    follows t2 chronologically and False otherwise"""
    # Hint: convert time to seconds and compare
    second1 = (t1.hour)*60*60 + (t1.minute)*60 + t1.second
    second2 = (t2.hour)*60*60 + (t2.minute)*60 + t2.second
    return second2>second1