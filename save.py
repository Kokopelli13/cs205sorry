#code to write save sata to file and load it back
import pickle
from deck import Deck
#things to save:
#player: name, position, color, pawn locations, AI setting if computer
#deck: current card, deck order
#game: current player,
#current player up

#player 1
player1_color = "blue"
player1_location = "down"
player1_setting = "none"
player1_pawn1_location = "1"
player1_pawn2_location = "2"
player1_pawn3_location = "3"
player1_pawn4_location = "4"

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
deck=Deck()
deck_order = deck.deck
current_card = "1"

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
    "current_card" : current_card
    }

pickle_out = open ("save.txt", "wb")
pickle.dump(info, pickle_out)
pickle_out.close()


print ("Game Saved")
