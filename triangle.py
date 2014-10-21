# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 18:18:44 2014

@author: cicek
"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    
def equilateral(t, a, l1):
    """draws a equilateral triangle whose peak angle is a
    with each equal side length is l
    t: turtle
    a: angle (in degrees)
    l: lenght of each side"""
    fd(t,l1)
    lt(t,(180+a)/2.0)
    aR = a/360.0*2*pi
    l2 = l1*sin(aR)/sin((pi-aR)/2)
    fd(t,l2) 
    lt(t,(180+a)/2.0)    
    fd(t,l1)
    lt(t,180-a)
    
def polygon(t, n, l):
    """draws a polygon that has n triangles
    each triangle will have two equal sides whose
    length is l"""
    a=360.0/n
    for i in range(n):
        equilateral(t, a, l)
        lt(t, a)
       
        
if __name__ == "__main__":
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001  
    
    #equilateral(bob, 80, 100)
    polygon(bob, 12, 100)
    wait_for_user()