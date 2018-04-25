#code to save end game data to database
#import MySQLdb
import mysql.connector as MySQLdb
import datetime
from game import Game

#saves player name, day/time, AI settings, result (Who won), how many turns
#button to query database and print out some stats
class Database:
    def __init__(self, main):
        self.main = main

    def write(self):
        print("Write")
        #get variables and store them as variables to insert
        db = MySQLdb.connect(host = "webdb.uvm.edu", user = "pmacksey_admin", password = "wSuDSSnRb0Bk", database = "PMACKSEY_cs205sorry")
        #db.query("""SELECT """)
        cursor = db.cursor()
        if self.main.pc1difficulty == "":
            AIleft = ""
        else:
            AIleft = self.main.pc1difficulty
        if self.main.pc2difficulty == "":
            AIup = ""
        else:
            AIup = self.main.pc2difficulty
        if self.main.pc3difficulty == "":
            AIright = ""
        else:
            AIright = self.main.pc3difficulty


        player_name = self.main.playerName
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        turns_taken = self.main.turnsTaken
        spaces_moved = self.main.spacesMoved
        players_bumped = self.main.playersBumped
        bumped_by_others = self.main.bumpedByOthers
        cards_drawn = self.main.cardsDrawn
        #result = self.main.game.won
        result = "test"


        #can use array instead of listing stuff out
        cursor.execute("""INSERT INTO stats (fldPlayername, fldDate, fldAIleft, fldAIup, fldAIright, fldTurns_taken, fldspaces_moved, fldplayers_bumped, fldbumped_by_others, fldcards_drawn, fldResult)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (player_name, date_time, AIleft, AIup, AIright, turns_taken, spaces_moved, players_bumped, bumped_by_others, cards_drawn, result))

        db.commit()
        db.close()
        print("Writing works")

    def read(self):
        print("Read")
        #query for info and print

        db = MySQLdb.connect(host = "webdb.uvm.edu", user = "pmacksey_admin", password = "wSuDSSnRb0Bk", database = "PMACKSEY_cs205sorry")
        #db.query("""SELECT """)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM stats;")
        rows = cursor.fetchall()
        total = 0
        games_won = 0
        for row in rows:
                print ("GameID: ", row[0], " Player Name: ", row[1], " Date: ", row[2], " AI Settings: ", row[3], row[4], row[5],
                " Turns Taken: ", row[6], " Spaces moved: ", row[7], " Players bumped: ", row[8], " Bumped by others: ", row[9],
                " Cards drawn: ", row[10], " Result: ", row[11])
                if row[0] > total:
                    total = row[0]
                if row[11] == 'won':
                    games_won += 1

        print("Total games played: ", total)
        print("Total games won: ", games_won)
        print("Win ratio: ", "{:.2%}".format(games_won/total))
        print("Average turns per game: ", row[6]/total)
        print("Average spaces moved per game: ", row[7]/total)
        print("Average computer players bumped by human player per game: ", row[8]/total)
        print("Average times human player bumped by others per game: ", row[9]/total)
        print("Average cards drawn per game: ", row[10]/total)
        data = [total, games_won, "{:.2%}".format(games_won/total), "{:.2}".format(row[6]/total), row[7]/total, row[8]/total, row[9]/total, row[10]/total]
        db.close()
        print("Reading done")
        return data

    #TEST
    #read()
    #write()
    #read()
