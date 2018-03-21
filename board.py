import sys, pygame


class Board:
    def __init__(self, scale, color):
        """
           Load all necessary images
        """
        #Load background
        self.background = pygame.image.load('images/background.png').convert()
        self.background = pygame.transform.rotozoom(self.background, 0, scale)

        #Load map
        colorToAngle = {'red': 90, 'blue': 180, 'green': 0, 'yellow': 270}
        self.map = pygame.image.load('images/map.png').convert_alpha()
        self.map = pygame.transform.rotozoom(self.map, colorToAngle[color], scale)
        
        #Load deck
        self.deck = pygame.image.load('images/deck.png').convert_alpha()
        self.deck = pygame.transform.rotozoom(self.deck, 0, scale)
    
        #Load pawns
        self.pawnYellow = pygame.image.load('images/pawn_yellow.png').convert_alpha()
        self.pawnYellow = pygame.transform.rotozoom(self.pawnYellow, 0, scale*0.5)
        self.pawnGreen = pygame.image.load('images/pawn_green.png').convert_alpha()
        self.pawnGreen = pygame.transform.rotozoom(self.pawnGreen, 0, scale*0.5)
        self.pawnRed = pygame.image.load('images/pawn_red.png').convert_alpha()
        self.pawnRed = pygame.transform.rotozoom(self.pawnRed, 0, scale*0.5)
        self.pawnBlue = pygame.image.load('images/pawn_blue.png').convert_alpha()
        self.pawnBlue = pygame.transform.rotozoom(self.pawnBlue, 0, scale*0.5)


def drawBoard(screen, board, scale):
    """
        Draw the background, the map, and the deck background in the middle
    """
    screen.blit(board.background, (0, 0))
    screen.blit(board.map, (56*scale, 56*scale))
    screen.blit(board.deck, (56*scale + 456*scale, 56*scale + 392*scale))


pygame.init()

#Create the screen
size = width, height = 960,640 #Screen size
scale = 960/2100
#screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen = pygame.display.set_mode(size)

color = 'red'
board = Board(scale, color)
drawBoard(screen, board, scale)




"""
for i in range(16):
    screen.blit(pawnYellow, (56*scale+80*i*scale, 56*scale-15*scale))
for i in range(16):
    screen.blit(pawnGreen, (56*scale+80*15*scale, 56*scale-15*scale+80*i*scale))
for i in range(16):
    screen.blit(pawnRed, (56*scale+80*i*scale, 56*scale-15*scale+80*15*scale))
for i in range(16):
    screen.blit(pawnBlue, (56*scale+80*0*scale, 56*scale-15*scale+80*i*scale))
"""


"""
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
"""

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Exit button
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #Esc
                sys.exit()

    pygame.display.update()
