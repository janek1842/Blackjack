import sqlite3
import crypter

class DataBase:

        def createTables(self):
            con = sqlite3.connect("database.db")
            cur=con.cursor()
            try:
                cur.execute(''' CREATE TABLE if not exists players (
                        playerID integer primary key autoincrement,
                        username  text not null unique ,
                        password text,
                        isActive int default false,
                        isAdmin int default true,
                        avatar text default null
                ) ''')

                cur.execute(''' CREATE TABLE if not exists statistics (
                    playerID integer primary key,
    
                    column2 integer default 0,
                    column3 integer default 0,
                    column4 integer default 0,
                    column5 integer default 0,
                    column6 integer default 0,
                    column7 integer default 0,
                    column8 integer default 0,
                    column9 integer default 0,
                    column10 integer default 0,
                    column11 integer default 0,
                    column12 integer default 0,
                    column13 integer default 0,  
                    column14 integer default 0,
    
                    gameAmount integer default 0,
                    winsAmount integer default 0,
                    gamesTimeSec integer default 0,
    
                    FOREIGN KEY(playerID) REFERENCES players(playerID)
                ) ''')
            except sqlite3.OperationalError:
                pass
            con.commit()
            con.close()

        def checkIfPlayerExists(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT count(*) FROM players where username =?',(username,))
            playerCounter = cur.fetchone()[0]
            con.close()
            if(playerCounter > 0):
                return True
            else:
                return False

        def addPlayer(self,username,password,avatar):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            playerChecker = False
            if(self.checkIfPlayerExists(username)==False):
                cur.execute("INSERT INTO players values(null,'{}','{}',0,0,'{}') ".format(username,crypter.encrypt_message(password),avatar))
                cur.execute('SELECT playerID FROM players where username=?',(username,))
                playerID= cur.fetchone()[0]
                cur.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ".format(playerID))
                playerChecker = True

            else:
                print("Username: ",username," already exists")
                playerChecker = False
            con.commit()
            con.close()
            return playerChecker

        def validateLogin(self,username,password):

            result = False

            if(self.checkIfPlayerExists(username)==False):
                pass
            else:
                result = self.validatePassword(username,password)
            return result

        def validatePassword(self,username,password):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            result=False
            cur.execute('SELECT password FROM players where username =?', (username,))
            dbPassword = crypter.decrypt_message(cur)
            if(dbPassword==password):
                result=True
            con.close()
            return result

def testPlayers():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM players')
    print(cur.fetchall())
    con.commit()
    con.close()

def testStat():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM statistics')
    print(cur.fetchall())
    con.commit()
    con.close()

# TEST

# db = DataBase()
# db.createTables()
#
# print(db.addPlayer("Jankersek","password","avatar"))
#
# testPlayers()
# testStat()




