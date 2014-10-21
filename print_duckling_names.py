# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 09:26:41 2014

@author: Ozkan
"""

def print_duckling_names():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print letter + 'u' + suffix
        else:
            print letter + suffix