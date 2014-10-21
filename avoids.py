# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 22:24:11 2014

@author: Ozkan
"""

def avoids(word, string):
    """takes a word and a string of forbidden letters,
    and that returns True if the word doesn’t use any
    of the forbidden letters."""
    result = 0
    for letter in string:
        result += (letter in word)
    if result == 0:
        return True
    else:
        return False
        
if __name__ == "__main__":
    fin = open('words.txt')
    string = raw_input("Enter the string of forbidden letters\n")
    number = 0
    for line in fin:
        word = line.strip()
        if (avoids(word, string) == True):
            number += 1
    print 'number of words that don\'t contain those words:', number
    
    