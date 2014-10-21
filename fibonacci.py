# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 14:31:59 2014

@author: asus
"""
import time

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memo(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
    
if __name__ == "__main__":
    known = {0:0, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720}
    start_time = time.time()
    arg = 35
    f = fibonacci(arg)
    elapsed_time = time.time() - start_time
    print 'fibonacci {0} without memo returned in {1} seconds'.format(arg,elapsed_time) 
    start_time = time.time()
    f = fibonacci_memo(arg)
    elapsed_time = time.time() - start_time
    print 'fibonacci {0} with memo returned in {1} seconds'.format(arg,elapsed_time)