#GUI()
#settings()
#game turn loop (while not won)
#   draw() --> Deck
#   move() --> player
#   change GUI

#from deck import Deck
import pygame
from player import Player
#from menu import Button


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

        playerNumDict = {'one': 2, 'two':3, 'three':4}
        self.playerNum = playerNumDict[self.main.numPlayers]
        self.playerList = []
        for i in range(self.playerNum):
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
            print('moving ' + str(steps) + ' steps')
        return steps

    def nextTurn(self):
        """
        Change to next turn
        """
        fourPosition = ['bottom', 'left', 'top', 'right']
        positionList = fourPosition[:self.playerNum]
        currentIndex = positionList.index(self.turn)
        self.turn = positionList[(currentIndex+1)%self.playerNum]

        pass

    def save(self):
        #save button to call save file
        savebutton = menu.Button(self.main, 330, 860, "save", "images/stats.png", 1)
        Save.save(self)
