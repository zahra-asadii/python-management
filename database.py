import sqlite3

class Database :
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS  contacts 
        (id INTEGER PRIMARY KEY , fname TEXT , lname TEXT , cname TEXT , password TEXT ) ''')
        self.con.commit()


    def select_item (self):
        self.cur.execute('SELECT * FROM contacts')
        item = self.cur.fetchall()
        return item

    def insert_item (self,fname,lname,cname,password):
        self.cur.execute('INSERT INTO contacts VALUES (null,?,?,?,?) ' , (fname,lname,cname,password) )
        self.con.commit()

    def remove_item (self,id):
        self.cur.execute('DELETE FROM contacts WHERE id =? ' ,(id,))   
        self.con.commit()

    def search_item (self,password):
        self.cur.execute('SELECT * FROM contacts WHERE password = ?' , (password,))
        records = self.cur.fetchall()
        return records


# db=Database('d:/python/exam/mydata.db')
# db.con.close()