# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 23:43:56 2014

@author: asus
"""
from copy import deepcopy
def move_rectangle(rect, dx, dy):
    """takes a Rectangle and two numbers named dx and dy and changes 
    the location of the rectangle by adding dx to the x coordinate of
    corner and adding dy to the y coordinate of corner"""
    rect.corner.x += dx
    rect.corner.y += dy
    
def move_rectangle2(rect, dx, dy):
    """takes a Rectangle and two numbers named dx and dy. Returns a new
    rectangle whose location is shifted by (dx,dy)"""
    res = deepcopy(rect)
    move_rectangle(res,dx,dy)
    return res