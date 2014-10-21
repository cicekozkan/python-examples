# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 17:19:19 2014

@author: asus
"""

def most_frequent(s):
    """takes a string and prints the letters
    in decreasing order of frequency"""
    #1) create a dictionary with letters as keys and freq as values
    #2) traverse the input string and increase the frequency of letter
    #3) call items method to dictionary and get a list of tuples
    #4) travers the list of tuples and create a new list of tuples whose
    #    first element is frequency and the second element is letter
    #5) sort that list
    #6) traverse and print letters
    l=[]
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        l.append((letter,0))
    d=dict(l)
    for letter in s:
        d[letter] = d[letter] + +1
    lot=d.items()
    lot2=[]
    for letter,freq in lot:
        lot2.append((freq,letter))
    lot2.sort()
    for freq,letter in lot2:
        if freq !=0:
            print letter
        
    
    
    
    
    