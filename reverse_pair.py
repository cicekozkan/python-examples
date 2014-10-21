# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 00:57:18 2014

@author: Ozkan
"""

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
    
def is_palindrome(word):
    if ((len(word))==1 or len(word)==0):
        return True
    elif (len(word)>=2 and first(word)==last(word)):
        return is_palindrome(middle(word))
    else:
        return False

def build_word_list():
    """reads the file words.txt and builds a list with one element
    per word"""
    t = []
    pin = open('words.txt')
    for line in pin:
        word = line.strip()
        t.append(word)
    return t

def reverse_pair(w1, w2):
    """returns True if w1 and w2 are a reverse pair"""
    if (len(w1) != len(w2)):    # if their lenght are not equal they can't 
        return False            # be a reverse pair
    if (w1 == w2[::-1]):
        return True
    else:
        return False
    #for i in range(len(w1)):
    #    if(w1[i] != w2[-1 + -1*i]):
    #        return False
    #return True

def find_reverse_pair_words(t):
    """returns a list that contains reverse pair words inside the list t
    Precondition: the list must be in sorted order
    """
    r = []  # create an ampty list
    n = t[:]    # copy the originial list
    for i in range(len(n)):
        if not is_palindrome(n[i]): # if a word is palindrome skip it
            for j in range(len(n)):
                if (reverse_pair(n[i],n[j])):
                    if (n[i] not in r):                
                        r.append(n[i])
                    if (n[j] not in r):
                        r.append(n[j])   
                    break;  # reverse pair has been found. break the loop
    return r
    
if __name__ == "__main__":
    t = build_word_list()
    #t = ['ula', 'totoli', 'gotoli', 'sikik', 'naber', 'alu']
    #reverse = find_reverse_pair_words(t)     
    
    

    