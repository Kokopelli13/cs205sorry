import pygame

class Playing:

    def __init__(self, main, turn, player, playerNum):
        """
        Class constructor
        """
        ####################Player####################
        
        #Get player's information
        self.main = main
        self.playerIndex = player.playerIndex
        self.playerPosition = player.playerPosition
        self.color = player.color
        
        #Create a pawn image
        imagePath = 'images/pawn_' + self.color + '.png'
        self.pawn = pygame.image.load(imagePath).convert_alpha()
        self.pawn = pygame.transform.rotozoom(self.pawn, 0, 0.3)
        
        #Create a list of player's information
        self.playerInfoList = self.getPlayerInfoList(playerNum)
        
        ####################Card####################
        
        #Create a card area
        self.faceUpCardList = []
        self.faceDownCard = pygame.image.load('images/topofcard_small.png').convert_alpha()
        self.faceDownCard = pygame.transform.rotozoom(self.faceDownCard, 0, 0.09)
        cardList = ['Sorry!', 1, 2, 3, 4, 5, '', 7, 8, '', 10, 11, 12]
        
        self.faceUpCardList.append(pygame.image.load('images/cardSorry!_small.png').convert_alpha())
        self.faceUpCardList[0] = pygame.transform.rotozoom(self.faceUpCardList[0], 0, 0.09)
        for i in range(1,13):
            if i in [6, 9]:
                self.faceUpCardList.append('')
            else:
                self.faceUpCardList.append(pygame.image.load('images/card' + str(cardList[i]) + '_small.png').convert_alpha())
                self.faceUpCardList[i] = pygame.transform.rotozoom(self.faceUpCardList[i], 0, 0.09)

        self.card = self.faceDownCard

        ####################Objects####################

        #Add playing information to board object
        self.layer = 4
        self.main.activeObj.add(self)

        ####################Status####################

        #Show if this player has drawn a card
        self.drawCardBool = False
        #Show if this player is ready to pick a pawn
        self.readyToPickPawnBool = False
        #This player is ready to pick his/her pawns or an opponent's pawns
        self.pick = ''
        #Show if this player has picked a pawn
        self.pickedPawnBool = False
        #Show if player can enter relaxed start mode
        self.relaxedStartbool = True
        
        ####################Card####################
        
        #Show card information
        self.cardInfoList = []
        self.cardInfoList.append(Text(self.main, 750, 150, 14, 'Draw a card', False))
        
        ####################Messages####################
        
        #Show option information
        self.optionInfoList = []
        #Show information
        self.infoList = []
        
        ####################Buttons####################
        
        #Add needed buttons
        self.drawButton = PlayingButton(self.main, 750, 175, "draw", "images/draw.png", 0.8, True)
        self.optionButton1 = PlayingButton(self.main, 660, 250, "option1", "images/option.png", 0.8, False)
        self.optionButton2 = PlayingButton(self.main, 660, 300, "option2", "images/option.png", 0.8, False)
        #Add relaxed start button
        self.relaxedButton = PlayingButton(self.main, 670, 550, "relaxed", "images/relaxedstart.png", 0.8, True)
        #Add skip button
        self.skipButton = PlayingButton(self.main, 670, 500, "skip", "images/skip.png", 0.8, True)
        #Add quit button
        self.quitButton = PlayingButton(self.main, 805, 550, "quit", "images/quit.png", 0.8, True)
        #add save button
        self.saveButton = PlayingButton(self.main, 805, 500, "save", "images/save.png", 0.8, True)

        self.numButton1 = PlayingButton(self.main, 680, 400, "num1", "images/1.png", 0.8, False)
        self.numButton2 = PlayingButton(self.main, 720, 400, "num2", "images/2.png", 0.8, False)
        self.numButton3 = PlayingButton(self.main, 760, 400, "num3", "images/3.png", 0.8, False)
        self.numButton4 = PlayingButton(self.main, 800, 400, "num4", "images/4.png", 0.8, False)
        self.numButton5 = PlayingButton(self.main, 840, 400, "num5", "images/5.png", 0.8, False)
        self.numButton6 = PlayingButton(self.main, 880, 400, "num6", "images/6.png", 0.8, False)


        pass

    def initialize(self):
        """
        Initialize all needed variables
        """
        self.card = self.faceDownCard
        
        #Show if this player is ready to pick a pawn
        self.readyToPickPawnBool = False
        #This player is ready to pick his/her pawns or an opponent's pawns
        self.pick = ''
        #Show if this player has picked a pawn
        self.pickedPawnBool = False
        
        #Show card information
        self.cardInfoList.clear()
        if self.drawCardBool is False:
            self.cardInfoList.append(Text(self.main, 750, 150, 14, 'Draw a card', False))
        else:
            self.cardInfoList.append(Text(self.main, 750, 150, 14, 'Draw the second card', False))
            #self.drawCardBool = False
            
        #Show option information
        self.optionInfoList.clear()
    
        #Show information
        self.infoList.clear()

        self.drawButton.visible = True
        self.optionButton1.visible = False
        self.optionButton2.visible = False
        
        self.drawnCard = None

        pass

    def draw(self):
        """
        Draw the playing information on the screen at the corresponding position
        """
        self.rect = self.main.screen.blit(self.pawn, (670, 60))
        self.rect = self.main.screen.blit(self.card, (660, 150))

        for playerInfo in self.playerInfoList[self.playerIndex]:
            playerInfo.draw()
        for cardInfo in self.cardInfoList:
            cardInfo.draw()
        for optionInfo in self.optionInfoList:
            optionInfo.draw()
        for info in self.infoList:
            info.draw()
        
        pass
    
    def onClick(self):
        pass

    def tick(self):
        pass

    def nextTurn(self, turn, player):
        """
        Show new information for the player of next turn
        """
        self.playerIndex = player.playerIndex
        self.playerPosition = player.playerPosition
        self.color = player.color
        
        #Create a pawn image
        imagePath = 'images/pawn_' + self.color + '.png'
        self.pawn = pygame.image.load(imagePath).convert_alpha()
        self.pawn = pygame.transform.rotozoom(self.pawn, 0, 0.3)
        
        self.initialize()
        
        #Check if the player can enter relaxed start mode
        if self.relaxedStartbool is True:
            for i in range(self.main.game.playerNum):
                for j in range(4):
                    if self.main.game.playerList[i].pawnList[j].position['type'] != 'start':
                        self.relaxedStartbool = False
                        self.relaxedButton.visible = False
                        break
        
        pass
    
    def getPlayerInfoList(self, playerNum):
        """
        Create a list of player's information
        """
        playerInfoList = []
        #Player
        playerInfoList.append(list())
        playerInfoList[0].append(Text(self.main, 750, 55, 14, 'Player: You', True))
        playerInfoList[0].append(Text(self.main, 750, 77, 14, 'Position: Bottom', True))
        playerInfoList[0].append(Text(self.main, 750, 99, 14, 'Setting: Genius', True))
        #Computer
        setting = ['', self.main.pc1difficulty, self.main.pc2difficulty, self.main.pc3difficulty]
        fourPosition = ['bottom', 'left', 'top', 'right']
        for i in range(1, playerNum):
            playerInfoList.append(list())
            playerInfoList[i].append(Text(self.main, 750, 55, 14, 'Player: Computer', True))
            
            position = fourPosition[i][0].upper() + fourPosition[i][1:]
            playerInfoList[i].append(Text(self.main, 750, 77, 14, 'Position: '+position, True))
            
            formatSetting = setting[i][0].upper() + setting[i][1:4] + ' & ' + setting[i][4].upper() + setting[i][5:]
            playerInfoList[i].append(Text(self.main, 750, 99, 14, 'Setting: '+formatSetting, True))
        
        return playerInfoList

    def processOption(self, pawn):
        """
        Process option for the pawn
        """
        if self.drawnCard is not 2 and self.drawCardBool is True:
            self.drawCardBool = False
        
        if self.drawnCard is 'Sorry!' or self.drawnCard is 0:
            #Select own pawn in START
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and pawn.position['type'] is 'start':
                self.pickedPawn = pawn
                self.pickedPawnBool = True
                self.readyToPickPawnBool = True
                self.pick = 'opponent'
                
                self.infoList.clear()
                self.main.game.playing.infoList.append(Text(self.main, 700, 370, 16, 'Select opponent\'s pawn', False))
            #Select opponent's pawn to BUMP to Start
            elif self.pick is 'opponent' and pawn.playerPosition is not self.main.game.turn and self.pickedPawnBool is True and pawn.position['type'] is 'track':
                tmp = {}
                tmp['type'] = pawn.position['type']
                tmp['side'] = pawn.position['side']
                tmp['index'] = pawn.position['index']
                
                pawn.position['type'] = 'start'
                pawn.position['side'] = pawn.playerPosition
                pawn.position['index'] = pawn.index
                
                self.pickedPawn.position = tmp
                self.pickedPawn.tryToMove(0, True)
                
                self.readyToPickPawnBool = False
                self.pick = ''
                self.pickedPawnBool = False
        elif self.drawnCard is 1:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn:
                if self.option is 1 and pawn.position['type'] is 'start':
                    pawn.tryToMove(1, True)
                    self.infoList.clear()
                elif self.option is 2 and pawn.position['type'] is not 'start':
                    pawn.tryToMove(1, True)
                    self.infoList.clear()
        elif self.drawnCard is 2:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn:
                if self.option is 1 and pawn.position['type'] is 'start':
                    pawn.tryToMove(1, True)
                    self.initialize()
                    self.infoList.clear()
                elif self.option is 2 and pawn.position['type'] is 'track':
                    pawn.tryToMove(2, True)
                    self.initialize()
                    self.infoList.clear()
                #For the player to draw again
                if pawn.playerPosition is not self.main.game.turn and self.drawCardBool is True:
                    for i in range(self.main.game.playerNum - 1):
                        self.main.game.nextTurn(True)
        elif self.drawnCard is 3:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and pawn.position['type'] is not 'start':
                pawn.tryToMove(3, True)
        elif self.drawnCard is 4:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and pawn.position['type'] is not 'start':
                pawn.tryToMove(-4, True)
        elif self.drawnCard is 5:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and pawn.position['type'] is not 'start':
                pawn.tryToMove(5, True)

        elif self.drawnCard is 7:
            #Select own pawn to move forward
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and self.option is 1 and pawn.position['type'] is not 'start':
                pawn.tryToMove(7, True)
                self.infoList.clear()
            #Select first pawn to move
            elif self.pick is 'own' and pawn.playerPosition is self.main.game.turn and self.option is 2 and self.pickedPawnBool is False and pawn.position['type'] is not 'start':
                self.pickedPawn = pawn
                self.pickedPawnBool = True
                self.readyToPickPawnBool = True
                self.pick = 'own'
                
                self.infoList.clear()
                self.main.game.playing.infoList.append(Text(self.main, 700, 370, 16, 'How many steps to move?', False))
                self.numButton1.visible = True
                self.numButton2.visible = True
                self.numButton3.visible = True
                self.numButton4.visible = True
                self.numButton5.visible = True
                self.numButton6.visible = True
            #Select second pawn to move
            elif self.pick is 'own' and pawn.playerPosition is self.main.game.turn and self.option is 2 and self.pickedPawnBool is True and pawn.position['type'] is not 'start':
                pawn.tryToMove(7-self.pickedNum, True)
                
                #Fail to move
                if pawn.playerPosition is self.main.game.turn:
                    self.readyToPickPawnBool = False
                    self.pick = 'own'
                    self.pickedPawnBool = False
                    self.pickedPawn.position = self.originalPosition
                    self.infoList.clear()
                    self.optionButton2.processOption(7, 2)

        elif self.drawnCard is 8:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and pawn.position['type'] is not 'start':
                pawn.tryToMove(8, True)
        elif self.drawnCard is 10:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn:
                if self.option is 1 and pawn.position['type'] is not 'start':
                    pawn.tryToMove(10, True)
                    self.infoList.clear()
                elif self.option is 2 and pawn.position['type'] is not 'start':
                    pawn.tryToMove(-1, True)
                    self.infoList.clear()

        elif self.drawnCard is 11:
            #Select own pawn to move forward
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and self.option is 1 and pawn.position['type'] is not 'start':
                pawn.tryToMove(11, True)
                self.infoList.clear()
            #Select own pawn to switch
            elif self.pick is 'own' and pawn.playerPosition is self.main.game.turn and self.option is 2 and pawn.position['type'] is not 'start':
                self.pickedPawn = pawn
                self.pickedPawnBool = True
                self.readyToPickPawnBool = True
                self.pick = 'opponent'

                self.infoList.clear()
                self.main.game.playing.infoList.append(Text(self.main, 700, 370, 16, 'Select opponent\'s pawn', False))
            #Select opponent's pawn to switch
            elif self.pick is 'opponent' and pawn.playerPosition is not self.main.game.turn and self.option is 2 and self.pickedPawnBool is True and pawn.position['type'] is 'track':
                tmp = {'type': pawn.position['type'], 'side': pawn.position['side'], 'index': pawn.position['index']}
                pawn.position = self.pickedPawn.position
                self.pickedPawn.position = tmp
                pawn.tryToMove(0, True)
                
                self.readyToPickPawnBool = False
                self.pick = ''
                self.pickedPawnBool = False
                    
        elif self.drawnCard is 12:
            if self.pick is 'own' and pawn.playerPosition is self.main.game.turn and pawn.position['type'] is not 'start':
                pawn.tryToMove(12, True)

        pass

class PlayingButton:
    def __init__(self, main, x, y, action, img, scale, visible):
        """
        Class constructor
        """
        self.action = action
        self.main = main
        self.x, self.y = x, y
        self.layer = 4
        self.main.activeObj.add(self)
        self.scale = scale
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, self.scale)
        self.visible = visible
    
    def draw(self):
        if self.visible is True:
            self.rect = self.main.screen.blit(self.img, (self.x, self.y))
        else:
            self.rect = self.main.screen.blit(self.main.game.playing.pawn, (670, 60))
        
        pass
    
    
    def tick(self):
        pass
    
    def onClick(self):
        if self.visible is True:
            if self.action == "draw":
                self.drawCard()
            elif self.action == "option1":
                self.main.game.playing.infoList.clear()
                self.main.game.playing.option = 1
                self.processOption(self.main.game.playing.drawnCard, 1)
            elif self.action == "option2":
                self.main.game.playing.infoList.clear()
                self.main.game.playing.option = 2
                self.processOption(self.main.game.playing.drawnCard, 2)
            elif self.action == "skip":
                self.main.game.playing.drawCardBool = False
                self.main.game.nextTurn(True)
            elif self.action == "relaxed":
                for i in range(self.main.game.playerNum):
                    self.main.game.playerList[i].pawnList[0].position['type'] = 'track'
                    self.main.game.playerList[i].pawnList[0].position['index'] = 4
                    self.visible = False
            elif self.action == "quit":
                self.main.quit()
            elif self.action == "save":
                self.main.save.save()
            elif self.action == "num1":
                self.processCard7(1)
            elif self.action == "num2":
                self.processCard7(2)
            elif self.action == "num3":
                self.processCard7(3)
            elif self.action == "num4":
                self.processCard7(4)
            elif self.action == "num5":
                self.processCard7(5)
            elif self.action == "num6":
                self.processCard7(6)
        pass

    def drawCard(self):
        """
        Draw a card, change the image, and show card information
        """
        card = self.main.game.drawCard()

        self.main.game.playing.drawnCard = card
        if card is 'Sorry!' or card is 0:
            self.main.game.playing.card = self.main.game.playing.faceUpCardList[0]
        else:
            self.main.game.playing.card = self.main.game.playing.faceUpCardList[card]

        #This player has drawn a card
        self.main.game.playing.drawCardBool = True
        self.visible = False

        #Show card information
        self.main.game.playing.cardInfoList.clear()
        self.getCardInfo(card)
        
        #Let player to choose an option to move
        self.main.game.playing.optionInfoList.clear()
        self.moveOptionInfo(card)

        return card

    def moveOptionInfo(self, card):
        """
        Let player to choose an option to move
        """
        if card is 'Sorry!' or card is 0:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Select a pawn', False))
            self.main.game.playing.optionButton2.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 312, 14, 'Skip', False))
        elif card is 1:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Start a pawn', False))
            self.main.game.playing.optionButton2.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 312, 14, 'Move a pawn', False))
        elif card is 2:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Start a pawn', False))
            self.main.game.playing.optionButton2.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 312, 14, 'Move a pawn', False))
        elif card is 3:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn', False))
        elif card is 4:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn', False))
        elif card is 5:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn', False))
        elif card is 7:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn', False))
            self.main.game.playing.optionButton2.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 312, 14, 'Move two pawns', False))
        elif card is 8:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn', False))
        elif card is 10:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn forward', False))
            self.main.game.playing.optionButton2.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 312, 14, 'Move a pawn backward', False))
        elif card is 11:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn', False))
            self.main.game.playing.optionButton2.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 312, 14, 'Switch a pawn ', False))
        elif card is 12:
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionInfoList.append(Text(self.main, 790, 262, 14, 'Move a pawn', False))
        
        pass

    def processOption(self, card, option):
        """
        Process this option if player has to choose two pawns
        """
        if card is 'Sorry!' or card is 0:
            if option is 1:
                self.main.game.playing.readyToPickPawnBool = True
                self.main.game.playing.pick = 'own'
            else:
                self.main.game.nextTurn(True)
    
        elif card in [1,2,3,4,5,7,8,10,11,12]:
            if card is 7 and self.main.game.playing.pickedPawnBool is True:
                #Return from option 2 to option 1
                self.main.game.playing.pickedPawnBool = False
                self.main.game.playing.pickedPawn.position = self.main.game.playing.originalPosition
            self.main.game.playing.readyToPickPawnBool = True
            self.main.game.playing.pick = 'own'

        if card is 7 and option is 2:
            self.main.game.playing.infoList.append(Text(self.main, 720, 370, 16, 'Select the first pawn', False))
        else:
            self.main.game.playing.infoList.append(Text(self.main, 750, 370, 16, 'Select a pawn', False))
        pass

    def processCard7(self, number):
        """
        Store original position, move the first pawn, and hide number buttons
        """
        self.main.game.playing.pickedNum = number
        
        #Store the original position
        position = self.main.game.playing.pickedPawn.position
        self.main.game.playing.originalPosition = {'type': position['type'], 'side': position['side'], 'index': position['index']}
        self.main.game.playing.originalPawn = self.main.game.playing.pickedPawn
        
        self.main.game.playing.pickedPawn.tryToMove(number, False)
        
        #If the pawn can move successfully, then player can select the next pawn
        if self.main.game.playing.pickedPawn.moveStep is not 0:
            self.main.game.playing.infoList.clear()
            self.main.game.playing.infoList.append(Text(self.main, 660, 370, 16, 'Select the second pawn to move '+str(7-number), False))
            self.main.game.playing.numButton1.visible = False
            self.main.game.playing.numButton2.visible = False
            self.main.game.playing.numButton3.visible = False
            self.main.game.playing.numButton4.visible = False
            self.main.game.playing.numButton5.visible = False
            self.main.game.playing.numButton6.visible = False
    
        pass
    
    def getCardInfo(self, card):
        """
        Show card information
        """
        if card is 'Sorry!' or card is 0:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Take one pawn from your START,', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'place it on any space that is', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'occupied by any opponent, and', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 210, 13, 'BUMP that opponent’spawn', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 230, 13, 'back to its START.', False))
        elif card is 1:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either start a pawn OR move', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'one pawn forward 1 space.', False))
        elif card is 2:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either start a pawn OR move one', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'pawn forward 2 spaces. Whichever', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'you do or even if you couldn’t', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 210, 13, 'move—DRAW GAIN and move', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 230, 13, 'accordingly.', False))
        elif card is 3:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 3 spaces.', False))
        elif card is 4:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn backward 4 spaces.', False))
        elif card is 5:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 5 spaces.', False))
        elif card is 7:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either move one pawn forward 7', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'spaces—OR split the forward', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'move between any two pawns.', False))
        elif card is 8:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 8 spaces.', False))
        elif card is 10:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either move one pawn forward 10', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'spaces—OR move one pawn', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'backward 1 space.', False))

        elif card is 11:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 11 spaces', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, '—OR switch any one of your pawns', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'with one of any opponent’s.', False))
        elif card is 12:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 12 spaces', False))

        pass

class Text:
    def __init__(self, main, x, y, size, text, underLine):
        self.main = main
        self.x, self.y = x, y
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.font.set_underline(underLine)
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.layer = 4
    
    def draw(self):
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.main.screen.blit(self.textSurface, (self.x, self.y))
    
    def tick(self):
        pass
    
    def onClick(self):
        pass
