#code to write save sata to file and load it back
import pickle
from deck import Deck
from game import Game
#things to save:
#player: name, position, color, pawn locations, AI setting if computer
#deck: current card, deck order
#game: current player,
#current player up
class Save:
    def __init__(self, main):
        self.main = main
        self.playerList = self.main.game.playerList

    def save(self):
        #for i in len(playerList):
        #    color = playerList[i].color
        #    player1_location = playerList[i].playerPosition



        #player 0 which is THE player
        player1_index = 0
        player1_color = self.playerList[0].color
        player1_location = self.playerList[0].playerPosition
        player1_setting = "none"
        #pawns
        player1_pawn1_index = 0
        player1_pawn2_index = 1
        player1_pawn3_index = 2
        player1_pawn4_index = 3

        player1_pawn1_playerIndex = player1_index
        player1_pawn2_playerIndex = player1_index
        player1_pawn3_playerIndex = player1_index
        player1_pawn4_playerIndex = player1_index

        player1_pawn1_playerLocation = player1_location
        player1_pawn2_playerLocation = player1_location
        player1_pawn3_playerLocation = player1_location
        player1_pawn4_playerLocation = player1_location

        player1_pawn1_color = player1_color
        player1_pawn2_color = player1_color
        player1_pawn3_color = player1_color
        player1_pawn4_color = player1_color
        
        player1_pawn1_location = self.playerList[0].pawnList[0].position
        player1_pawn2_location = self.playerList[0].pawnList[1].position
        player1_pawn3_location = self.playerList[0].pawnList[2].position
        player1_pawn4_location = self.playerList[0].pawnList[3].position

        print("")
        print (player1_color)
        print(player1_location)
        print(player1_pawn1_location)
        print(player1_pawn2_location)
        print("")

        #player 2
        player2_index = 1
        player2_color = self.playerList[1].color
        player2_location = self.playerList[1].playerPosition
        player2_setting = "hard"
        player2_pawn1_location = self.playerList[1].pawnList[0].position
        player2_pawn2_location = self.playerList[1].pawnList[1].position
        player2_pawn3_location = self.playerList[1].pawnList[2].position
        player2_pawn4_location = self.playerList[1].pawnList[3].position

        #player 3
        player3_index = 2
        player3_color = self.playerList[2].color
        player3_location = self.playerList[2].playerPosition
        player3_setting = "hard"
        player3_pawn1_location = self.playerList[2].pawnList[0].position
        player3_pawn2_location = self.playerList[2].pawnList[1].position
        player3_pawn3_location = self.playerList[2].pawnList[2].position
        player3_pawn4_location = self.playerList[2].pawnList[3].position

        #player 4
        player4_index = 3
        player4_color = self.playerList[3].color
        player4_location = self.playerList[3].playerPosition
        player4_setting = "hard"
        player4_pawn1_location = self.playerList[3].pawnList[0].position
        player4_pawn2_location = self.playerList[3].pawnList[1].position
        player4_pawn3_location = self.playerList[3].pawnList[2].position
        player4_pawn4_location = self.playerList[3].pawnList[3].position

        #deck information
        #deck order, current card
        deck=Deck(self.main)
        deck_order = deck.deck
        card_index = deck.card_index
        current_card = deck.current_card

        info = {
            "player1_color": player1_color,
            "player1_location" : player1_location,
            "player1_setting" : player1_setting,
            "player1_pawn1_location": player1_pawn1_location,
            "player1_pawn2_location" : player1_pawn2_location,
            "player1_pawn3_location" : player1_pawn3_location,
            "player1_pawn4_location" : player1_pawn4_location,

            "player2_color": player2_color,
            "player2_location" : player2_location,
            "player2_setting" : player2_setting,
            "player2_pawn1_location": player2_pawn1_location,
            "player2_pawn2_location" : player2_pawn2_location,
            "player2_pawn3_location" : player2_pawn3_location,
            "player2_pawn4_location" : player2_pawn4_location,

            "player3_color": player3_color,
            "player3_location" : player3_location,
            "player3_setting" : player3_setting,
            "player3_pawn1_location": player3_pawn1_location,
            "player3_pawn2_location" : player3_pawn2_location,
            "player3_pawn3_location" : player3_pawn3_location,
            "player3_pawn4_location" : player3_pawn4_location,

            "player4_color": player4_color,
            "player4_location" : player4_location,
            "player4_setting" : player4_setting,
            "player4_pawn1_location": player4_pawn1_location,
            "player4_pawn2_location" : player4_pawn2_location,
            "player4_pawn3_location" : player4_pawn3_location,
            "player4_pawn4_location" : player4_pawn4_location,

            "deck_order" : deck_order,
            "card_index" : card_index,
            "current_card" : current_card
            }

        pickle_out = open ("save.txt", "wb")
        pickle.dump(info, pickle_out)
        pickle_out.close()


        print ("Game Saved")

#if(__name__ == "__main__"):
#    main = ""
#    app = Save(main)
