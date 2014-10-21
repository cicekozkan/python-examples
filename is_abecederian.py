# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 23:20:36 2014

@author: Ozkan
"""

def is_abecederian(word):
    """returns True if the letters in a word
    appear in alphabetical order (double letters are ok)"""
    index = 0    
    for letter in word:
        if letter.isupper() == True:
                letter = letter.lower()
        if index != 0:
            if letter < word[index-1].lower():
                return False
        index += 1
    return True

if __name__ == "__main__":
    number = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if (is_abecederian(word)):
            number += 1
    print 'number of abecederian words is', number
        