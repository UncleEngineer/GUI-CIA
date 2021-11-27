# database.py
import sqlite3

conn = sqlite3.connect('user.sqlite3')
c = conn.cursor()

#create table
c.execute("""CREATE TABLE IF NOT EXISTS userinfo (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		code TEXT,
		first_name TEXT,
		last_name TEXT,
		tel TEXT,
		address TEXT,
		points INT,
		skill TEXT,
		experience TEXT,
		photo TEXT
	)""")



def insert_userinfo(datadict):
	ID=None
	code = datadict['code']
	first_name = datadict['first_name']
	last_name = datadict['last_name']
	tel = datadict['tel']
	address = datadict['address']
	points = datadict['points']
	skill = datadict['skill']
	experience = datadict['experience']
	photo = datadict['photo']
	with conn:
		command = 'INSERT INTO userinfo VALUES (?,?,?,?,?,?,?,?,?,?)'
		c.execute(command,(ID,code,first_name,last_name,tel,address,points,skill,experience,photo))
	conn.commit() #save
	print('success')


def view_userinfo():
	with conn:
		command = "SELECT * FROM userinfo"
		c.execute(command)
		result = c.fetchall()
	return result

def search_userinfo(field,data,fetchall=True):
	with conn:
		command = "SELECT * FROM userinfo WHERE code=(?)"
		command = 'SELECT * FROM userinfo WHERE {}=(?)'.format(field)
		c.execute(command,([data]))
		if fetchall:
			result = c.fetchall()
		else:
			result = c.fetchone()
	return result


def update_userinfo(ID,field,data):
	with conn:
		command = 'UPDATE userinfo SET {} = (?) WHERE ID=(?)'.format(field)
		c.execute(command,([data,ID]))
	conn.commit()
	print('success')


def delete_userinfo(ID):
	with conn:
		command = 'DELETE FROM userinfo WHERE ID=(?)'
		c.execute(command,([ID]))
	conn.commit()
	print('deleted')


data = {'code':'US-1002',
		'first_name':'Somchai',
		'last_name':'Engineer',
		'tel':'0801234567',
		'address':'99 Siam Bangkok',
		'points':0,
		'skill':'1. Python\n2. IoT\n3. 3D Model',
		'experience':'-Submarine\n-Jet Engine',
		'photo':'user1.png'}

# insert_userinfo(data)
# update_userinfo(1,'code','US-1001')
# delete_userinfo(2)
d = search_userinfo('last_name','Engineer')
print(d)

#viewdata = view_userinfo()
#print(viewdata)