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
import random


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
            #print("\nCreate a", fourColor[(playerColorIndex+i)%4], "player at", fourPosition[i], "side\n")
            self.playerList.append(Player(self.main, i, fourPosition[i], fourColor[(playerColorIndex+i)%4], playerSetting[i]))

        self.playing = Playing(self.main, self.turn, self.playerList[0], self.playerNum)


        #Add playing information to board object
        self.layer = 4
        self.main.activeObj.add(self)

        self.nextTurnBool = False

        pass

    def draw(self):
        self.rect = pygame.Rect(0,0,0,0)
        pass

    def onClick(self):
        pass

    def tick(self):
        if self.nextTurnBool is True:
            fourPosition = ['bottom', 'left', 'top', 'right']
            currentIndex = fourPosition.index(self.lastTurn)
            for pawn in self.playerList[currentIndex].pawnList:
                if pawn.finishMovingBool is False:
                    #Add this print function to slow down the program to avoid problems
                    #Really weird!! It might be the issue of race condition
                    #print("#######Pawn's still moving")
                    return
            nextIndex = fourPosition.index(self.turn)
            self.playing.nextTurn(self.turn, self.playerList[nextIndex])
            self.nextTurnBool = False

            if self.turn is not 'bottom':
                self.computerMove()
        pass

    def drawCard(self):
        """
        Draw a card from the deck
        """
        #return int(input("How many steps to move:"))
        steps = self.main.deck.drawNext()
        if(steps == 'Sorry!'):
            steps = 0
        else:
            steps = int(steps)
            #print('moving ' + str(steps) + ' steps')
        return steps

    def nextTurn(self, allowed):
        """
        Change to next turn
        """
        self.checkEndGame()

        if allowed is True:
            if self.turn is not 'bottom':
                self.main.processRendering()
                self.delayGame(10)

            self.lastTurn = self.turn

            fourPosition = ['bottom', 'left', 'top', 'right']
            positionList = fourPosition[:self.playerNum]
            currentIndex = positionList.index(self.turn)
            nextIndex = (currentIndex+1)%self.playerNum
            self.turn = positionList[nextIndex]

            self.nextTurnBool = True
            #self.playing.nextTurn(self.turn, self.playerList[nextIndex])

        pass

    def computerMove(self):
        """
        Computer plays automatically
        """
        self.playing.drawButton.onClick()

        index, move = self.chooseRandomMove()

        self.main.processRendering()
        self.delayGame(5)


        if move is None:
            self.playing.skipButton.onClick()
            return

        if move['option'] is 1:
            self.playing.optionButton1.onClick()
        else:
            self.playing.optionButton2.onClick()

        firstPawn = move['firstPawn']
        secondPawn = move['secondPawn']

        #All cards but 7
        if self.playing.drawnCard is not 7:
            if firstPawn is not None:
                firstPawn.onClick()
            if secondPawn is not None:
                secondPawn.onClick()
        #Card 7
        else:
            if move['option'] is 1:
                firstPawn.onClick()
            else:
                #The first pawn
                numberButtons = [None, self.playing.numButton1, self.playing.numButton2, self.playing.numButton3, self.playing.numButton4, self.playing.numButton5, self.playing.numButton6]
                firstPawn.onClick()
                numberButtons[move['move']].onClick()
                secondPawn.onClick()

        pygame.display.update()

        pass

    def delayGame(self, loop):
        for i in range(loop):
            pygame.display.update()
        pass

    def chooseRandomMove(self):
        """
        Randomly return a possible move
        """
        if len(self.playing.possibleList) is 0:
            return 0, None
        index = random.randrange(len(self.playing.possibleList))
        possibleMove = self.playing.possibleList[index]

        return index, possibleMove

    def checkEndGame(self):
        """
        Check if there's anyone winning the game
        """
        end = False
        homeCount = 0
        for i in range(self.playerNum):
            for j in range(4):
                if self.playerList[i].pawnList[j].position['type'] is 'home':
                    homeCount += 1
            if homeCount is 4 and not end:
                self.endGame(i)
                end = True
            else:
                homeCount = 0
        pass

    def endGame(self, playerIndex):
        """
        Finish this game
        """
        winner = self.playerList[playerIndex]
        if winner == 0:
            self.won == "won"
        else:
            self.won == "lost"
        #print("Winner")
        #print(winner.color)
        self.main.win(winner.color)

        pass



    # def save(self):
    #     #save button to call save file
    #     savebutton = menu.Button(self.main, 330, 860, "save", "images/stats.png", 1)
    #     Save.save(self)
