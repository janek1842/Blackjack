import sqlite3
import crypter

class DataBase:

        def __init__(self):
            self.createTables()

        def createTables(self):
            con = sqlite3.connect("database.db")
            cur=con.cursor()
            try:
                cur.execute(''' CREATE TABLE if not exists players (
                        playerID integer primary key autoincrement,
                        username  text not null unique ,
                        password text,
                        money integer default 0,
                        isActive text default 'False',
                        isAdmin text default 'False',
                        avatar text default 'anubis.png',
                        description text
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
                    columnJ integer default 0,
                    columnQ integer default 0,
                    columnK integer default 0,  
                    columnA integer default 0,
    
                    gameAmount integer default 0,
                    winsAmount integer default 0,
                    gamesTimeSec integer default 0,
    
                    FOREIGN KEY(playerID) REFERENCES players(playerID)
                ) ''')

                con.execute("INSERT INTO players values(null,'player1','{}',1000,'False','False','anubis.png',null) on conflict do nothing".format(
                    crypter.encrypt_message("tajnehaslo")))
                con.execute("INSERT INTO players values(null,'player2','{}',2000,'False','False','anubis.png',null) on conflict do nothing ".format(
                    crypter.encrypt_message("tajnehaslo")))
                con.execute("INSERT INTO players values(null,'player3','{}',3000,'False','False','anubis.png',null) on conflict do nothing ".format(
                    crypter.encrypt_message("tajnehaslo")))
                con.execute("INSERT INTO players values(null,'player4','{}',4000,'False','False','anubis.png',null) on conflict do nothing ".format(
                    crypter.encrypt_message("tajnehaslo")))
                con.execute("INSERT INTO players values(null,'player5','{}',5000,'False','False','anubis.png',null) on conflict do nothing ".format(
                    crypter.encrypt_message("tajnehaslo")))
                con.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) on conflict do nothing ".format(1))
                con.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) on conflict do nothing ".format(2))
                con.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) on conflict do nothing".format(3))
                con.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) on conflict do nothing".format(4))
                con.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) on conflict do nothing".format(5))

            except sqlite3.OperationalError:
                print("cos nie tak ")
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
                cur.execute("INSERT INTO players values(null,'{}','{}',0,0,0,'anubis.png',null) ".format(username,crypter.encrypt_message(password)))
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
            print("oto1")
            dbPassword = crypter.decrypt_message(cur)

            if(dbPassword==password):
                result=True

            return result

        def getPlayer(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT username,money,isActive,isAdmin,avatar,description FROM players where username =?', (username,))
            player = cur.fetchall()
            player = {"username":player[0][0],"money":player[0][1],"isActive":player[0][2],"isAdmin":player[0][3],"avatar":player[0][4],"description":player[0][5]}
            return player

        def getPlayer2(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT username,avatar,isAdmin FROM players where username =?', (username,))
            player = cur.fetchone()
            return player

        def getPlayers(self):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT username,money,isActive,isAdmin,avatar,description FROM players ')
            player = cur.fetchall()
            player = {"username": player[0][0], "money": player[0][1], "isActive": player[0][2],
                      "isAdmin": player[0][3], "avatar": player[0][4], "description": player[0][5]}
            return player

        def getPlayers2(self):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT username,isActive,isAdmin FROM players ')
            player = cur.fetchall()
            print(player)
            return player

        def makeBanned(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('UPDATE players SET isActive="False" where username =?',(username,))
            con.commit()

        def makeUnBanned(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('UPDATE players SET isActive="True" where username =?',(username,))
            con.commit()

        def makeAdmin(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('UPDATE players SET isAdmin="True" where username =?',(username,))
            con.commit()

        def makeUser(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('UPDATE players SET isAdmin="False" where username =?',(username,))
            con.commit()

        def getCardStatistics(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM statistics where playerID = (SELECT playerID FROM players WHERE username =?)',(username,))
            statSet = cur.fetchall()
            statistics = {"2":statSet[0][1],"3":statSet[0][2],"4":statSet[0][3],"5":statSet[0][4],"6":statSet[0][5]
                          ,"7":statSet[0][6],"8":statSet[0][7],"9":statSet[0][8],"10":statSet[0][9],"J":statSet[0][10],
                          "Q":statSet[0][11],"K":statSet[0][12],"A":statSet[0][13]}
            return statistics

        def getPlayerStatistics(self,username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM statistics where playerID = (SELECT playerID FROM players WHERE username =?)', (username,))
            playerStatSet = cur.fetchall()

            winRatio = self.getProperStatToAvoidZeroDivision(playerStatSet[0][15],playerStatSet[0][14])
            averageTime = self.getProperStatToAvoidZeroDivision(playerStatSet[0][16], playerStatSet[0][14])
            mostPickedCard = max(self.getCardStatistics(username), key=self.getCardStatistics(username).get)
            cardsGotten = sum((self.getCardStatistics(username).values()))

            playerStatistics = {"HandsPlayed":playerStatSet[0][14],"WonHands":playerStatSet[0][15],"WinRatio":winRatio,
                                "AverageTimeToMove":averageTime,"MostPickedCard":mostPickedCard,"CardsGotten":cardsGotten}
            return playerStatistics

        def getProperStatToAvoidZeroDivision(self,nominator,denominator):
            if(denominator==0):
                return 0
            else:
                return (int(nominator)/int(denominator))

        def getRank(self):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT username,money,IIF(gameAmount=0,0,winsAmount/gameAmount) FROM players,statistics where statistics.playerID=players.playerID ORDER BY money DESC')
            rankStat = cur.fetchall()
            return rankStat

        def updateAvatar(self,username,avatar):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT playerID FROM players where username =?', (username,))
            playerID = cur.fetchone()[0]
            cur.execute('UPDATE players SET avatar=? WHERE playerID = ?', (avatar,playerID) )
            con.commit()

        def updateDescription(self,username,description):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT playerID FROM players where username =?', (username,))
            playerID = cur.fetchone()[0]
            cur.execute('UPDATE players SET description=? WHERE playerID = ?', (description,playerID))
            con.commit()

        def updatePassword(self,username,password):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT playerID FROM players where username =?', (username,))
            playerID = cur.fetchone()[0]
            cur.execute('UPDATE players SET password=? WHERE playerID = ?', (crypter.encrypt_message(password),playerID))
            con.commit()

        def getPasswd(self, username):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT password FROM players WHERE username=?', (username,))
            return crypter.decrypt_message(cur)

        def updateCardStats(self,username,cards):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT playerID FROM players where username =?', (username,))
            playerID = cur.fetchone()[0]

            for key,value in cards.items():
                currentCard = "column"+key
                cur.execute('SELECT '+currentCard+'  FROM statistics where playerID =?', (playerID,))
                currentCardValue = cur.fetchone()[0]
                currentCardValue = currentCardValue + value
                cur.execute('UPDATE statistics SET '+currentCard+'=? WHERE playerID = ?',(currentCardValue,playerID))
                con.commit()
            con.close()

        def updatePlayerStat(self,username,isWinner,gameTimeSec,winMoney):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT playerID FROM players where username =?', (username,))
            playerID = cur.fetchone()[0]

            cur.execute('UPDATE players SET money = money + ?  WHERE playerID = ?', (winMoney,playerID,))
            cur.execute('UPDATE statistics SET gameAmount = gameAmount + 1  WHERE playerID = ?', (playerID,))
            cur.execute('UPDATE statistics SET gamesTimeSec = gamesTimeSec + ?  WHERE playerID = ?', (gameTimeSec,playerID))

            if(isWinner):
                cur.execute('UPDATE statistics SET winsAmount = winsAmount + 1  WHERE playerID = ?', (playerID,))

            con.commit()
            con.close()

        def checkIfAdminPresent(self,username1=None,username2=None,username3=None,username4=None,username5=None):
            listOfUsers = [username1,username2,username3,username4,username5]

            for u in listOfUsers:
                if u is not None:
                    con = sqlite3.connect('database.db')
                    cur = con.cursor()
                    cur.execute('SELECT isAdmin FROM players where username =?', (u,))
                    try:
                        if(cur.fetchone()[0]=="True"):
                            return True
                    except:
                        print("Sth wrong in checkIfAdminPresent")
            return False

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



