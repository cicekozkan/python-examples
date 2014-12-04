# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 14:11:08 2014

@author: ocicek
"""
import random

class Card(object):
    """Represents a standard playing card.
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """
    def __init__(self, suit=0, rank=2):
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
        t2 = other.suit, other.rank
        return cmp(t1,t2)
        
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
        
class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label