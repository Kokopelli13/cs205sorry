#code to load file in and resume game by making all needed variables equal to what they are in file
import pickle

pickle_in = open("save.txt", "rb")
info = pickle.load(pickle_in)

#print(info)
#player 1 data
# player1_color = info["player1_color"]
# player1_location = info["player1_location"]
# player1_setting = info["player1_setting"]
# player1_pawn1_location = info["player1_pawn1_location"]
# player1_pawn2_location = info["player1_pawn2_location"]
# player1_pawn3_location = info["player1_pawn3_location"]
# player1_pawn4_location = info["player1_pawn4_location"]
#
#
# player1_info = info["player1_info"]
# player1_pawn1_info = info["player1_pawn1_info"]
# player1_pawn2_info = info["player1_pawn2_info"]
# player1_pawn3_info = info["player1_pawn3_info"]
# player1_pawn4_info = info["player1_pawn4_info"]

# #player 2 data
# player2_color = info["player2_color"]
# player2_location = info["player2_location"]
# player2_setting = info["player2_setting"]
# player2_pawn1_location = info["player2_pawn1_location"]
# player2_pawn2_location = info["player2_pawn2_location"]
# player2_pawn3_location = info["player2_pawn3_location"]
# player2_pawn4_location = info["player2_pawn4_location"]
#
# #player 3 data
# player3_color = info["player3_color"]
# player3_location = info["player3_location"]
# player3_setting = info["player3_setting"]
# player3_pawn1_location = info["player3_pawn1_location"]
# player3_pawn2_location = info["player3_pawn2_location"]
# player3_pawn3_location = info["player3_pawn3_location"]
# player3_pawn4_location = info["player3_pawn4_location"]
#
# #player 4 data
# player4_color = info["player4_color"]
# player4_location = info["player4_location"]
# player4_setting = info["player4_setting"]
# player4_pawn1_location = info["player4_pawn1_location"]
# player4_pawn2_location = info["player4_pawn2_location"]
# player4_pawn3_location = info["player4_pawn3_location"]
# player4_pawn4_location = info["player4_pawn4_location"]

#deck data
deck_order = info["deck_order"]
card_index = info["card_index"]
current_card = info["current_card"]

# #player 1
# print("Player 1 color: ", player1_color)
# print("Player 1 location: ", player1_location)
# print("Player 1 setting: ", player1_setting)
# print("Player 1 Pawn 1 location: ", player1_pawn1_location)
# print("Player 1 Pawn 2 location: ", player1_pawn2_location)
# print("Player 1 Pawn 3 location: ", player1_pawn3_location)
# print("Player 1 Pawn 4 location: ", player1_pawn4_location)
# print("")

# print("Player 1 info: ", player1_info)
# print("Player 1 pawn 1 info: ", player1_pawn1_info)
# print("Player 1 pawn 2 info: ", player1_pawn2_info)
# print("Player 1 pawn 3 info: ", player1_pawn3_info)
# print("Player 1 pawn 4 info: ", player1_pawn4_info)

# #player 2
# print("Player 2 color: ", player2_color)
# print("Player 2 location: ", player2_location)
# print("Player 2 setting: ", player2_setting)
# print("Player 2 Pawn 1 location: ", player2_pawn1_location)
# print("Player 2 Pawn 2 location: ", player2_pawn2_location)
# print("Player 2 Pawn 3 location: ", player2_pawn3_location)
# print("Player 2 Pawn 4 location: ", player2_pawn4_location)
# print("")
#
# #player 3
# print("Player 3 color: ", player3_color)
# print("Player 3 location: ", player3_location)
# print("Player 3 setting: ", player3_setting)
# print("Player 3 Pawn 1 location: ", player3_pawn1_location)
# print("Player 3 Pawn 2 location: ", player3_pawn2_location)
# print("Player 3 Pawn 3 location: ", player3_pawn3_location)
# print("Player 3 Pawn 4 location: ", player3_pawn4_location)
# print("")
#
# #player 4
# print("Player 4 color: ", player4_color)
# print("Player 4 location: ", player4_location)
# print("Player 4 setting: ", player4_setting)
# print("Player 4 Pawn 1 location: ", player4_pawn1_location)
# print("Player 4 Pawn 2 location: ", player4_pawn2_location)
# print("Player 4 Pawn 3 location: ", player4_pawn3_location)
# print("Player 4 Pawn 4 location: ", player4_pawn4_location)
# print("")

#deck
print("Deck order: ", deck_order)
print("Current card: ", current_card)
print("Card Index: ", card_index)
