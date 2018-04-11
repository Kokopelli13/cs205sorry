#GUI()
#settings()
#game turn loop (while not won)
#   draw() --> Deck
#   move() --> player
#   change GUI

#from deck import Deck
import pygame
from player import Player

class Game:
    def __init__(self, main):
        """
        Class constructor
        """
        self.main = main
        self.turn = 'bottom'

        #Create players at different position in the corresponding color
        #Store players in a list
        fourPosition = ['bottom', 'left', 'top', 'right']
        fourColor = ['red', 'blue', 'yellow', 'green']
        playerColorIndex = fourColor.index(self.main.color)
        self.playerList = []
        for i in range(4):
            print("\nCreate a", fourColor[(playerColorIndex+i)%4], "player at", fourPosition[i], "side\n")
            self.playerList.append(Player(self.main, i, fourPosition[i], fourColor[(playerColorIndex+i)%4]))

        pass

    def drawCard(self):
        """
        Change this!!!!
        """
        #return int(input("How many steps to move:"))
        steps = self.main.deck.drawNext()
        if(steps == 'Sorry!'):
            steps = 0
        else:
            steps = int(steps)
        return steps

    def getPlayerNumAndColor(self):
        """
        Change This!!!!
        """
        self.number = 2
        self.colorList = ['red', 'yellow']

        fourPosition = ['bottom', 'left', 'top', 'right']
        fourColor = ['red', 'blue', 'yellow', 'green']
