# Made by Rocadinis at github.com
# Deckfuncs is a library for card-based games.
# IMPORTANT! If you are going to use these functions, keep in mind that the variables correspondant to Hands, Decks and Graveyards (if this last one does exist) need to be Lists in order for these functions to work, since this library heavily uses List methods.
# Also, here's some friendly advice. Remember that these functions TAKE OUT cards from decks, which means the number of cards decrease, too. You may or not want to increase / decrease the values of variables that count the number of cards on hands, decks, graveyards, or length functions... It's up to you!
from random import shuffle
def draw(deckVar, handVar, lenCheck):
    """
    Void - Draws the top card of a deck, deckVar (where you should put a variable correspondant to a deck), and places it on a hand - handVar (a hand variable.). If lenCheck (bool) is set to true, this function reads the number of cards in deckVar, and will do nothing if the number of cards is 0 or less (preventing the draw). If lenCheck is set to false, this bypasses the check.

    Example: draw(myDeck, myHand, True)
    """
    if lenCheck == True and len(deckVar) <= 0:
        pass
    else:
        drawn = deckVar.pop(0)
        handVar.append(drawn)

def search(card, deckVar, handVar):
    """
    Void - Adds a card from a deck (deckVar) to a hand (handVar), then shuffles the deck. 'card' can be treated as, for example, a variable or list element. Only one card of the given name is taken, not all occurences!

    Example: search("Swamp", myDeck, myHand) - This would search a deck for a card named 'Swamp' and put it on a player's hand.
             search(myDeck[2], myDeck, myHand) - This would search for the third card on top of a player's deck and put it on their hand.
    """
    deckVar.remove(card)
    handVar.append(card)
    shuffle(deckVar)

def bury(card, deckVar, gyVar):
    """
    Void - Sends a card from a deck (deckVar) to a graveyard / discard pile (gyVar), then shuffles the deck. 'card' can be treated as, for example, a variable or list element. Only one card of the given name is taken, not all occurences!

    Example: bury("Zombie", myDeck, graveyard) - This would send a card named "Zombie" from a deck to the graveyard / discard pile.
    """
    deckVar.remove(card)
    gyVar.append(card)
    shuffle(deckVar)

def mill(deckVar, gyVar, number):
    """
    Void - Sends the top X cards (number) of a deck to the graveyard / discard pile (gyVar). Keep in mind that the last cards that go into the graveyard will effectively be in the first positions in the graveyard / discard pile list.

    Example: mill(myDeck, gy, 3) - This would send the top 3 cards of a deck to the graveyard / discard pile.
    """
    for i in range(number):
        topCard = deckVar.pop(0)
        gyVar.insert(0, topCard)

def returnCard(card, deckVar, gyVar):
    """
    Void - Returns a card (card) to a deck (deckVar) from a graveyard / discard pile (gyVar). The deck is then shuffled.

    Example: returnCard("Island", mydeck, graveyard) - This would return a card named "Island" from a deck to the graveyard / discard pile, then shuffle the deck.
    """
    gyVar.remove(card)
    deckVar.append(card)
    shuffle(deckVar)