#code to write save sata to file and load it back
import pickle
from deck import Deck
from game import Game
#from main import Main
#things to save:
#player: name, position, color, pawn locations, AI setting if computer
#deck: current card, deck order
#game: current player,
#current player up
class Save:
    def __init__(self, main):
        print("Test save 1")
        self.main = main
        self.playerList = self.main.game.playerList
        print("Test save 2")


    def save(self):
        print("""Saving the game
        .Saving
        .Saving
        .Saving
        .Saving
        """)
        #player AI
        # player2_AI = main.pc1difficulty
        # player3_AI = main.pc2difficulty
        # player4_AI = main.pc3difficulty
        # self.numPlayers = ''
        # #player info?
        # player1_info = self.playerList[0]
        # #player1 pawn info. pawnlist should have its own index, playerindex, playerposition, and color
        # #just need to store pawnlist and playerlist
        # player1_pawn1_info = self.playerList[0].pawnList[0].position
        # player1_pawn2_info = self.playerList[0].pawnList[1].position
        # player1_pawn3_info = self.playerList[0].pawnList[2].position
        # player1_pawn4_info = self.playerList[0].pawnList[3].position
        #
        #
        # #player 0 which is THE player
        # player1_index = 0
        # player1_color = self.playerList[0].color
        # player1_location = self.playerList[0].playerPosition
        # player1_setting = "none"
        #
        # #pawns
        # #each pawn has type, side, and index. Type refers to in start zone, end zone, or on the track
        # #side refers to the side of the board. Each side ends at 14, and each pawn starts at
        # #index 4 of their respective side
        #
        # #can I just put these into a list like how they are created instead of all seperate, and playerdata too?
        #
        # #refers to the type of pawn
        # player1_pawn1_type = 'start'
        # player1_pawn2_type = 'start'
        # player1_pawn3_type = 'start'
        # player1_pawn4_type = 'start'
        #
        # #refers to the side a pawn is on
        # player1_pawn1_side = 'bottom'
        # player1_pawn2_side = 'bottom'
        # player1_pawn3_side = 'bottom'
        # player1_pawn4_side = 'bottom'
        #
        # #this refers to the location on a given side
        # player1_pawn1_index = self.playerList[0].pawnList[0].index
        # player1_pawn2_index = self.playerList[0].pawnList[1].index
        # player1_pawn3_index = self.playerList[0].pawnList[2].index
        # player1_pawn4_index = self.playerList[0].pawnList[3].index
        #
        #
        #
        # #assigns a given pawn to player
        # player1_pawn1_playerIndex = player1_index
        # player1_pawn2_playerIndex = player1_index
        # player1_pawn3_playerIndex = player1_index
        # player1_pawn4_playerIndex = player1_index
        #
        # #no idea what I was going with here
        # # player1_pawn1_playerLocation = player1_location
        # # player1_pawn2_playerLocation = player1_location
        # # player1_pawn3_playerLocation = player1_location
        # # player1_pawn4_playerLocation = player1_location
        #
        # player1_pawn1_color = player1_color
        # player1_pawn2_color = player1_color
        # player1_pawn3_color = player1_color
        # player1_pawn4_color = player1_color
        #

        # print("")
        # print (player1_color)
        # print(player1_location)
        # print(player1_pawn1_location)
        # print(player1_pawn2_location)
        # print("")

        # #player 2
        # player2_index = 1
        # player2_color = self.playerList[1].color
        # player2_location = self.playerList[1].playerPosition
        # player2_setting = "hard"
        # player2_pawn1_location = self.playerList[1].pawnList[0].position
        # player2_pawn2_location = self.playerList[1].pawnList[1].position
        # player2_pawn3_location = self.playerList[1].pawnList[2].position
        # player2_pawn4_location = self.playerList[1].pawnList[3].position
        #
        # #player 3
        # player3_index = 2
        # player3_color = self.playerList[2].color
        # player3_location = self.playerList[2].playerPosition
        # player3_setting = "hard"
        # player3_pawn1_location = self.playerList[2].pawnList[0].position
        # player3_pawn2_location = self.playerList[2].pawnList[1].position
        # player3_pawn3_location = self.playerList[2].pawnList[2].position
        # player3_pawn4_location = self.playerList[2].pawnList[3].position
        #
        # #player 4
        # player4_index = 3
        # player4_color = self.playerList[3].color
        # player4_location = self.playerList[3].playerPosition
        # player4_setting = "hard"
        # player4_pawn1_location = self.playerList[3].pawnList[0].position
        # player4_pawn2_location = self.playerList[3].pawnList[1].position
        # player4_pawn3_location = self.playerList[3].pawnList[2].position
        # player4_pawn4_location = self.playerList[3].pawnList[3].position

        #deck information
        #deck order, current card
        print("Saving deck")
        #deck=Deck(self.main)
        deck_order = self.main.deck.deck
        #deck_order = deck.deck
        current_card = self.main.deck.current_card
        card_index = self.main.deck.card_index

        print("Deck order: ", deck_order)
        print("Current card: ", current_card)
        print("Card index: ", card_index)

        print("Deck saved")
        info = {
            # "player1_info" : player1_info,
            # "player1_pawn1_info" : player1_pawn1_info,
            # "player1_pawn2_info" : player1_pawn2_info,
            # "player1_pawn3_info" : player1_pawn3_info,
            # "player1_pawn4_info" : player1_pawn4_info,


            # "player1_color": player1_color,
            # "player1_location" : player1_location,
            # "player1_setting" : player1_setting,
            # "player1_pawn1_location": player1_pawn1_location,
            # "player1_pawn2_location" : player1_pawn2_location,
            # "player1_pawn3_location" : player1_pawn3_location,
            # "player1_pawn4_location" : player1_pawn4_location,
            #
            # "player2_color": player2_color,
            # "player2_location" : player2_location,
            # "player2_setting" : player2_setting,
            # "player2_pawn1_location": player2_pawn1_location,
            # "player2_pawn2_location" : player2_pawn2_location,
            # "player2_pawn3_location" : player2_pawn3_location,
            # "player2_pawn4_location" : player2_pawn4_location,
            #
            # "player3_color": player3_color,
            # "player3_location" : player3_location,
            # "player3_setting" : player3_setting,
            # "player3_pawn1_location": player3_pawn1_location,
            # "player3_pawn2_location" : player3_pawn2_location,
            # "player3_pawn3_location" : player3_pawn3_location,
            # "player3_pawn4_location" : player3_pawn4_location,
            #
            # "player4_color": player4_color,
            # "player4_location" : player4_location,
            # "player4_setting" : player4_setting,
            # "player4_pawn1_location": player4_pawn1_location,
            # "player4_pawn2_location" : player4_pawn2_location,
            # "player4_pawn3_location" : player4_pawn3_location,
            # "player4_pawn4_location" : player4_pawn4_location,

            # "deck_order" : deck_order,
            # "card_index" : card_index,
            # "current_card" : current_card
            }

        pickle_out = open ("save.txt", "wb")
        pickle.dump(info, pickle_out)
        pickle_out.close()


        print ("Game Saved")

#if(__name__ == "__main__"):
#    main = ""
#    app = Save(main)
