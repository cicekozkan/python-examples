# -*- coding: utf-8 -*-
"""
Created on Wed Jun 04 01:17:07 2014

@author: Ozkan
"""

def gcd(a,b):
    """returns a and b's greatest common divisor"""
    if(a==b):
        return a
    elif (a>b):
        r=a%b
    else:
        r=b%a
        
    if(b==0):
        return a
    
    if r==0 and a>b:
        return b
    elif r==0 and b>a:
        return a
    else:
        return gcd(b,r)
    
   
    