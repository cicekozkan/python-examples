"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
    
    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """      
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
    
    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
        Note that this works correctly for hands with more than 2 cards.        
        """
        if len(self.cards) < 2:
            raise ValueError ('Hand must have at least 2 cards')
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    
    def has_two_pair(self):
        """Returns True if the hand has two pairs, False otherwise.
        Note that this works correctly for hands with more than 4 cards.        
        """    
        if len(self.cards) < 4:
            raise ValueError ('Hand must have at least 4 cards')
        pair = 0
        for val in self.ranks.values():
            if val >= 4:
                return True
            if val >= 2:
                pair += 1
            if pair == 2:
                return True
        return False
        
    def has_three_of_a_kind(self):
        """Returns True if the hand has three cards with the same rank, False otherwise.
        Note that this works correctly for hands with more than 3 cards.        
        """ 
        if len(self.cards) < 3:
            raise ValueError ('Hand must have at least 3 cards')  
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    
    def has_straight(self):
        """Returns True if five cards with ranks in sequence, False otherwise.
        Note that this works correctly for hands with more than 5 cards.        
        """
        num_in_seq = 0
        if len(self.cards) < 5:
            raise ValueError ('Hand must have at least 5 cards') 
        rank_list = []
        for card in self.cards:
            rank_list.append(card.rank)
        rank_list.sort()    
        for i in range(len(rank_list)-1):
            # "ace is low" case
            if rank_list[i] == (rank_list[i+1] - 1):
                num_in_seq += 1
            # "ace is high" case
            elif rank_list[i] == 13 and rank_list[i+1] == 1:
                num_in_seq += 1
            else:
                num_in_seq = 0
       
        if num_in_seq >= 4:
            return True
        else:
            return False
                                       
    def has_flush(self):
        """Returns True if the hand has five cards with the same suit, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        if len(self.cards) < 5:
            raise ValueError ('Hand must have at least 5 cards') 
            
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_full_house(self):
        """Returns True if the hand has a three cards with one rank, 
        two cards with another, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        has_two = False
        has_three = False
        if len(self.cards) < 5:
            raise ValueError ('Hand must have at least 5 cards') 
        self.rank_hist()
        for val in self.ranks.values():
            if val == 2:
                has_two = True
            elif val == 3:
                has_three = True
        if has_two and has_three:
            return True
        else:
            return False
        
    def has_four_of_a_kind(self):
        """Returns True if the hand has four cards with the same rank, False otherwise.
        Note that this works correctly for hands with more than 4 cards.        
        """
        if len(self.cards) < 4:
            raise ValueError ('Hand must have at least 4 cards') 
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False
    
    def has_straight_flush(self):
        """Returns True if five cards in sequence and with the same suit, 
        False otherwise.
        Note that this works correctly for hands with more than 5 cards.        
        """
        if len(self.cards) < 5:
            raise ValueError ('Hand must have at least 5 cards')
        # first of all check that if the hand has flush or not
        if self.has_flush():
            # Hand has flush. Remove cars from the hand that has different
            # suit and then check whether are they in sequence or not
            # make sure adding removed cards back to the hand before
            # returning
            removed_cards = Hand()
            cards_to_remove = []
            num_removed_cards = 0
            self.sort() # make sure hand is sorted
            for card in self.cards:
                if self.suits[card.suit] < 5:
                    cards_to_remove.append(card)
            for card in cards_to_remove:
                self.remove_card(card)
                removed_cards.add_card(card)
                num_removed_cards += 1
            if self.has_straight():
                removed_cards.move_cards(self,num_removed_cards)
                return True
            else:
                removed_cards.move_cards(self,num_removed_cards)
                return False 
        else:
            return False
    
    def classify(self):
        """figures out the highest-value classification for a hand
        and sets the label attribute accordingly. For example, a 
        7-card hand might contain a flush
        and a pair; it should be labeled 'flush'."""
        if self.has_straight_flush():
            self.label = 'straight flush'
            return
        elif self.has_four_of_a_kind():
            self.label = 'four of a kind'
            return
        elif self.has_full_house():
            self.label = 'full house'
            return
        elif self.has_flush():
            self.label = 'flush'
            return
        elif self.has_straight():
            self.label = 'straight'
            return
        elif self.has_three_of_a_kind():
            self.label = 'three of a kind'
            return
        elif self.has_two_pair():
            self.label = 'two pair'
            return
        elif self.has_pair():
            self.label = 'pair'
            return
        else:
            self.label = 'Rest'            
     
if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    #deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print "Hand has pair? %s" %hand.has_pair()
        print "Hand has two pairs? %s" %hand.has_two_pair()
        print "Hand has three of a kind? %s" %hand.has_three_of_a_kind()
        print "Hand has flush? %s" %hand.has_flush()
        print "Hand has straight? %s" %hand.has_straight()
        print "Hand has full house? %s" %hand.has_full_house()
        print "Hand has four of a kind? %s" %hand.has_four_of_a_kind()
        print "Hand has straight flush? %s" %hand.has_straight_flush()
        hand.classify()
        print 'Hand is %s' %hand.label
        print ''
        

