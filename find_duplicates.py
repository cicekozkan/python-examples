# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:25:10 2014

@author: cicek
"""

import os

def find_duplicates(dirname, suffixes):
    """searches a directory and all of its subdirectories, 
    recursively, and returns a list of complete paths for all files
    with a given suffix (like .mp3).
    dirname: root directory
    suffixes: tuple that contains the suffixes to search for"""
    res=[]
    for root, dirs, files in os.walk(dirname):
        for filename in files:
                for suffix in suffixes:
                    if filename.endswith(suffix):
                        res.append(os.path.join(root, filename))
    return res