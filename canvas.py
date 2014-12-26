# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 09:49:53 2014

@author: ocicek
"""

from swampy.Gui import *
g=Gui()
g.title('Gui')
i_glb = 0

canvas = g.ca(width=100, height=100)
canvas.config(bg='white')

def create_circle():
    global i_glb
    circle = canvas.circle([i_glb*30,0], 15, fill='red')
    i_glb += 1

g.bu(text='Press me', command=create_circle)
g.mainloop()
