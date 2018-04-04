import pygame
from board import Board
from game import Game


class Menu:
    def __init__(self, main):
        self.main = main
        self.main.activeObj = set()
        #Buttons
        newGame = Button(self.main, 250, 300, "new", "images/newgame.png", 1)

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
        if self.action == "red" or self.action == "blue" or self.action == "yellow" or self.action == "green":
            self.setUpBoard()

    def newGame(self):
        self.main.activeObj = set()
        self.main.activeObj.add(Button(self.main, 100, 300, "red", "images/pawn_red.png", 0.5))
        self.main.activeObj.add(Button(self.main, 200, 300, "blue", "images/pawn_blue.png", 0.5))
        self.main.activeObj.add(Button(self.main, 300, 300, "yellow", "images/pawn_yellow.png", 0.5))
        self.main.activeObj.add(Button(self.main, 400, 300, "green", "images/pawn_green.png", 0.5))

    def setUpBoard(self):
        self.main.color = self.action
        self.main.activeObj = set()
        self.main.board = Board(self.main)
        self.main.gameStarted = True
<<<<<<< HEAD
<<<<<<< HEAD
        self.main.menu = Menu(self.main)
        self.main.game = Game(self.main)
=======
>>>>>>> f16f4185364385c527257f60507b4f482b2457d7
=======
>>>>>>> f16f4185364385c527257f60507b4f482b2457d7
