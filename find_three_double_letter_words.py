# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 23:54:04 2014

@author: Ozkan
"""

def find_three_double_consecutive(fin):
    """finds the words in a list that have three consecutive double letters"""
    numberOfFound = 0
    for line in fin:
        word = line.strip()
        l = len(word)
        i = 0
        count = 0
        while i<l-2:
            if word[i]==word[i+1]:
                count += 1
                i += 1 # skip the next letter
            else:
                count -= 1
            if count < 0:
                count = 0
            if count == 3:
                print 'word', numberOfFound, ' = ', word
                numberOfFound += 1
                break
            i += 1

if __name__ == "__main__":
    fin = open('words.txt')
    find_three_double_consecutive(fin)
    print "Finished"
        
            