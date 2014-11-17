# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:51:02 2014

@author: ocicek
"""
from Deck import Deck

class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label