# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:43:58 2014

@author: cicek
"""
import string
from math import log10

def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = file(filename)
    
    for line in fp:
        process_line(line, hist)
    return hist
    
def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1
        
def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency."""
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t

if __name__ == "__main__":
    word_hist = process_file('emma.txt')
    rank_list = most_common(word_hist)
    rank=1
    for frequency,word in rank_list:
        print word, log10(frequency), log10(rank)
        rank = rank + 1
        if rank == 10:
            break
        