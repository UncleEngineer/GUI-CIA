

# GUICIA.py
from tkinter import *
import tkinter.scrolledtext as st
import wikipedia
from PIL import Image, ImageTk
from tkinter import filedialog
wikipedia.set_lang('th')

###################DATABASE###################
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

######################################


#COLOR
bg = '#1c1c1c' #background
fg = '#e6e6e6' #foreground


GUI = Tk()
GUI.geometry('500x400+500+50')
GUI.configure(background=bg)
GUI.state('zoomed')
GUI.title('Unclelabs User Database')
WW = GUI.winfo_screenwidth()
WH = GUI.winfo_screenheight()

GUI.attributes('-fullscreen',False)
GUI.bind('<F11>', lambda event: GUI.attributes('-fullscreen', not GUI.attributes('-fullscreen')))
# 16:9 , 4:3

canvas = Canvas(GUI,width=WW,height=WH,background=bg)
canvas.configure(bd=0,relief='ridge',highlightthickness=0)
canvas.place(x=0,y=0)

def FrameRect(x,y,width=200,height=200,fill=False):
	if fill:
		frame1 = canvas.create_rectangle(0,0,width,height,outline=fg,width=2,fill=fg)
	else:
		frame1 = canvas.create_rectangle(0,0,width,height,outline=fg,width=2)
	canvas.move(frame1,x,y) # move to 200,200 ,(200,200)


##########FONT###########

f1 = ('Digital tech',30)
f2 = (None,15)
##########TOP ZONE###########

L1 = Label(GUI,text='UNCLELABS USER DATABASE',bg=bg,fg=fg,font=f1)
L1.place(x=50,y=30)

def FixedText(x,y,text='fixed text',font=f2,color=fg):
	L1 = Label(GUI,text=text,bg=bg,fg=color,font=font)
	L1.place(x=x,y=y)


# Entry
v_search = StringVar()
E1 = Entry(GUI,textvariable=v_search,font=('Angsana New',20),width=70 ,bg=bg, fg=fg)
E1.configure(insertbackground=fg)
E1.configure(highlightthickness=2, highlightbackground=fg, highlightcolor=fg)
E1.place(x=600,y=40)

def Search(event):
	keyword = v_search.get()
	result = search_userinfo('code',keyword)[0] #เลือกผลลัพท์แรก

	if len(result) != 0:
		r = result[:7]
		v_name.set('{} {}'.format(r[2].upper(),r[3].upper()))
		userinfotext = 'CODE: {}\nTEL: {}\nADDRESS: {}'.format(r[1],r[4],r[5])
		v_userinfo.set(userinfotext)
		# (1, 'US-1001', 'Somsak', 'Engineer', '0801234567', '99 Siam Bangkok', 0,....)

		v_skill.set('')
		v_skill.set(result[7])
		skill.delete(1.0,END)
		skill.insert(INSERT, v_skill.get())

		v_experience.set('')
		v_experience.set(result[8])
		experience.delete(1.0,END)
		experience.insert(INSERT, v_experience.get())


		#set image
		try:
			photofile = Image.open(result[-1])
		except:
			photofile = Image.open( './photo/'+ result[-1])

		img_w , img_h = photofile.size
		ratio = img_h / img_w
		resize_w = 300
		new_h = int(ratio * resize_w)

		photofile = photofile.resize((resize_w,new_h))
		photo = ImageTk.PhotoImage(photofile)
		userphoto.configure(image=photo)
		userphoto.image = photo

	else:
		v_name.set('-----No result-----')
		v_userinfo.set('-----No result-----')
		v_skill.set('')
		v_skill.set('-----No result-----')
		skill.delete(1.0,END)
		skill.insert(INSERT, v_skill.get())

		v_experience.set('')
		v_experience.set('-----No result-----')
		experience.delete(1.0,END)
		experience.insert(INSERT, v_experience.get())


	# try:
	# 	text = wikipedia.summary(keyword)
	# 	v_experience.set('')
	# 	v_experience.set(text)
	# 	experience.delete(1.0,END)
	# 	experience.insert(INSERT, v_experience.get())
	# except:
	# 	v_experience.set('')
	# 	v_experience.set('-----No result-----')
	# 	experience.delete(1.0,END)
	# 	experience.insert(INSERT, v_experience.get())


E1.bind('<Return>',Search)


##########LEFT ZONE###########
# main
FrameRect(50,100,900,40) #header bar
FixedText(440,105,'USER INFO',font=('Digital tech',15))


FrameRect(50,100,900,900) # from top left corner
# in-right
FrameRect(400,190,520,200)


v_name = StringVar()
usertext = 'Uncle Engineer'
v_name.set(usertext.upper())
nameinfo = Label(GUI,textvariable=v_name,fg=fg,bg=bg,font=('impact',25),justify=LEFT)
nameinfo.place(x=420,y=200)

v_userinfo = StringVar()
#usertext = 'Name: Uncle Engineer\nEmail: loong.wissawakorn@gmail.com\nTel: 0801234567\nAddress: 99 Siam, Bangkok'
usertext = '---No result---'
v_userinfo.set(usertext)
userinfo = Label(GUI,textvariable=v_userinfo,fg=fg,bg=bg,font=('Courier',15,'bold'),justify=LEFT)
userinfo.place(x=420,y=250)

#photo = PhotoImage(file='./photo/user1.png').subsample(3)
photofile = Image.open('./photo/user1.png')
print('SIZE:', photofile.size)

# control h
# ratio = 500 / 250
# ratio = 2
# new_h = 500
# new_w = 2 * 500

# control w
# ratio = 250 / 500
# ratio = 0.5
# new_w = 250
# new_h = 0.5 * 250

img_w , img_h = photofile.size
ratio = img_h / img_w
resize_w = 300
new_h = int(ratio * resize_w)

photofile = photofile.resize((resize_w,new_h))
photo = ImageTk.PhotoImage(photofile)

userphoto = Label(GUI,image=photo,bd=0,relief='ridge',highlightthickness=0)
userphoto.place(x=60,y=150)



# text = wikipedia.summary('albert einstein')
# v_experience.set(text)

F1 = Frame(GUI,bg=bg)
F1.place(x=400,y=400)
# experience = Label(F1,textvariable=v_experience,fg=fg,bg=bg,font=f2)
# experience.pack()

# experience = st.ScrolledText(F1,width=100,height=10,bg=bg,fg=fg,font=('Angsana New',18))
# experience.pack()

# in-bottom
v_skill = StringVar()
v_skill.set('----skill result----')
skill = Text(F1,width=65,height=8,bg=bg,fg=fg,font=('Angsana New',18))
skill.grid(row=0,column=0)
skill.insert(INSERT, v_skill.get())


v_experience = StringVar()
v_experience.set('----experience result----')
experience = Text(F1,width=65,height=8,bg=bg,fg=fg,font=('Angsana New',18))
experience.grid(row=1,column=0,pady=10)
experience.insert(INSERT, v_experience.get())


##########RIGHT ZONE###########
# main
FrameRect(1000,100,900,40) #header bar
FrameRect(1000,100,900,900) # from top left corner

# RIGHT ZONE

def TextField(value,frame,label):
	L = Label(frame,text=label,font=f2,bg=bg,fg=fg,justify=LEFT).pack(pady=10,anchor='w')
	E1 = Entry(frame,textvariable=value,font=('Angsana New',20),width=50 ,bg=bg, fg=fg)
	E1.configure(insertbackground=fg)
	E1.configure(highlightthickness=2, highlightbackground=fg, highlightcolor=fg)
	E1.pack()

v_code = StringVar()
v_first_name = StringVar()
v_last_name = StringVar()
v_tel = StringVar()
v_address = StringVar()
v_points = StringVar()
v_skill2 = StringVar() # text
v_experience2 = StringVar() # text
v_photo = StringVar() # select file

F2 = Frame(GUI,bg=bg)
F2.place(x=1050,y=150)

TextField(v_code,F2,'code')
TextField(v_first_name,F2,'First name')
TextField(v_last_name,F2,'Last name')
TextField(v_tel,F2,'Tel')
TextField(v_address,F2,'Address')
TextField(v_points,F2,'Points')
TextField(v_skill2,F2,'Skill')
TextField(v_experience2,F2,'Experience')

v_filename = StringVar()
def BrowsePhoto():
	filename = filedialog.askopenfilename()
	v_filename.set(filename)
	print(filename)

B = Button(GUI,text='Browse Photo',bg=bg,fg=fg, command=BrowsePhoto)
B.place(x=1050,y=920)

def SaveData():
	data = {'code':v_code.get(),
		'first_name':v_first_name.get(),
		'last_name':v_last_name.get(),
		'tel':v_tel.get(),
		'address':v_address.get(),
		'points':v_points.get(),
		'skill':v_skill2.get(),
		'experience':v_experience2.get(),
		'photo':v_filename.get()}

	insert_userinfo(data)
	v_code.set('')
	v_first_name.set('')
	v_last_name.set('')
	v_tel.set('')
	v_address.set('')
	v_points.set('')
	v_skill.set('')
	v_experience.set('')
	v_filename.set('')


BSave = Button(GUI,text='Save Data',bg=bg,fg=fg, command=SaveData ,width=30,height=5)
BSave.place(x=1250,y=900)

GUI.mainloop()