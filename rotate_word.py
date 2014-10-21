# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 00:28:33 2014

@author: Ozkan
"""

def rotate_letter(char, shift):
    """To rotate a letter means to shift it through the alphabet, 
    wrapping around to the beginning if necessary, so ’A’ shifted 
    by 3 is ’D’ and ’Z’ shifted by 1 is ’A’."""
    o = ord(char)  
    if char.isupper():
        omax = ord('Z')
        omin = ord('A')
    else:
        omax = ord('z')
        omin = ord('a')
    o+=shift
    if o>omax:
        o-=26
    elif o<omin:
        o+=26
    return chr(o)
        
def rotate_word(word, shift):
    new_word = ''
    for c in word:
        new_word += rotate_letter(c,shift)
    return new_word
             
    
        
        