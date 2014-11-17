# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:46:43 2014

@author: ocicek
"""

def find_defining_class(obj, meth_name):
    """takes an object and a method name (as a string) and returns 
    the class that provides the definition of the method"""
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty