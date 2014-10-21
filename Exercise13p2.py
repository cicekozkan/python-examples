# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:05:20 2014

@author: cicek
"""

import string
wl=[]   # word list
fin=open('The Brothers Karamazov.pdf')
i=0
for page in fin:
    word = page.strip(string.whitespace+string.punctuation)
    wl.append(word)
    i=i+1
    if i == 500:
        break
    