"""
INSTRUCTIONS: Type a command and this file will do the selected operation using deckfuncs.
note: the card names are case-sensitive
available commands: search, draw, view, bury, discard, mill, return to deck, to top of deck, to bottom of deck, graveyard to hand / gy to hand, view top cards, play, remove
"""
import deckfuncs as df
from random import shuffle
deck = ["Crobat V", "Crobat V", "Deino", "Deino", "Zweilous", "Hydreigon", "Hydreigon", "Koffing", "Koffing", "Koffing", "Koffing", "Weezing", "Weezing", "Weezing", "Galarian Weezing", "Galarian Weezing", "Quick Ball", "Quick Ball", "Quick Ball", "Quick Ball", "Rare Candy", "Rare Candy", "Evolution Incense", "Evolution Incense", "Evolution Incense", "Battle VIP Pass", "Battle VIP Pass", "Battle VIP Pass", "Battle VIP Pass", "Familiar Bell", "Familiar Bell", "Switch", "Switch", "Ordinary Rod", "Ordinary Rod", "Marnie", "Marnie", "Boss's Orders", "Boss's Orders", "Professor's Research", "Professor's Research", "Piers", "Piers", "Choice Belt", "Choice Belt", "Choice Belt", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy", "Darkness Energy"]
hand = []
graveyard = []
activeSpot = []
bench = []
shuffle(deck)
for x in range(7):
    df.draw(deck, hand, False)
print(hand)
def commands():
    command = input("Command? ").lower()
    if command == "search":
        toSearch = input("Card to search? ")
        try:
            df.search(toSearch, deck, hand, True)
            print(toSearch + " was added to your hand.")
            commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "draw":
        try:
            numDraw = int(input("Draw how many cards? "))
        except:
            print("The number must be an integer.")
            commands()
        for i in range(numDraw):
            drawn = df.draw(deck, hand, True)
            print("You drew: " + drawn)
        commands()
    elif command == "view":
        target = input("View which field? ").lower()
        if target == "hand":
            print(hand)
            commands()
        elif target == "deck":
            print(deck)
            commands()
        elif target == "graveyard" or target == "gy":
            print(graveyard)
            commands()
        elif target == "active spot" or target == "active":
            print(activeSpot)
            commands()
        elif target == "bench":
            print(bench)
            commands()
        else:
            print("Area not found.")
            commands()
    elif command == "bury":
        toBury = input("Bury which card? ")
        try:
            df.bury(toBury, deck, graveyard, True)
            print("Buried: " + toBury)
            commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "discard":
        toDiscard = input("Discard which card? ")
        try:
            df.discard(toDiscard, hand, graveyard)
            print("You discarded: " + toDiscard)
            commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "mill":
        try:
            toMill = int(input("Mill how many cards? "))
        except:
            print("The number must be an integer.")
            commands()
        milledcards = df.mill(deck, graveyard, toMill)
        print("Milled: ")
        for i in milledcards:
            print(i)
        commands()
    elif command == "return to deck":
        toReturn = input("Return which card to deck? ")
        try:
            df.returnCard(toReturn, deck, graveyard, True)
            print("Returned " + toReturn + " to the deck.")
            commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "to top of deck":
        toTop = input("Return which card to the top of the deck? ")
        try:
            df.topDeck(toTop, deck, graveyard)
            print("Returned " + toTop + " to the top of the deck.")
            commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "to bottom of deck":
        toBottom = input("Return which card to the bottom of the deck? ")
        try:
            df.bottomDeck(toTop, deck, graveyard)
            print("Returned " + toBottom + " to the bottom of the deck.")
            commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "graveyard to hand" or command == "gy to hand":
        toHand = input("Return which card to the hand? ")
        try:
            df.gyToHand(toHand, graveyard, hand)
            print("Return " + toHand + " to the hand from the graveyard.")
            commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "view top cards":
        try:
            numTop = int(input("View how many cards? "))
            topcards = df.viewTopCards(deck, numTop)
            print(topcards)
            commands()
        except:
            print("The number must be an integer. ")
            commands()
    elif command == "play":
        toPlay = input("Play which Pokémon? ")
        try:
            hand.remove(toPlay)
            if len(activeSpot) < 1:
                activeSpot.append(toPlay)
                print("You put " + toPlay + " on your active spot.")
                commands()
            else:
                bench.append(toPlay)
                print("You put " + toPlay + " on your bench.")
                commands()
        except:
            print("A card with that name was not found.")
            commands()
    elif command == "remove": # this command is unique to gameboard - it's not in deckfuncs
        removedCard = input("Remove which card? ")
        removeFrom = input("Remove from which area? (Active spot / Bench) ").lower()
        if removeFrom == "active spot" or removeFrom == "active":
            activeSpot.pop(0)
            graveyard.insert(0, removedCard)
            print(removedCard + " was removed from the active spot and sent to the graveyard.")
            commands()
        elif removeFrom == "bench":
            bench.remove(removedCard)
            graveyard.insert(0, removedCard)
            print(removedCard + " was removed from the bench and sent to the graveyard.")
            commands()
        else:
            print("Either the card was not found or the specified area was invalid. Please try again.")
            commands()
    else:
        print("Command not found. Please try again.")
        commands()
commands()
