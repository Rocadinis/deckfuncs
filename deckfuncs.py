# Made by Rocadinis at github.com
from random import shuffle
def draw(deckVar, handVar, lenCheck):
    if type(lenCheck) != bool:
        raise TypeError("The lenCheck variable must be true or false")
    elif lenCheck == True and len(deckVar) <= 0:
        pass
    else:
        drawn = deckVar.pop(0)
        handVar.append(drawn)
        return drawn

def search(card, deckVar, handVar, shuffleAfter):
    deckVar.remove(card)
    handVar.append(card)
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    elif shuffleAfter == True:
        shuffle(deckVar)
    return card

def bury(card, deckVar, gyVar, shuffleAfter):
    deckVar.remove(card)
    gyVar.insert(0, card)
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    elif shuffleAfter == True:
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
    gyVar.remove(card)
    deckVar.append(card)
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    elif shuffleAfter == True:
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
    toAdd = deckVar[0]
    for i in range(len(handVar)):
        deckVar.append(toAdd)
        shuffled.append(toAdd)
        handVar.pop(0)
    shuffle(deckVar)
    return shuffled