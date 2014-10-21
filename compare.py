# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:43:12 2014

@author: asus
"""

def compare(x,y):
    if x==y:
        return 0
    elif x<y:
        return -1
    else:
        return 1
        
if __name__ == "__main__":
    
    a=compare(1,1)
    b=compare(2,1)
    c=compare(1,2)