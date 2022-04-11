from random import shuffle
import deckfuncs
deck = ["sonic", "poop", "shit", "fart", "apple", "lads", "akhyu"]
hand = []
graveyard = ["mega"]
def search(card, deckVar, handVar, shuffleAfter):
    deckVar.remove(card)
    handVar.append(card)
    if type(shuffleAfter) != bool:
        raise TypeError("The shuffleAfter variable must be true or false")
    elif shuffleAfter == True:
        shuffle(deckVar)
    return card

result = print(search("poop", deck, hand, True))
deckfuncs.bury("sonic", deck, graveyard, True)
print(deck)
print(len(deck))
print(deck)
deckfuncs.bottomDeck("sonic", deck, graveyard)
print(deck)