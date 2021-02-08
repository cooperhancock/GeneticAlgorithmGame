from enum import Enum

# card suits

S = 'spades'
C = 'clubs'
H = 'hearts'
D = 'diamonds'
null = 'no suit'

# card class

class Card:
    # constructor
    def __init__(self, value=0, suit=null):
        self.value = value
        self.suit = suit
    # returns true if valid card value
    def hasValue(self):
        valid = self.suit == S or self.suit == C or self.suit == H or self.suit == D
        return valid and self.value>0 and self.value<14
    # comparisons
    def __eq__(self, other):
        return self.value == other.value
    def __ne__(self, other):
        return self.value != other.value
    # for comparisons, aces are low
    def __lt__(self, other): 
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value
    def sameSuit(self, other):
        return self.suit == other.suit
    # to string format suit of value
    def __str__(self):
        if self.value == 1:
            value = 'ace'
        elif self.value == 11:
            value = 'jack'
        elif self.value == 12:
            value = 'queen'
        elif self.value == 13:
            value = 'king'
        else:
            value = self.value
        return str(value) + ' of ' + str(self.suit)
# takes input from user and returns card object
def inputCard(msg):
    while True:
        cardIn = list(map(str,input(msg).strip().split()))
        if cardIn[0] == 'ace':
            cardIn[0] = 1
        elif cardIn[0] == 'jack':
            cardIn[0] = 11
        elif cardIn[0] == 'queen':
            cardIn[0] = 12
        elif cardIn[0] == 'king':
            cardIn[0] = 13
        try:
            cardIn[0] = int(cardIn[0])
        except:
            cardIn[0] = 0
        newCard = Card(cardIn[0], cardIn[2])
        if newCard.hasValue():
            break
        else:
            msg = 'invalid card, try again: '
    return newCard

card1 = Card(1, S)
print(card1)
card2 = inputCard('insert: ')
print(card2)