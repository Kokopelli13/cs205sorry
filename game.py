#GUI()
#settings()
#game turn loop (while not won)
#   draw() --> Deck
#   move() --> player
#   change GUI

#from deck import Deck
import pygame
from player import Player
from playing import Playing


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
        playerSetting = [self.main.pc0difficulty, self.main.pc1difficulty, self.main.pc2difficulty, self.main.pc3difficulty]
        self.playerList = []
        for i in range(self.playerNum):
            print("\nCreate a", fourColor[(playerColorIndex+i)%4], "player at", fourPosition[i], "side\n")
            self.playerList.append(Player(self.main, i, fourPosition[i], fourColor[(playerColorIndex+i)%4], playerSetting[i]))

        self.playing = Playing(self.main, self.turn, self.playerList[0], self.playerNum)

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
        self.checkEndGame()
        
        fourPosition = ['bottom', 'left', 'top', 'right']
        positionList = fourPosition[:self.playerNum]
        currentIndex = positionList.index(self.turn)
        nextIndex = (currentIndex+1)%self.playerNum
        self.turn = positionList[nextIndex]
        
        self.playing.nextTurn(self.turn, self.playerList[nextIndex])

        pass

    def checkEndGame(self):
        """
        Check if there's anyone winning the game
        """
        homeCount = 0
        for i in range(self.playerNum):
            for j in range(4):
                if self.playerList[i].pawnList[j].position['type'] is 'home':
                    homeCount += 1
            if homeCount is 4:
                self.endGame(i)
            else:
                homeCount = 0
        pass

    def endGame(self, playerIndex):
        """
        Finish this game
        """
        winner = self.playerList[playerIndex]
        print("Winner")
        print(winner.color)

        pass



    # def save(self):
    #     #save button to call save file
    #     savebutton = menu.Button(self.main, 330, 860, "save", "images/stats.png", 1)
    #     Save.save(self)
