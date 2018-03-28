#drawNext()
#discard()
#shuffle()
import random
class Deck:
    #class variables

    #def __init__(self, asdf):
        #class constructor

    def shuffle(deck):
        #function to shuffle deck
        random.shuffle(deck)

    global i
    i = 0
    def drawNext(deck):
        #return the next card
        global i
        value = deck[i];
        print(value)
        i+=1

    #The modern deck contains 45 cards: there are five
    #1 cards as well as four each of the other cards
    #(Sorry!, 2, 3, 4, 5, 7, 8, 10, 11 and 12)
    #13 = sorry card

    #initialise empty array
    deck = []

    #counter  is the count to see how many cards there are total
    counter = 0
    #int is the card number (1-13)
    int = 1

    for x in range(1,46):
        #skips 6 and 9
        if int == 6 or int == 9:
            int+=1
        #makes sure to add 5 1s
        if counter < 5:
            int == 1
        #13 used as Sorry card space, may be changed here and transformed in another place
        if int <13:
            deck.append(int)
        else:
            deck.append("Sorry!")
        #changes int every 4 spaces
        if counter>1 and counter%4 == 0:
            int+=1

        counter+=1

    #print(deck)
    shuffle(deck)
    print(deck)
    #for x in range(0,45):

    tree = input("Enter: ")
    if tree == 'draw':
        drawNext(deck)
    while tree != '':
        tree = input("Enter: ")
        if tree == 'draw':
            drawNext(deck)
