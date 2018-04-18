import sys, time, pygame
from menu import Menu
from board import Board


class Main:
    def __init__(self):
        self.activeObj = set()
        pygame.init()
        self.clock = pygame.time.Clock()
        #Create the screen
        self.size = width, height = 960, 640 #Screen size
        self.scale = 960/2100
        #screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.screen = pygame.display.set_mode(self.size)
        #set up the background (static)
        self.background = pygame.image.load('images/background.png').convert()
        self.background = pygame.transform.rotozoom(self.background, 0, self.scale)
        #set cursor
        self.cursor = pygame.image.load('images/arrow.png').convert_alpha()
        self.cursor = pygame.transform.rotozoom(self.cursor, 0, 1)
        pygame.mouse.set_visible(False)
        #game variables
        self.gameStarted = False
        self.color = ''
        self.pc0difficulty = ''
        self.pc1difficulty = ''
        self.pc2difficulty = ''
        self.pc3difficulty = ''
        self.numPlayers = ''
        #set up gui
        self.menu = Menu(self)
        
        #Show if the main loop should stop
        self.stop = False

        self.main()
    
    
    def main(self):
        #main loop
        while 1:
            if self.stop is False:
                self.processEvents()
                self.processGame()
                self.processRendering()
                self.clock.tick(60) #run at 60 fps, we don't need more and its extra processing work
            else:
                self.initialize()

                
    def processEvents(self):
        #lets look at all the events that have happened
        for event in pygame.event.get():
            #handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('mouse') #debug
                #print(pygame.mouse.get_pos())
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
                #ESC to exit
                if event.key == pygame.K_ESCAPE: #Esc
                    sys.exit()

    def processGame(self):
        for obj in self.activeObj:
            obj.tick()

    def processRendering(self):
        #always draw the background first
        self.screen.blit(self.background, (0, 0))
        #then draw everything else on top
        #layer 0 = all menu items
        #layer 1 = game board
        #layer 2 = player pieces
        #layer 3 = deck
        for i in range(0, 5):
            for obj in self.activeObj:
                if(obj.layer == i):
                    obj.draw()
        #draw the cursor last
        self.screen.blit(self.cursor, pygame.mouse.get_pos())
        #finally render the frame
        pygame.display.update()


    def quit(self):
        """
        Change the stop variable to stop the main loop
        """
        self.stop = True
        pass

    def initialize(self):
        """
        Initialize game variables
        """
        self.activeObj.clear()
        #game variables
        self.gameStarted = False
        self.color = ''
        self.pc0difficulty = ''
        self.pc1difficulty = ''
        self.pc2difficulty = ''
        self.pc3difficulty = ''
        self.numPlayers = ''

        self.stop = False

        #set up gui
        self.menu = Menu(self)

        pass




#if this file is run (as opposed to being imported elsewhere), execute this
if (__name__ == "__main__"):
    app = Main()
