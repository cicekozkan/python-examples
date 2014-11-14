# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 22:47:15 2014

@author: Ozkan
"""

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%d,%d)'%(self.x, self.y)
    def __add__(self,other):
        assert isinstance(self,Point) and \
        (isinstance(other,Point) or isinstance(other,tuple)),\
        'the argument must be either a Point object or a tuple'
        res = Point()
        if isinstance(other,Point):
            res.x = self.x + other.x
            res.y = self.y + other.y
        elif isinstance(other,tuple):
            res.x = self.x + other[0]
            res.y = self.y + other[1]
        return res
    def __radd__(self,other):
        return self.__add__(other)
    def print_attributes(self):
        for attr in self.__dict__:
            print attr, getattr(self,attr)