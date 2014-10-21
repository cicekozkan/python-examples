# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 22:00:36 2014

@author: Ozkan
"""

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def print_has_no_e():
    """print only the words that have no “e” and compute
    the percentage of the words in the list have no “e.”"""
    fin = open('words.txt')
    total = 0.0
    eNum = 0.0
    for line in fin:
        word = line.strip()
        total+=1
        if has_no_e(word) == True:
            print word
            eNum += 1
    percentage = (eNum/total)*100.0
    print 'percentage', percentage        
            
    