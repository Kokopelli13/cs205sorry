import pygame
from board import Board
from instructions import Instructions

from game import Game


class Menu:
    def __init__(self, main):
        self.main = main
        self.main.activeObj = set()
        #Buttons
        newGame = Button(self.main, 250, 300, "new", "images/newgame.png", 1)
        #instructions = Button(self.main, 250, 400, "instructions", "images/newgame.png", 1)
        test = Text(self.main, 100, 100, 'Hello')
        instructions = Button(self.main, 250, 400, "instructions", "images/newgame.png", 1)
        #test = Text(self.main, 100, 100, 'Hello')

class Button:
    def __init__(self, main, x, y, action, img, scale):
        self.action = action
        self.main = main
        self.x, self.y = x, y
        self.main.activeObj.add(self)
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, scale)

    def draw(self):
        self.rect = self.main.screen.blit(self.img, (self.x, self.y))

    def onClick(self):
        if self.action == "new":
            self.newGame()
        if self.action == "instructions":
            self.instructions()
        if self.action == "red" or self.action == "blue" or self.action == "yellow" or self.action == "green":
            self.setUpBoard()

    def newGame(self):
        self.main.activeObj = set()
        self.main.activeObj.add(Button(self.main, 100, 300, "red", "images/pawn_red.png", 0.5))
        self.main.activeObj.add(Button(self.main, 200, 300, "blue", "images/pawn_blue.png", 0.5))
        self.main.activeObj.add(Button(self.main, 300, 300, "yellow", "images/pawn_yellow.png", 0.5))
        self.main.activeObj.add(Button(self.main, 400, 300, "green", "images/pawn_green.png", 0.5))

    def instructions(self):
        Instructions()

    def setUpBoard(self):
        self.main.color = self.action
        self.main.activeObj = set()
        self.main.board = Board(self.main)
        self.main.game = Game(self.main)
        self.main.gameStarted = True


class Text:
    def __init__(self, main, x, y, text):
        self.main = main
        self.x, self.y = x, y
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', 26)
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.main.activeObj.add(self)

    def draw(self):
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.main.screen.blit(self.textSurface, (self.x, self.y))
