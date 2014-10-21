# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 20:07:10 2014

@author: cicek
"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
    
def koch_line(t, l):
    """koch draws a koch curve
    t: turtle
    l: length"""
    if l>=3:
        fd(t, l/3)
        lt(t,60)
        fd(t, l/3)
        rt(t,120)
        fd(t, l/3)
        lt(t,60)
        fd(t, l/3)
    else:
        fd(t, l)
def koch_segment(t,l):
    koch_line(t, l)
    lt(bob,60)
    koch_line(t, l)
    rt(bob,120)
    koch_line(t, l)
    lt(bob,60)
    koch_line(t, l)
def koch(t,l):
    koch_segment(t, l)
    lt(bob,60)
    koch_segment(t, l)
    rt(bob,120)
    koch_segment(t, l)
    lt(bob,60)
    koch_segment(t, l)
def snowflake(t,l):
    koch(t, l)
    lt(bob,60)
    koch(t, l)
    rt(bob,120)
    koch(t, l)
    lt(bob,60)
    koch(t, l)

if __name__ == "__main__":
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001
    
    snowflake(bob,20) 
    rt(bob,120)
    snowflake(bob,20) 
    rt(bob,120)
    snowflake(bob,20) 
    wait_for_user()