# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 19:24:07 2014

@author: cicek
"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)
    
def flower(t, l, r=100):
    """Draws a flower with the given number of leaves
    t: Turtle
    l: number of leaves
    r: radius
    """
    for i in range(l):
        arcAngle = 360/l
        arc(t, r, arcAngle)
        lt(t,180-arcAngle)
        arc(t, r, arcAngle)
        lt(t, 180 - 2*arcAngle)    

if __name__ == '__main__':
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001    
    
    flower(bob, 12, 400)
    flower(bob, 24, 400)    
    wait_for_user()