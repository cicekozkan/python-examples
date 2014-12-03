# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:01:34 2014

@author: ocicek
"""
from Card import Card
import random

class Deck(object):
    """Represents a deck of playing cards.
    Attributes:
      cards: list of Card objects.
    """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)
    def add_card(self, card):
        self.cards.append(card)
    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    def deal_hands(self, num_hands, num_cards_per_hand):
        """creates new Hand objects, deals the appropriate
        number of cards per hand, and returns a list of Hand objects"""
        res = []
        for h in range(num_hands):
            hand_name = 'Hand%d'%h
            hand = Hand(hand_name)
            for c in range(num_cards_per_hand):  
                self.shuffle()
                hand.add_card(self.pop_card())
            res.append(hand)
        return res
            