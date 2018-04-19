#code to load file in and resume game by making all needed variables equal to what they are in file
import pickle


class Load:


    def __init__(self, main):
        self.main = main
        self.playerList = self.main.game.playerList

    def load(self):
        pickle_in = open("save.txt", "rb")
        info = pickle.load(pickle_in)

        #game info
        current_player = info["current_player"]
        num_players = info["num_players"]
        print("Current player: ", current_player)
        print("Number of computer players: ", num_players)


        #player 1 data
        player1_index = info["player1_index"]
        player1_color = info["player1_color"]
        player1_location = info["player1_location"]
        player1_pawn1_info = info["player1_pawn1_info"]
        player1_pawn2_info = info["player1_pawn2_info"]
        player1_pawn3_info = info["player1_pawn3_info"]
        player1_pawn4_info = info["player1_pawn4_info"]

        #player 1
        print("Player 1 index: ", player1_index)
        print("Player 1 color: ", player1_color)
        print("Player 1 location: ", player1_location)
        print("Player 1 pawn 1 info: ", player1_pawn1_info)
        print("Player 1 pawn 2 info: ", player1_pawn2_info)
        print("Player 1 pawn 3 info: ", player1_pawn3_info)
        print("Player 1 pawn 4 info: ", player1_pawn4_info)
        print("")

        # #player 2 data
        player2_AI = info["player2_AI"]
        player2_index = info["player2_index"]
        player2_color = info["player2_color"]
        player2_location = info["player2_location"]
        player2_pawn1_info = info["player2_pawn1_info"]
        player2_pawn2_info = info["player2_pawn2_info"]
        player2_pawn3_info = info["player2_pawn3_info"]
        player2_pawn4_info = info["player2_pawn4_info"]


        #player 2 print data
        print("Player 2 AI: ", player2_AI)
        print("Player 2 index: ", player2_index)
        print("Player 2 color: ", player2_color)
        print("Player 2 location: ", player2_location)
        print("Player 2 pawn 1 info: ", player2_pawn1_info)
        print("Player 2 pawn 2 info: ", player2_pawn2_info)
        print("Player 2 pawn 3 info: ", player2_pawn3_info)
        print("Player 2 pawn 4 info: ", player2_pawn4_info)
        print("")

        if num_players > 1:
            # #player 3 data
            player3_AI = info["player3_AI"]
            player3_index = info["player3_index"]
            player3_color = info["player3_color"]
            player3_location = info["player3_location"]
            player3_pawn1_info = info["player3_pawn1_info"]
            player3_pawn2_info = info["player3_pawn2_info"]
            player3_pawn3_info = info["player3_pawn3_info"]
            player3_pawn4_info = info["player3_pawn4_info"]

            #player 3 print data
            print("Player 3 AI: ", player3_AI)
            print("Player 3 index: ", player3_index)
            print("Player 3 color: ", player3_color)
            print("Player 3 location: ", player3_location)
            print("Player 3 pawn 1 info: ", player3_pawn1_info)
            print("Player 3 pawn 2 info: ", player3_pawn2_info)
            print("Player 3 pawn 3 info: ", player3_pawn3_info)
            print("Player 3 pawn 4 info: ", player3_pawn4_info)
            print("")
        #
        if num_players > 2:
            # #player 4 data
            player4_AI = info["player4_AI"]
            player4_index = info["player4_index"]
            player4_color = info["player4_color"]
            player4_location = info["player4_location"]
            player4_pawn1_info = info["player4_pawn1_info"]
            player4_pawn2_info = info["player4_pawn2_info"]
            player4_pawn3_info = info["player4_pawn3_info"]
            player4_pawn4_info = info["player4_pawn4_info"]

            #player 4 print data
            print("Player 4 AI: ", player4_AI)
            print("Player 4 index: ", player4_index)
            print("Player 4 color: ", player4_color)
            print("Player 4 location: ", player4_location)
            print("Player 4 pawn 1 info: ", player4_pawn1_info)
            print("Player 4 pawn 2 info: ", player4_pawn2_info)
            print("Player 4 pawn 3 info: ", player4_pawn3_info)
            print("Player 4 pawn 4 info: ", player4_pawn4_info)
            print("")

        #deck data
        deck_order = info["deck_order"]
        card_index = info["card_index"]
        current_card = info["current_card"]

        #deck
        print("Deck order: ", deck_order)
        print("Current card: ", current_card)
        print("Card Index: ", card_index)


        #SETTING VALUES

        #game info
        self.main.game.turn = current_player
        self.main.numPlayers = num_players

        #deck information
        self.main.deck.deck = deck_order
        self.main.deck.current_card = current_card
        self.main.deck.i = card_index


        #player 1 info
        self.playerList[0].playerIndex = player1_index
        self.playerList[0].color = player1player1_color
        self.playerList[0].playerPosition = player1_location
        # #player1 pawn info.
        self.playerList[0].pawnList[0].position = player1_pawn1_info
        self.playerList[0].pawnList[1].position = player1_pawn2_info
        self.playerList[0].pawnList[2].position = player1_pawn3_info
        self.playerList[0].pawnList[3].position = player1_pawn4_info



        #player 2 information
        self.main.pc1difficulty = player2_AI
        self.playerList[1].playerIndex = player2_index
        self.playerList[1].color = player1player2_color
        self.playerList[1].playerPosition = player2_location
        # #player1 pawn info.
        self.playerList[1].pawnList[0].position = player2_pawn1_info
        self.playerList[1].pawnList[1].position = player2_pawn2_info
        self.playerList[1].pawnList[2].position = player2_pawn3_info
        self.playerList[1].pawnList[3].position = player2_pawn4_info

        #player 3 information
        self.main.pc2difficulty = player3_AI
        self.playerList[2].playerIndex = player3_index
        self.playerList[2].color = player1player3_color
        self.playerList[2].playerPosition = player3_location
        # #player1 pawn info.
        self.playerList[2].pawnList[0].position = player3_pawn1_info
        self.playerList[2].pawnList[1].position = player3_pawn2_info
        self.playerList[2].pawnList[2].position = player3_pawn3_info
        self.playerList[2].pawnList[3].position = player3_pawn4_info

        if num_players > 1:
            #player 3 information
            self.main.pc2difficulty = player3_AI
            self.playerList[2].playerIndex = player3_index
            self.playerList[2].color = player1player3_color
            self.playerList[2].playerPosition = player3_location
            # #player1 pawn info.
            self.playerList[2].pawnList[0].position = player3_pawn1_info
            self.playerList[2].pawnList[1].position = player3_pawn2_info
            self.playerList[2].pawnList[2].position = player3_pawn3_info
            self.playerList[2].pawnList[3].position = player3_pawn4_info


        if num_players > 2:
            #player 4 information
            self.main.pc3difficulty = player4_AI
            self.playerList[3].playerIndex = player4_index
            self.playerList[3].color = player1player4_color
            self.playerList[3].playerPosition = player4_location
            # #player1 pawn info.
            self.playerList[3].pawnList[0].position = player4_pawn1_info
            self.playerList[3].pawnList[1].position = player4_pawn2_info
            self.playerList[3].pawnList[2].position = player4_pawn3_info
            self.playerList[3].pawnList[3].position = player4_pawn4_info
