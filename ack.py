# -*- coding: utf-8 -*-
"""
Created on Sat May 31 21:35:33 2014

@author: asus
"""

def ack(m,n):
    """ack(m,n) evaluates Ackermann's function"""
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
    
    