#code to save end game data to database
#import MySQLdb
import datetime

#saves player name, day/time, AI settings, result (Who won), how many turns
#button to query database and print out some stats
class Database:
    def write():
        print("Write")
        #get variables and store them as variables to insert
        db = MySQLdb.connect("webdb.uvm.edu", "pmacksey_admin", "wSuDSSnRb0Bk", "PMACKSEY_cs205sorry")
        #db.query("""SELECT """)
        cursor = db.cursor()

        player_name = "SALAMI"
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        AIleft = "SA"
        AIup = "LA"
        AIright = "MI"
        result = "salami"

        #can use array instead of listing stuff out
        cursor.execute("""INSERT INTO stats (fldPlayername, fldDate, fldAIleft, fldAIup, fldAIright, fldResult)
            VALUES (%s, %s, %s, %s, %s, %s)""", (player_name, date_time, AIleft, AIup, AIright, result))

        db.commit()
        db.close()
        print("Writing works")

    def read():
        print("Read")
        #query for info and print

        db = MySQLdb.connect("webdb.uvm.edu", "pmacksey_admin", "wSuDSSnRb0Bk", "PMACKSEY_cs205sorry")
        #db.query("""SELECT """)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM stats;")
        rows = cursor.fetchall()
        total = 0
        games_won = 0
        for row in rows:
                print ("GameID: ", row[0], " Player Name: ", row[1], " Date: ", row[2], " AI Settings: ", row[3], row[4], row[5], " Result: ", row[6])
                if row[0] > total:
                    total = row[0]
                if row[6] == 'won':
                    games_won += 1

        print("Total games played: ", total)
        print("Total games won: ", games_won)
        print("Win ratio: ", "{:.2%}".format(games_won/total))
        db.close()
        print("Reading works")

    #TEST
    #read()
    #write()
    #read()
