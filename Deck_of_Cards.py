# Object Orientating programming
# Deck of Cards
# By: Jeff Kwan
# GitHub: https://github.com/Jeffkw213

import random;

class Cards:
    def __init__(self, cards, suit):    
        self.cards = cards
        self.suit = suit
    def show(self):
        print("{} of {}".format(self.cards,self.suit)) 

class Deck:
    def __init__ (self):
        self.deck = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for i in suits:
            for j in range(1, 14):
                self.deck.append(Cards(j, i))
    def shuffle(self):
        for i in range (len(self.deck)-1,0,-1):
            r = random.randint(0 , i)
            self.deck[i]  , self.deck[r] = self.deck[r] , self.deck[i]

    def draw(self):
        return self.deck.pop()
    def show(self):
        for i in self.deck:
            i.show()

class BlackJackPlayer:
    def __init__(self):
        self.hand = []
    
    def drawCards(self, card):
        self.hand.append(card)
    
    def show(self):
        for i in self.hand:
            i.show()

        
        
        
        
Deck = Deck()
Deck.shuffle()
# Deck.show()

hi = BlackJackPlayer()
hi.drawCards(Deck.draw())
hi.drawCards(Deck.draw())
hi.show()