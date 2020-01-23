# Made by Rocadinis at github.com
# Deckfuncs is a library for card-based games.
# IMPORTANT! If you are going to use these functions, keep in mind that the variables correspondant to Hands, Decks and Graveyards (if this last one does exist) need to be Lists in order for these functions to work, since this library heavily uses List methods.
# Also, here's some friendly advice. Remember that these functions TAKE OUT cards from decks, which means the number of cards decrease, too. You may or not want to increase / decrease the values of variables that count the number of cards on hands, decks, graveyards, or length functions... It's up to you!
def draw(deckVar, handVar):
    """
    Void - Draws the top card of a deck, deckVar (where you should put a variable correspondant to a deck), and places it on your hand - handVar (a hand variable.)
    """
    drawn = deckVar.pop(0)
    handVar.append(drawn)

def search(cardName, deckVar, handVar):
    """
    Void - Adds a card (cardName) from your deck (deckVar) to your hand (handVar).
    """
    deckVar.remove(cardName)
    handVar.append(cardName)