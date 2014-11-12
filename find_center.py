# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 23:28:39 2014

@author: asus
"""
from Point import Point
def find_center(rect):
    """takes a Rectangle as an argument and returns a Point 
    that contains the coordinates of the center of the Rectangle"""
    p=Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p