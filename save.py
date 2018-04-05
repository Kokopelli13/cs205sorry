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


        print('test')
        print(self.playerList)
        #for i in len(playerList):
        #    color = playerList[i].color
        #    player1_location = playerList[i].playerPosition



        #player 0 which is THE player
        player0_color = self.playerList[0].color

        print("")
        print (player0_color)
        print("")

        player0_location = self.playerList[0].playerPosition
        player0_setting = "none"
        player0_pawn0_location = self.playerList[0].pawnList[0].position
        player0_pawn1_location = self.playerList[0].pawnList[1].position
        player0_pawn2_location = self.playerList[0].pawnList[2].position
        player0_pawn3_location = self.playerList[0].pawnList[3].position

        #player 2
        player2_color = "orange"
        player2_location = "left"
        player2_setting = "hard"
        player2_pawn1_location = "1"
        player2_pawn2_location = "2"
        player2_pawn3_location = "3"
        player2_pawn4_location = "4"

        #player 3
        player3_color = "yellow"
        player3_location = "up"
        player3_setting = "easy"
        player3_pawn1_location = "1"
        player3_pawn2_location = "2"
        player3_pawn3_location = "3"
        player3_pawn4_location = "4"

        #player 4
        player4_color = "green"
        player4_location = "right"
        player4_setting = "nice"
        player4_pawn1_location = "1"
        player4_pawn2_location = "2"
        player4_pawn3_location = "3"
        player4_pawn4_location = "4"

        #deck information
        #deck order, current card
        deck=Deck(self.main)
        deck_order = deck.deck
        current_card = "1"

        info = {
            "player0_color": player0_color,
            "player0_location" : player0_location,
            "player0_setting" : player0_setting,
            "player0_pawn1_location": player0_pawn0_location,
            "player0_pawn2_location" : player0_pawn1_location,
            "player0_pawn3_location" : player0_pawn2_location,
            "player0_pawn4_location" : player0_pawn3_location,

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
            "current_card" : current_card
            }

        pickle_out = open ("save.txt", "wb")
        pickle.dump(info, pickle_out)
        pickle_out.close()


        print ("Game Saved")

#if(__name__ == "__main__"):
#    main = ""
#    app = Save(main)
