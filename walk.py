# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 17:39:19 2014

@author: cicek
"""
import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)