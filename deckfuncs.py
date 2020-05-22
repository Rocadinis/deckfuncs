# Made by Rocadinis at github.com
from random import shuffle
def draw(deckVar, handVar, lenCheck):
    if lenCheck == True and len(deckVar) <= 0:
        pass
    else:
        drawn = deckVar.pop(0)
        handVar.append(drawn)
        return drawn

def search(card, deckVar, handVar):
    deckVar.remove(card)
    handVar.append(card)
    shuffle(deckVar)
    return card

def bury(card, deckVar, gyVar):
    deckVar.remove(card)
    gyVar.append(card)
    shuffle(deckVar)
    return card

def mill(deckVar, gyVar, number):
    milledList = []
    for i in range(number):
        topCard = deckVar.pop(0)
        gyVar.insert(0, topCard)
        milledList.append(topCard)
    return milledList
        
def returnCard(card, deckVar, gyVar):
    gyVar.remove(card)
    deckVar.append(card)
    shuffle(deckVar)
    return card