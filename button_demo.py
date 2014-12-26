# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 09:27:42 2014

@author: ocicek
"""

from swampy.Gui import *
g=Gui()
g.title('Gui')

def display_message():
    g.la(text="Nice job!")

def create_second_button():
    g.bu(text='Now press me', command=display_message)

g.bu(text='Press me',command=create_second_button)

g.mainloop()