import binascii
import hashlib
import os
import sqlite3
import crypter
from cryptography.fernet import Fernet
import base64

conn = sqlite3.connect('database.db')

c = conn.cursor()
c.execute('PRAGMA foreign_keys = ON')

c.execute(''' CREATE TABLE if not exists players (
        playerID integer primary key autoincrement,
        username  text not null unique ,
        password text,
        money integer default 0,
        isActive integer default 0,
        isAdmin integer,
        avatar text
) ''')

c.execute(''' CREATE TABLE if not exists statistics (
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


c.execute("INSERT INTO players values(null,'player1','{}',1000,1,0,'images/default.png') ".format(crypter.encrypt_message("tajnehaslo")))
c.execute("INSERT INTO players values(null,'player2','{}',2000,1,0,'images/default.png') ".format(crypter.encrypt_message("tajnehaslo")))
c.execute("INSERT INTO players values(null,'player3','{}',3000,1,0,'images/default.png') ".format(crypter.encrypt_message("tajnehaslo")))
c.execute("INSERT INTO players values(null,'player4','{}',4000,1,0,'images/default.png') ".format(crypter.encrypt_message("tajnehaslo")))
c.execute("INSERT INTO players values(null,'player5','{}',5000,1,0,'images/default.png') ".format(crypter.encrypt_message("tajnehaslo")))
c.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ".format(1))
c.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ".format(2))
c.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ".format(3))
c.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ".format(4))
c.execute("INSERT INTO statistics values('{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ".format(5))
#c.execute("INSERT INTO cards values(null,1,null,null,null,null,null,null,null,null,null,null,null,null,null)")

#c.execute("SELECT cardID, max(amount) FROM players p ,cards c where p.username='Ciota' and p.playerID=c.playerID ")

c.fetchall()
conn.commit()
conn.close()

