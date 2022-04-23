# Made by Rocadinis at github.com
from random import shuffle, randint
import math
def draw(deckVar, handVar):
    if len(deckVar) <= 0:
        raise Exception("The deck list is empty")
    else:
        drawn = deckVar.pop(0)
        handVar.append(drawn)
        return drawn

def search(card, deckVar, handVar, shuffleAfter):
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    else:
        deckVar.remove(card)
        handVar.append(card)
    if shuffleAfter == True:
        shuffle(deckVar)
    return card

def bury(card, deckVar, gyVar, shuffleAfter):
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    else:
         deckVar.remove(card)
         gyVar.insert(0, card)
    if shuffleAfter == True:
        shuffle(deckVar)
    return card

def discard(card, handVar, gyVar):
    handVar.remove(card)
    gyVar.insert(0, card)
    return card

def mill(deckVar, gyVar, number):
    if type(number) != int:
        raise TypeError("The number of cards to mill must be an integer")
    milledList = []
    for i in range(number):
        topCard = deckVar.pop(0)
        gyVar.insert(0, topCard)
        milledList.append(topCard)
    return milledList
        
def returnCard(card, deckVar, gyVar, shuffleAfter):
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    else:
        gyVar.remove(card)
        deckVar.append(card)
    if shuffleAfter == True:
        shuffle(deckVar)
    return card

def gyToHand(card, gyVar, handVar):
    if len(gyVar) <= 0:
        raise Exception("The graveyard / discard pile is empty")
    else:
        gyVar.remove(card)
        handVar.append(card)
        return card

def topDeck(card, deckVar, gyVar):
    if len(gyVar) <= 0:
        raise Exception("The graveyard / discard pile is empty")
    else:
        gyVar.remove(card)
        deckVar.insert(0, card)
        return card

def bottomDeck(card, deckVar, gyVar):
    if len(gyVar) <= 0:
        raise Exception("The graveyard / discard pile is empty")
    else:
        deckLength = len(deckVar)
        gyVar.remove(card)
        deckVar.insert(deckLength + 1, card)
        return card

def viewTopCards(deckVar, numCards):
    if type(numCards) != int:
        raise TypeError("The number of cards to be viewed must be an integer")
    elif numCards <= 0:
        raise Exception("The number of cards to be viewed must not be 0 or less")
    else:
        viewed = []
        for i in range(numCards):
            viewed.insert(i - 1, deckVar[0:numCards])
            return viewed

def shuffleHandIntoDeck(deckVar, handVar): # i tried going for a "for each card in hand" loop but for some reason it shuffled cards until only 3 were left in hand, and idk why. this code works though
    shuffled = []
    for i in range(len(handVar)):
        toAdd = handVar[0]
        deckVar.append(toAdd)
        shuffled.append(toAdd)
        handVar.pop(0)
    shuffle(deckVar)
    return shuffled

def shuffleGYIntoDeck(deckVar, gyVar): # the same happened in this function during testing, I assume it's python's fault for some reason
    shuffled = []
    for i in range(len(gyVar)):
        toAdd = gyVar[0]
        deckVar.append(toAdd)
        shuffled.append(toAdd)
        gyVar.pop(0)
    shuffle(deckVar)
    return shuffled

def findCopies(card, target):
    copies = []
    for i in range(target.count(card)):
        copies.append(card)
    return copies

def cut(deckVar, shuffleBefore):
    if type(shuffleBefore) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    else:
        if shuffleBefore == True:
            shuffle(deckVar)
        if len(deckVar) % 2 == 0:
            cutNum = int(len(deckVar) / 2)
            cutDeck1 = deckVar[cutNum:]
            cutDeck2 = deckVar[:cutNum]
            return cutDeck1, cutDeck2
        else:
            cutNum = math.floor(len(deckVar) / 2)
            cutDeck1 = deckVar[cutNum:]
            cutDeck2 = deckVar[:cutNum]
            return cutDeck1, cutDeck2

def dice(sides):
    if type(sides) != int:
        raise TypeError("The sides variable must be an integer")
    else:
        return randint(1, sides)
