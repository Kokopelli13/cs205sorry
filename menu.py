import pygame
from board import Board
from instructions import Instructions

from game import Game
from save import Save


class Menu:
    def __init__(self, main):
        self.main = main
        self.main.activeObj = set()
        #Text
        #test = Text(self.main, 100, 100, 26, 'Hello')
        #Images
        welcome = Button(self.main, 84, 68, "none", "images/welcome.png", 0.5)
        #Buttons
        newGame = Button(self.main, 150, 380, "new", "images/newgame.png", 1)
        resumeGame = Button(self.main, 330, 380, "resume", "images/resumegame.png", 1)
        instructions = Button(self.main, 150, 460, "instructions", "images/instructions.png", 1)
        statistics = Button(self.main, 330, 460, "stats", "images/stats.png", 1)
        #test = Text(self.main, 100, 100, 'Hello')

class Button:
    def __init__(self, main, x, y, action, img, scale):
        self.action = action
        self.main = main
        self.x, self.y = x, y
        self.layer = 0
        self.main.activeObj.add(self)
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, scale)

    def draw(self):
        self.rect = self.main.screen.blit(self.img, (self.x, self.y))

    def tick(self):
        pass

    def onClick(self):
        if self.action == "new":
            self.newGame()
        if self.action == "instructions":
            self.instructions()
        if self.action == "red" or self.action == "blue" or self.action == "yellow" or self.action == "green":
            self.pickNumPlayers()
        if self.action == "numplayersone" or self.action == "numplayerstwo" or self.action == "numplayersthree":
            self.setDifficulty()
        if self.action == "nicedumb" or self.action == "nicesmart" or self.action == "meandumb" or self.action == "meansmart":
            self.setUpBoard()

    def newGame(self):
        self.main.activeObj = set()
        pickColorTxt = Text(self.main, 176, 250, 30, 'Please pick a color:')
        self.main.activeObj.add(Button(self.main, 120, 300, "red", "images/pawn_red.png", 0.5))
        self.main.activeObj.add(Button(self.main, 220, 300, "blue", "images/pawn_blue.png", 0.5))
        self.main.activeObj.add(Button(self.main, 320, 300, "yellow", "images/pawn_yellow.png", 0.5))
        self.main.activeObj.add(Button(self.main, 420, 300, "green", "images/pawn_green.png", 0.5))

    def pickNumPlayers(self):
        print('color is ' + self.action)
        self.main.color = self.action
        self.main.activeObj = set()
        pickNumPlayersTxt = Text(self.main, 110, 250, 30, 'How many computer players?')
        self.main.activeObj.add(Button(self.main, 120, 300, "numplayersone", "images/pawn_red.png", 0.5))
        self.main.activeObj.add(Button(self.main, 220, 300, "numplayerstwo", "images/pawn_red.png", 0.5))
        self.main.activeObj.add(Button(self.main, 320, 300, "numplayersthree", "images/pawn_red.png", 0.5))

    def setDifficulty(self):
        if self.action == "numplayersone":
            self.main.numPlayers = "one"
        if self.action == "numplayerstwo":
            self.main.numPlayers = "two"
        if self.action == "numplayersthree":
            self.main.numPlayers = "three"
        print('num players: ' + self.main.numPlayers)
        self.main.activeObj = set()
        pickDifficultyTxt = Text(self.main, 140, 250, 30, 'How hard should this be?')
        self.main.activeObj.add(Button(self.main, 120, 300, "nicedumb", "images/pawn_blue.png", 0.5))
        self.main.activeObj.add(Button(self.main, 220, 300, "nicesmart", "images/pawn_blue.png", 0.5))
        self.main.activeObj.add(Button(self.main, 320, 300, "meandumb", "images/pawn_blue.png", 0.5))
        self.main.activeObj.add(Button(self.main, 420, 300, "meansmart", "images/pawn_blue.png", 0.5))

    def instructions(self):
        Instructions()

    def setUpBoard(self):
        self.main.difficulty = self.action
        print('difficulty is ' + self.main.difficulty)
        self.main.activeObj = set()
        self.main.board = Board(self.main)
        self.main.game = Game(self.main)
        self.main.save = Save(self.main)
        #commented out because this was casuing an error
        #self.main.save.save()
        self.main.gameStarted = True


class Text:
    def __init__(self, main, x, y, size, text):
        self.main = main
        self.x, self.y = x, y
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.layer = 0
        self.main.activeObj.add(self)

    def draw(self):
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.main.screen.blit(self.textSurface, (self.x, self.y))

    def tick(self):
        pass
