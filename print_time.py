# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 10:17:39 2014

@author: asus
"""

def print_time(time):
    """takes a Time object and prints it in the form hour:minute:second"""
    print '%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second)