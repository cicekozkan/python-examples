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
            
def walk2(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print os.path.join(root, filename)