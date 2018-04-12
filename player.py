#check all possible moves
#user select

import pygame, time

class Player:

    def __init__(self, main, playerIndex, playerPosition, playerColor):
        """
        Class constructor
        """
        self.main = main
        self.playerIndex = playerIndex
        self.playerPosition = playerPosition
        self.color = playerColor

        #Create pawns and store in a list
        self.pawnList = []
        for i in range(4):
            print("Create a pawn in", playerColor, "color with index", i)
            self.pawnList.append(Pawn(main, i, playerIndex, playerPosition, playerColor))

        pass

class Pawn:

    def __init__(self, main, index, playerIndex, playerPosition, color):
        """
        Class constructor
        """
        self.main = main
        self.index = index
        self.playerPosition = playerPosition
        self.playerIndex = playerIndex
        self.color = color

        #Store the coordinate map in the beginning
        self.positionMap = self.getPositionMap()

        #Put pawn in start area
        self.position = {'type': 'start', 'side': playerPosition, 'index': index}

        #Create a pawn image
        imagePath = 'images/pawn_' + color + '_small.png'
        self.pawn = pygame.image.load(imagePath).convert_alpha()
        self.pawn = pygame.transform.rotozoom(self.pawn, 0, 1)

        #Add pawn to board object
        self.layer = 2
        self.main.activeObj.add(self)

        #Movement variables
        self.moveStep = 0
        self.lastStep = 0

        pass

    def draw(self):
        """
        Draw the pawn on the screen at the corresponding position
        """
        destination = self.getCoordinate(self.position)
        self.rect = self.main.screen.blit(self.pawn, destination)

        pass

    def tick(self):
        #if there are moves this pawn needs to make, lets make one
        if(self.moveStep > 0 or self.moveStep < 0) and (time.clock() - self.lastStep > 0.35):
            offset = 0
            #debug output
            print('move ' + str(self.moveStep) + ', ' + str(self.position))
            #get destination to move to
            destination = self.getNext(self.position)
            #When sliding, the pawn bumps all pawns on the way to the start
            if self.status is 'sliding':
                self.checkCollision(destination, self.status)
            #move to the destination
            self.move(destination)
            #decrement the moves left
            if self.moveStep > 0:
                self.moveStep -= 1
            elif self.moveStep < 0:
                self.moveStep += 1
            #If the destination is on the triangle of slide section in different color, slide to the end
            if self.moveStep is 0:
                self.moveStep += self.checkSlideStep(destination)
                if self.moveStep is not 0:
                    self.status = 'sliding'
                    offset = 0.25
            #finally mark the time we made this move
            self.lastStep = offset + time.clock()


    def onClick(self):
        """
        When a pawn is clicked, this function will be called and move the pawn if possible
        """
        if (self.playerPosition is self.main.game.turn):
            #Draw a card and decide how many steps to move
            self.moveStep = self.main.game.drawCard()

            #Check if this pawn can move to the destination
            #status = moving/sliding/safe/home/notAllowed
            self.status = 'moving'
            destination = self.position
            for i in range(abs(self.moveStep)):
                destination = self.getNext(destination)
            self.status = self.checkCollision(destination, self.status)
            if self.status is 'notAllowed': #If this pawn cannot move, ignore
                self.moveStep = 0
            self.status = 'moving'
    
            #Change to next turn
            self.main.game.nextTurn()

        """
        #Move until reaching the destination
        while moveStep > 0:
            #Delay the movement
            #self.main.clock.tick(3)
            time.sleep(0.3)
            print('move ' + str(moveStep) + ', ' + str(self.position))
            self.main.processRendering()
            #Move one step at a time
            destination = self.moveForward(self.position)
            self.move(destination)
            moveStep -= 1

            #When sliding, the pawn bumps all pawns on the way to the start
            if status is 'sliding':
                self.checkCollision(destination, status)

            #If the destination is on the triangle of slide section in different color, slide to the end
            if moveStep is 0:
                moveStep += self.checkSlideStep(destination)
                if moveStep is not 0:
                    status = 'sliding'
        pass
        """

    def checkCollision(self, destination, status):
        """
        Check if the pawn will bump any pawns or overmove after entering home
        """
        #If a pawn is already at home, it cannot move
        if destination['type'] is 'wrong':
            print("Pawns cannot move to the destination")
            return 'notAllowed'

        #Check if there's any pawn at the destination
        for obj in self.main.activeObj:
            if obj is not self and obj.layer == 2 and obj.position['side'] is destination['side'] and obj.position['index'] is destination['index'] and obj.position['type'] is destination['type']:
                #If there's a pawn in the same color, this move is not allowed
                if obj.color is self.color and status is 'moving':
                    print("Pawns cannot move to the position of any other pawns in the same color")
                    return 'notAllowed'
                #If this pawn is sliding, bump all pawns, and
                #if this pawn is moving and there's a pawn in different color, bump it
                else:
                    print("Bump the pawn to the start")
                    self.bump(obj)
                    return

        return 'safe'

    def bump(self, bumpedPawn):
        """
        Bump the pawn to the start
        """
        bumpedPawn.position['type'] = 'start'
        bumpedPawn.position['side'] = bumpedPawn.playerPosition
        bumpedPawn.position['index'] = bumpedPawn.index

        pass

    def checkSlideStep(self, destination):
        """
        Return the steps to slide or return 0 if it not the triangle of a slide area
        """
        slide = 0
        #Slide
        if destination['type'] is 'track' and destination['side'] is not self.playerPosition:
            if destination['index'] is 1: #Slide 3 steps
                slide = 3
            elif destination['index'] is 9: #Slide 4 steps
                slide = 4

        return slide

    def move(self, destination):
        """
        Change the position of a pawn to the destination
        """
        self.position = destination

        pass

    def getNext(self, position):
        """
        Decide to move forward or backward based on the steps left
        """
        if self.moveStep > 0:
            destination = self.moveForward(position)
        elif self.moveStep < 0:
            destination = self.moveBackward(position)
        else:
            destination = {'type':'wrong'}

        return destination

    def moveForward(self, position):
        """
        Move forward and return the next position of current position
        """
        type = position['type']
        side = position['side']
        index = position['index']

        #If the pawn is on the track
        if type is 'track':
            if index is 14: #Move to the corner
                fourPosition = ['bottom', 'left', 'top', 'right']
                currentIndex = fourPosition.index(side)
                destination = {'type':'track', 'side':fourPosition[(currentIndex+1)%4], 'index':0}
            elif index is 2 and side is self.playerPosition: #Move to safety zone
                destination = {'type':'safetyZone', 'side':side, 'index':0}
            else: #Stay on the track
                destination = {'type':'track', 'side':side, 'index':index+1}

        #If the pawn is in safety zone
        elif type is 'safetyZone':
            if index is 4: #Move to home
                destination = {'type':'home', 'side':side, 'index':self.index}
            else: #Stay in the safety zone
                destination = {'type':'safetyZone', 'side':side, 'index':index+1}

        #If the pawn is in start
        elif type is 'start': #Move to the track
            destination = {'type':'track', 'side':side, 'index':4}

        #If the pawn is at home
        elif type is 'home': #Cannot move after entering home
            destination = {'type':'wrong'}

        return destination
    
    def moveBackward(self, position):
        """
        Move backward and return the next position of current position
        """
        type = position['type']
        side = position['side']
        index = position['index']
        
        #If the pawn is on the track
        if type is 'track':
            if index is 0: #Move back from the corner
                fourPosition = ['bottom', 'left', 'top', 'right']
                currentIndex = fourPosition.index(side)
                destination = {'type':'track', 'side':fourPosition[(currentIndex+-1+4)%4], 'index':14}
            else: #Stay on the track
                destination = {'type':'track', 'side':side, 'index':index-1}
                
        #If the pawn is in safety zone
        elif type is 'safetyZone':
            if index is 0: #Move out to track
                destination = {'type':'track', 'side':side, 'index':2}
            else: #Stay in the safety zone
                destination = {'type':'safetyZone', 'side':side, 'index':index-1}

        #If the pawn is in start
        elif type is 'start': #Cannot move backward from start
            destination = {'type':'wrong'}
            
        #If the pawn is at home
        elif type is 'home': #Cannot move backward from home
            destination = {'type':'wrong'}

        return destination

    def getCoordinate(self, position):
        """
        Find the exact coordinates of the position
        """
        type = position['type']
        side = position['side']
        index = position['index']
        coordinate = self.positionMap[type][side][index]

        return coordinate

    def getPositionMap(self):
        """
        Create a dictionary mapping position to coordinate
        """
        #Create an empty dictionary first
        position = {}
        position['track'] = {}
        position['safetyZone'] = {}
        position['start'] = {}
        position['home'] = {}
        for type in position:
            position[type]['top'] = {}
            position[type]['bottom'] = {}
            position[type]['left'] = {}
            position[type]['right'] = {}

        scale = self.main.scale

        #Set the position of the track
        for i in range(15):
            position['track']['top'][i] = [(80*i+64)*scale, 64*scale]
            position['track']['bottom'][i] = [(80*(15-i)+64)*scale, (80*15+64)*scale]
            position['track']['left'][i] = [64*scale, (80*(15-i)+64)*scale]
            position['track']['right'][i] = [(80*15+64)*scale, (80*i+64)*scale]

        #Set the position of the safetyZone
        for i in range(5):
            position['safetyZone']['top'][i] = [(80*2+64)*scale, (80*(1+i)+64)*scale]
            position['safetyZone']['bottom'][i] = [(80*13+64)*scale, (80*(14-i)+64)*scale]
            position['safetyZone']['left'][i] = [(80*i+64)*scale, (80*13+64)*scale]
            position['safetyZone']['right'][i] = [(80*(14-i)+64)*scale, (80*2+64)*scale]

        #Set the position of the start
        for i in range(2):
            position['start']['top'][i] = [(80*(3.6+i)+56)*scale, (80*(1.3)+56)*scale]
            position['start']['bottom'][i] = [(80*(10.6+i)+56)*scale, (80*(12.79)+56)*scale]
            position['start']['left'][i] = [(80*(1.33+i)+56)*scale, (80*(10.55)+56)*scale]
            position['start']['right'][i] = [(80*(12.82+i)+56)*scale, (80*(3.55)+56)*scale]
        for i in range(2):
            position['start']['top'][i+2] = [(80*(3.6+i)+56)*scale, (80*(1.3+1)+56)*scale]
            position['start']['bottom'][i+2] = [(80*(10.6+i)+56)*scale, (80*(12.79+1)+56)*scale]
            position['start']['left'][i+2] = [(80*(1.33+i)+56)*scale, (80*(10.55+1)+56)*scale]
            position['start']['right'][i+2] = [(80*(12.82+i)+56)*scale, (80*(3.55+1)+56)*scale]

        #Set the position of the home
        for i in range(2):
            position['home']['top'][i] = [(80*(1.6+i)+56)*scale, (80*(6)+56)*scale]
            position['home']['bottom'][i] = [(80*(12.6+i)+56)*scale, (80*(8.29)+56)*scale]
            position['home']['left'][i] = [(80*(5.87+i)+56)*scale, (80*(12.55)+56)*scale]
            position['home']['right'][i] = [(80*(8.3+i)+56)*scale, (80*(1.55)+56)*scale]
        for i in range(2):
            position['home']['top'][i+2] = [(80*(1.6+i)+56)*scale, (80*(6+1)+56)*scale]
            position['home']['bottom'][i+2] = [(80*(12.6+i)+56)*scale, (80*(8.29+1)+56)*scale]
            position['home']['left'][i+2] = [(80*(5.87+i)+56)*scale, (80*(12.55+1)+56)*scale]
            position['home']['right'][i+2] = [(80*(8.3+i)+56)*scale, (80*(1.55+1)+56)*scale]

        return position
