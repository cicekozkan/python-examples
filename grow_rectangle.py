# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 23:40:07 2014

@author: asus
"""

def grow_rectangle(rect, dwidth, dheight):
    """takes a Rectangle object and two numbers, dwidth and dheight, 
    and adds the numbers to the width and height of the rectangle"""
    rect.width += dwidth
    rect.height += dheight  