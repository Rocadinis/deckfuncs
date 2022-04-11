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
    gyVar.append(card)
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    elif shuffleAfter == True:
        shuffle(deckVar)
    return card

def mill(deckVar, gyVar, number):
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