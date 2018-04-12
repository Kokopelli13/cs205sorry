import pygame
from board import Board
from instructions import Instructions
from database import Database
import sys
from game import Game
from save import Save
from deck import Deck


class Menu:
    def __init__(self, main):
        self.main = main
        self.main.activeObj = set()
        #Images
        welcome = Button(self.main, 84, 68, "none", "images/welcome.png", 0.5)
        #Buttons
        newGame = Button(self.main, 150, 380, "new", "images/newgame.png", 1)
        resumeGame = Button(self.main, 330, 380, "resume", "images/resumegame.png", 1)
        instructions = Button(self.main, 150, 450, "instructions", "images/instructions.png", 1)
        statistics = Button(self.main, 330, 450, "stats", "images/stats.png", 1)
        quit = Button(self.main, 240, 520, "quit", "images/quit.png", 1)

class Button:
    def __init__(self, main, x, y, action, img, scale):
        self.action = action
        self.main = main
        self.x, self.y = x, y
        self.layer = 0
        self.main.activeObj.add(self)
        self.scale = scale
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, self.scale)

    def draw(self):
        self.rect = self.main.screen.blit(self.img, (self.x, self.y))

    def tick(self):
        pass

    def onClick(self):
        if self.action == "new":
            self.newGame()
        if self.action == "instructions":
            self.instructions()
        if self.action == "stats":
            self.read()
        if self.action == "red" or self.action == "blue" or self.action == "yellow" or self.action == "green":
            self.pickNumPlayers()
        if self.action == "numplayersone" or self.action == "numplayerstwo" or self.action == "numplayersthree":
            self.setDifficulty()
        if self.action == "nicedumb" or self.action == "nicesmart" or self.action == "meandumb" or self.action == "meansmart":
            self.setUpBoard()
        if self.action[:3] == "pc1" or self.action[:3] == "pc2" or self.action[:3] == "pc3":
            self.setPC()
        if self.action == "done":
            self.setUpBoard()
        if self.action == "quit":
            sys.exit()

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
        self.main.activeObj.add(Button(self.main, 130, 300, "numplayersone", "images/one.png", 0.5))
        self.main.activeObj.add(Button(self.main, 265, 300, "numplayerstwo", "images/two.png", 0.5))
        self.main.activeObj.add(Button(self.main, 410, 300, "numplayersthree", "images/three.png", 0.5))

    def setDifficulty(self):
        if self.action == "numplayersone":
            self.main.numPlayers = "one"
        if self.action == "numplayerstwo":
            self.main.numPlayers = "two"
        if self.action == "numplayersthree":
            self.main.numPlayers = "three"
        print('num players: ' + self.main.numPlayers)
        self.main.activeObj = set()
        pickDifficultyTxt = Text(self.main, 140, 100, 30, 'How hard should this be?')
        pc1Text = Text(self.main, 70, 185, 30, 'PC1')
        self.main.activeObj.add(Button(self.main, 140, 150, "pc1nicedumb", "images/nicedumb.png", 0.5))
        self.main.activeObj.add(Button(self.main, 250, 150, "pc1nicesmart", "images/nicesmart.png", 0.5))
        self.main.activeObj.add(Button(self.main, 360, 150, "pc1meandumb", "images/meandumb.png", 0.5))
        self.main.activeObj.add(Button(self.main, 470, 150, "pc1meansmart", "images/meansmart.png", 0.5))
        if self.action == "numplayerstwo" or self.action == "numplayersthree":
            pc2Text = Text(self.main, 70, 305, 30, 'PC2')
            self.main.activeObj.add(Button(self.main, 140, 270, "pc2nicedumb", "images/nicedumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 250, 270, "pc2nicesmart", "images/nicesmart.png", 0.5))
            self.main.activeObj.add(Button(self.main, 360, 270, "pc2meandumb", "images/meandumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 470, 270, "pc2meansmart", "images/meansmart.png", 0.5))
        if self.action == "numplayersthree":
            pc3Text = Text(self.main, 70, 425, 30, 'PC3')
            self.main.activeObj.add(Button(self.main, 140, 390, "pc3nicedumb", "images/nicedumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 250, 390, "pc3nicesmart", "images/nicesmart.png", 0.5))
            self.main.activeObj.add(Button(self.main, 360, 390, "pc3meandumb", "images/meandumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 470, 390, "pc3meansmart", "images/meansmart.png", 0.5))
        self.main.activeObj.add(Button(self.main, 250, 520, "done", "images/done.png", 1))

    def setPC(self):
        pc = 0
        if self.action[:3] == "pc1":
            self.main.pc1difficulty = self.action[3:]
        if self.action[:3] == "pc2":
            self.main.pc2difficulty = self.action[3:]
        if self.action[:3] == "pc3":
            self.main.pc3difficulty = self.action[3:]
        for obj in self.main.activeObj:
            if obj.y >= 150 and obj.y <= 390 and obj.x >= 140:
                if obj.action[:3] == self.action[:3]:
                    if obj.action[3:] != self.action[3:]:
                        obj.img = pygame.image.load("images/" + obj.action[3:] + ".png").convert_alpha()
                        obj.img = pygame.transform.rotozoom(obj.img, 0, obj.scale)
                    else:
                        obj.img = pygame.image.load("images/" + obj.action[3:] + "_pressed.png").convert_alpha()
                        obj.img = pygame.transform.rotozoom(obj.img, 0, obj.scale)


    def instructions(self):
        self.main.activeObj = set()
        pickColorTxt = Text(self.main, 176, 250, 30, 'Instructions')
        back = Button(self.main, 150, 380, "back", "images/newgame.png", 1)

        #instructions = Text(self.main, 140, 100, 30, 'Instructions for SORRY!')
        #Instructions()


    def back(self):
        Menu(self.main)


    def read(self):
        Database.read()

    def setUpBoard(self):
        finished = True
        if self.main.numPlayers == "one" and self.main.pc1difficulty == '':
            finished = False
        if self.main.numPlayers == "two" and (self.main.pc1difficulty == '' or self.main.pc2difficulty == ''):
            finished = False
        if self.main.numPlayers == "three" and (self.main.pc1difficulty == '' or self.main.pc2difficulty == '' or self.main.pc3difficulty == ''):
            finished = False
        if finished:
            self.main.activeObj = set()
            self.main.board = Board(self.main)
            self.main.game = Game(self.main)
            self.main.save = Save(self.main)
            #commented out because this was casuing an error
            #self.main.save.save()
            self.main.deck = Deck(self.main)
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

    def onClick(self):
        pass
