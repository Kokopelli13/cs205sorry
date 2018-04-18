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
        self.main = main
        self.playerList = self.main.game.playerList


    def save(self):
        print("")
        print("""Saving the game""")
        #player AI
        num_players = self.main.numPlayers
        player2_AI = self.main.pc1difficulty
        player3_AI = self.main.pc2difficulty
        player4_AI = self.main.pc3difficulty
        print(player2_AI)
        if num_players == "two":
            num_players = 2
            print(player3_AI)
        if num_players == "three":
            num_players = 3
            print(player3_AI)
            print(player4_AI)
        else:
            num_players = 1
        print("Numbers of computer players: ", num_players)

        # #player 0 which is THE player
        print("Player 1 information")
        player1_index = self.playerList[0].playerIndex
        player1_color = self.playerList[0].color
        player1_location = self.playerList[0].playerPosition
        player1_setting = "none"
        print(player1_color)
        print(player1_location)

        # #player1 pawn info. pawnlist should have its own index, playerindex, playerposition, and color
        # #just need to store pawnlist and playerlist
        player1_pawn1_info = self.playerList[0].pawnList[0].position
        player1_pawn2_info = self.playerList[0].pawnList[1].position
        player1_pawn3_info = self.playerList[0].pawnList[2].position
        player1_pawn4_info = self.playerList[0].pawnList[3].position
        print(player1_pawn1_info)
        print(player1_pawn2_info)
        print(player1_pawn3_info)
        print(player1_pawn4_info)
        #
        #

        #
        # #pawns
        # #each pawn has type, side, and index. Type refers to in start zone, end zone, or on the track
        # #side refers to the side of the board. Each side ends at 14, and each pawn starts at
        # #index 4 of their respective side
        #
        # #can I just put these into a list like how they are created instead of all seperate, and playerdata too?
        #

        #
        #
        #
        # #assigns a given pawn to player
        # player1_pawn1_playerIndex = player1_index
        # player1_pawn2_playerIndex = player1_index
        # player1_pawn3_playerIndex = player1_index
        # player1_pawn4_playerIndex = player1_index



        # #player 2
        # #player 0 which is THE player
        print("Player 2 information")
        player2_index = self.playerList[1].playerIndex
        player2_color = self.playerList[1].color
        player2_location = self.playerList[1].playerPosition
        player2_setting = "none"
        print(player2_color)
        print(player2_location)

        # #player1 pawn info. pawnlist should have its own index, playerindex, playerposition, and color
        # #just need to store pawnlist and playerlist
        player2_pawn1_info = self.playerList[1].pawnList[0].position
        player2_pawn2_info = self.playerList[1].pawnList[1].position
        player2_pawn3_info = self.playerList[1].pawnList[2].position
        player2_pawn4_info = self.playerList[1].pawnList[3].position
        print(player2_pawn1_info)
        print(player2_pawn2_info)
        print(player2_pawn3_info)
        print(player2_pawn4_info)
        #

        if num_players > 1:
            # #player 3
            # #player 0 which is THE player
            print("Player 3 information")
            player3_index = self.playerList[2].playerIndex
            player3_color = self.playerList[2].color
            player3_location = self.playerList[2].playerPosition
            player3_setting = "none"
            print(player3_color)
            print(player3_location)

            # #player1 pawn info. pawnlist should have its own index, playerindex, playerposition, and color
            # #just need to store pawnlist and playerlist
            player3_pawn1_info = self.playerList[2].pawnList[0].position
            player3_pawn2_info = self.playerList[2].pawnList[1].position
            player3_pawn3_info = self.playerList[2].pawnList[2].position
            player3_pawn4_info = self.playerList[2].pawnList[3].position
            print(player3_pawn1_info)
            print(player3_pawn2_info)
            print(player3_pawn3_info)
            print(player3_pawn4_info)
        #

        if num_players > 2:
            # #player 4
            # #player 0 which is THE player
            print("Player 4 information")
            player4_index = self.playerList[3].playerIndex
            player4_color = self.playerList[3].color
            player4_location = self.playerList[3].playerPosition
            player4_setting = "none"
            print(player4_color)
            print(player4_location)

            # #player1 pawn info. pawnlist should have its own index, playerindex, playerposition, and color
            # #just need to store pawnlist and playerlist
            player4_pawn1_info = self.playerList[3].pawnList[0].position
            player4_pawn2_info = self.playerList[3].pawnList[1].position
            player4_pawn3_info = self.playerList[3].pawnList[2].position
            player4_pawn4_info = self.playerList[3].pawnList[3].position
            print(player4_pawn1_info)
            print(player4_pawn2_info)
            print(player4_pawn3_info)
            print(player4_pawn4_info)

        #deck information
        #deck order, current card
        print("Saving deck")
        #deck=Deck(self.main)
        deck_order = self.main.deck.deck
        #deck_order = deck.deck
        current_card = self.main.deck.current_card
        card_index = self.main.deck.i

        print("Deck order: ", deck_order)
        print("Current card: ", current_card)
        print("Card index: ", card_index)

        print("Deck saved")
        info = {
            #game info
            "num_players" : num_players,


            #player1 info
            "player1_index" : player1_index,
            "player1_color": player1_color,
            "player1_location" : player1_location,
            "player1_pawn1_info" : player1_pawn1_info,
            "player1_pawn2_info" : player1_pawn2_info,
            "player1_pawn3_info" : player1_pawn3_info,
            "player1_pawn4_info" : player1_pawn4_info,


            #player2 info
            "player2_AI" : player2_AI,
            "player2_index" : player2_index,
            "player2_color": player2_color,
            "player2_location" : player2_location,
            "player2_pawn1_info" : player2_pawn1_info,
            "player2_pawn2_info" : player2_pawn2_info,
            "player2_pawn3_info" : player2_pawn3_info,
            "player2_pawn4_info" : player2_pawn4_info,
            #

            "deck_order" : deck_order,
            "card_index" : card_index,
            "current_card" : current_card
            }

        if num_players > 1:
            player3_dict = {
                #player3 info
                "player3_AI" : player3_AI,
                "player3_index" : player3_index,
                "player3_color": player3_color,
                "player3_location" : player3_location,
                "player3_pawn1_info" : player3_pawn1_info,
                "player3_pawn2_info" : player3_pawn2_info,
                "player3_pawn3_info" : player3_pawn3_info,
                "player3_pawn4_info" : player3_pawn4_info
            }
            info.update(player3_dict)

        if num_players > 2:
            player4_dict = {
                #player4 info
                "player4_AI" : player4_AI,
                "player4_index" : player4_index,
                "player4_color": player4_color,
                "player4_location" : player4_location,
                "player4_pawn1_info" : player4_pawn1_info,
                "player4_pawn2_info" : player4_pawn2_info,
                "player4_pawn3_info" : player4_pawn3_info,
                "player4_pawn4_info" : player4_pawn4_info
            }
            info.update(player4_dict)


        pickle_out = open ("save.txt", "wb")
        pickle.dump(info, pickle_out)
        pickle_out.close()


        print ("Game Saved")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

#if(__name__ == "__main__"):
#    main = ""
#    app = Save(main)
