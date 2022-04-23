# This is an example of the cut function and how to manage its return values.
from random import shuffle
import math
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

deck = ["orange", "banana", "apple","pear", "cherry", "pineapple", "watermelon"]
cutdecks = cut(deck, True)
deck1 = cutdecks[0]
deck2 = cutdecks[1]
print(deck1)
print(deck2)