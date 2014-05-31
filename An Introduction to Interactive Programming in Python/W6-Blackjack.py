'''
Created on Jun 1, 2013
@author: Nenad

Blackjack is a simple, popular card game that is played in many casinos.
Cards in Blackjack have the following values:
    an ace may be valued as either 1 or 11 (player's choice),
    face cards (kings, queens and jacks) are valued at 10 and 
    the value of the remaining cards corresponds to their number. 
During a round of Blackjack, the players plays against a dealer with the goal of building a hand (a collection of cards) 
whose cards have a total value that is higher than the value of the dealer's hand, but not over 21.  
(A round of Blackjack is also sometimes referred to as a hand.)

The game logic for our simplified version of Blackjack is as follows. 
The player and the dealer are each dealt two cards initially with one of the dealer's cards being dealt faced down 
(his hole card). The player may then ask for the dealer to repeatedly "hit" his hand by dealing him another card. 
If, at any point, the value of the player's hand exceeds 21, the player is "busted" and loses immediately. 
At any point prior to busting, the player may "stand" and the dealer will then hit his hand until the value of his hand 
is 17 or more. (For the dealer, aces count as 11 unless it causes the dealer's hand to bust). 
If the dealer busts, the player wins. Otherwise, the player and dealer then compare the values of their hands and 
the hand with the higher value wins. The dealer wins ties in our version.

http://www.codeskulptor.org/#user15_6h1xzMh89f_0.py
'''
# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
score = 0
outcome = "Hit or Stand?"
sMessage = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], 
                           pos[1] + CARD_CENTER[1]], 
                          CARD_SIZE)
        
    def drawBack(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0] + 1, 
                           pos[1] + CARD_BACK_CENTER[1] + 1], 
                          CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        sCards = ""
        for card in self.cards:
            sCards = sCards + str(card) + " "
        return "Hand contains " + sCards.strip()

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        nValue = 0
        bAce = False
        for card in self.cards:
            nValue += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                bAce = True
        if bAce and nValue < 12:
            nValue += 10
        return nValue
   
    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            card.draw(canvas, pos)
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        sCards = ""
        for card in self.cards:
            sCards = sCards + str(card) + " "
        return "Deck contains " + sCards.strip()

#define event handlers for buttons
def deal():
    global in_play, myDeck, hPlayer, hDealer, outcome, score, sPlayer, sDealer, sMessage
    if in_play:
        score -= 1
        in_play = False
        deal()
    else:    
        myDeck = Deck()
        hPlayer = Hand()
        hDealer = Hand()
        myDeck.shuffle()
        hPlayer.add_card(myDeck.deal_card())
        hPlayer.add_card(myDeck.deal_card())
        hDealer.add_card(myDeck.deal_card())
        hDealer.add_card(myDeck.deal_card())
        outcome = "Hit or Stand?"
        sPlayer = "Player"
        sDealer = "Dealer"
        sMessage = ""
        in_play = True

def hit():
    global in_play, myDeck, hPlayer, score, outcome, sPlayer, sMessage
    if in_play:
        if hPlayer.get_value() < 22:
            hPlayer.add_card(myDeck.deal_card())
            if hPlayer.get_value() > 21:
                sPlayer = "Busted!"
                sMessage = "You've busted! You loose!"
                score -= 1
                outcome = "New deal?"
                in_play = False
       
def stand():
    global in_play, hDealer, hPlayer, score, outcome, sDealer, sMessage
    if in_play:
        while (hDealer.get_value() < 17):
            hDealer.add_card(myDeck.deal_card())
        if hDealer.get_value() > 21:
            sDealer = "Busted!"
            sMessage = "Dealer busted! You win!"
            score += 1
            outcome = "New deal?"
            in_play = False
        elif hPlayer.get_value() > hDealer.get_value():
            sMessage = "Your hand's stronger! You win!"
            score += 1
            outcome = "New deal?"
            in_play = False
        else:
            sMessage = "Your hand's weaker! You loose!"
            score -= 1
            outcome = "New deal?"
            in_play = False

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", (60, 100), 40, "Aqua")
    lDealer = canvas.draw_text(sDealer, (60, 185), 33, "Black")
    lPlayer = canvas.draw_text(sPlayer, (60, 385), 33, "Black")
    lOutcome = canvas.draw_text(outcome, (250, 385), 33, "Black")
    lMessage = canvas.draw_text(sMessage, (250, 185), 25, "Black")
    lScore = canvas.draw_text("Score: " + str(score), (450, 100), 33, "Black")
    hDealer.draw(canvas, [-65, 200])
    hPlayer.draw(canvas, [-65, 400])
    if in_play:
        hDealer.cards[0].drawBack(canvas, [28, 200])
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
deal()