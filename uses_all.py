# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 23:08:38 2014

@author: Ozkan
"""

def uses_all(word, string):
    """takes a word and a string of required letters,
    and that returns True if the word uses all the required 
    letters at least once"""
    for letter in string:
        if (letter in word) == False:
            return False
    return True

if __name__ == "__main__":
    fin = open('words.txt')
    number= 0
    for line in fin:
        word = line.strip()
        if uses_all(word, "aeiouy") == True:
            print word
            number += 1
    print 'number of words contain all the vowels and \'y\':', number
        