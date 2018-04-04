#drawNext()
#discard()
#shuffle()
import random
class Deck:
    #class variables
    def __init__(self):
        #class constructor
        #The modern deck contains 45 cards: there are five
        #1 cards as well as four each of the other cards
        #(Sorry!, 2, 3, 4, 5, 7, 8, 10, 11 and 12)
        #13 = sorry card

        #initialise empty array
        self.deck = []

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
                self.deck.append(int)
            else:
                self.deck.append("Sorry!")
            #changes int every 4 spaces
            if counter>1 and counter%4 == 0:
                int+=1

            counter+=1

        #print(self.deck)
        self.shuffle()
        #print(self.deck)


    def shuffle(self):
        #function to shuffle deck
        random.shuffle(self.deck)


    global i
    i = 0

    def drawNext(self):
        #return the next card
        global i
        value = self.deck[i];
        print(value)
        i+=1


if(__name__ == "__main__"):
    app = Deck()
