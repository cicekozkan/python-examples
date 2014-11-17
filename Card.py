# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 14:11:08 2014

@author: ocicek
"""

class Card(object):
    """Represents a standard playing card"""
    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = self.suit, self.rank
        return cmp(t1,t2)