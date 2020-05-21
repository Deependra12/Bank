import sqlite3
class sqlitehelp():
    def __init__(self,name=None):
        self.conn=None
        self.cursor=None

        if name:
            self.open(name)
    def open(self,name):
        try:
            self.conn=sqlite3.connect(name)
            self.cursor=self.conn.cursor()
            print(sqlite3.version)
        except:
            print('connection failed')
    def createtable(self):
        c=self.cursor
        c.execute("""CREATE TABLE bankusers1(
                        
                        Name TEXT NOT NULL,
                        Accountno INTEGER PRIMARY KEY ,
                        Accounttype TEXT NOT NULL,
                        Amount INTEGER
                        
                                    )""")
    def insert(self,query,add):
        c=self.cursor
        c.execute(query,add)
        self.conn.commit()
    def select(self,query):
        c=self.cursor
        c.execute(query)
        return c.fetchall()
    def update(self,query):
        c=self.cursor
        c.execute(query)
        self.conn.commit()
    
#test1=sqlitehelp("test111.db")
#test1.createtable()
#test.edit(" INSERT INTO users(name,year,admin)VALUES('deependrjffja',1998,0t
#test1.insert(" INSERT INTO users(name,year,admin)VALUES('ramesh',1998,0)")
#test.edit("UPDATE users SET name='harikishna' WHERE name='ramesh'" )
    
#print(test1.select("SELECT * FROM users ")[1][1])


           
