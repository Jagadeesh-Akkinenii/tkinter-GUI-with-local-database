import sqlite3

def connect():
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS HG_details (Hid INTEGER PRIMARY KEY , HName TEXT, HLlink TEXT, HRating INTEGER);")
	conn.commit()
	conn.close()

def search(HName = "", HLink = "", HRating = ""):
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM HG_details WHERE HName=? OR HLlink=? OR HRating=?;",(HName, HLink, HRating))
	rows = cur.fetchall()
	conn.close()
	return rows

def insert(HName = "", HLink = "", HRating = ""):
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO HG_details VALUES (NULL,? ,? ,?);",(HName, HLink, HRating))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM HG_details")
	rows = cur.fetchall()
	conn.close()
	return rows	

def delete(Hid):
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM HG_details WHERE Hid=?",(Hid,))
	conn.commit()
	conn.close()

def update(Hid = "", HName = "", HLink = "", HRating = ""):
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	cur.execute("UPDATE HG_details SET HName=?, HLlink=?, HRating=? WHERE Hid=?;",(HName, HLink, HRating, Hid))
	conn.commit()
	conn.close()
connect()
