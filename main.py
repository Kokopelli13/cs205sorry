import sys, pygame
from menu import Menu
from board import Board


class Main:
    def __init__(self):
        self.activeObj = set()
        pygame.init()
        #Create the screen
        self.size = width, height = 960, 640 #Screen size
        self.scale = 960/2100
        #screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.screen = pygame.display.set_mode(self.size)
        #set up the background (static)
        self.background = pygame.image.load('images/background.png').convert()
        self.background = pygame.transform.rotozoom(self.background, 0, self.scale)
        #game variables
        self.gameStarted = False
        self.color = ''
        self.difficulty = ''
        #set up gui
        self.menu = Menu(self)
        self.main()

    def main(self):
        #main loop
        while 1:
            self.processEvents()
            #processGame()
            self.processRendering()

    def processEvents(self):
        #lets look at all the events that have happened
        for event in pygame.event.get():
            #handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('mouse') #debug
                #go through all the active objects to see if any of them were clicked on
                for obj in self.activeObj:
                    if obj.rect.collidepoint(pygame.mouse.get_pos()):
                        print(obj) #debug
                        obj.onClick()
            #handle clicking the close button
            if event.type == pygame.QUIT: #Exit button
                sys.exit()
            #handle keypresses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Esc
                    sys.exit()

    def processGame(self):
        #nothing here yet...
        print('a') #if theres not at least something here python complains

    def processRendering(self):
        #always draw the background first
        self.screen.blit(self.background, (0, 0))
        #then draw everything else on top
<<<<<<< HEAD
        if self.gameStarted:
            self.menu.main.board.map.draw()
            for obj in self.boardObj:
                obj.draw()
        else:
            for obj in self.menuObj:
                obj.draw()
=======
        for obj in self.activeObj:
            obj.draw()
>>>>>>> f16f4185364385c527257f60507b4f482b2457d7
        #finally render the frame
        pygame.display.update()


#if this file is run (as opposed to being imported elsewhere), execute this
if (__name__ == "__main__"):
    app = Main()
