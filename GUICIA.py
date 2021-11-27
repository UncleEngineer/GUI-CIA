
# import sys
# print(sys.version)


# GUICIA.py
from tkinter import *
import tkinter.scrolledtext as st
import wikipedia
wikipedia.set_lang('th')

#COLOR
bg = '#1c1c1c' #background
fg = '#e6e6e6' #foreground


GUI = Tk()
GUI.geometry('500x400+500+50')
GUI.configure(background=bg)
GUI.state('zoomed')

WW = GUI.winfo_screenwidth()
WH = GUI.winfo_screenheight()

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
	try:
		text = wikipedia.summary(keyword)
		v_experience.set('')
		v_experience.set(text)
		experience.delete(1.0,END)
		experience.insert(INSERT, v_experience.get())
	except:
		v_experience.set('')
		v_experience.set('-----No result-----')
		experience.delete(1.0,END)
		experience.insert(INSERT, v_experience.get())


E1.bind('<Return>',Search)


##########LEFT ZONE###########
# main
FrameRect(50,100,900,40) #header bar
FixedText(440,105,'USER INFO',font=('Digital tech',15))


FrameRect(50,100,900,900) # from top left corner
# in-right
FrameRect(500,150,420,200)

photo = PhotoImage(file='./photo/user1.png')
userphoto = Label(GUI,image=photo,bd=0,relief='ridge',highlightthickness=0)
userphoto.place(x=60,y=150)

# in-bottom
v_experience = StringVar()
v_experience.set('----experience result----')

# text = wikipedia.summary('albert einstein')
# v_experience.set(text)

F1 = Frame(GUI,width=700)
F1.place(x=70,y=600)
# experience = Label(F1,textvariable=v_experience,fg=fg,bg=bg,font=f2)
# experience.pack()

experience = st.ScrolledText(F1,width=100,height=10,bg=bg,fg=fg,font=('Angsana New',18))
experience.pack()

experience.insert(INSERT, v_experience.get())


##########RIGHT ZONE###########
# main
FrameRect(1000,100,900,20,fill=True) #header bar
FrameRect(1000,100,900,800) # from top left corner


GUI.mainloop()