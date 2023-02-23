from tkinter import *
from tkinter import messagebox

def mainwindow() :
   root = Tk()
   root.title("Homework Week2 : Design layout using Frame")
   root.geometry("700x400")
   root.configure(bg='lightgreen')
   root.option_add('*font','Helvetica 16')
   root.rowconfigure(0,weight=1)
   root.rowconfigure(1,weight=4)
   root.rowconfigure(2,weight=2)
   root.columnconfigure(0,weight=2)
   root.columnconfigure(1,weight=2)
   root.columnconfigure(1,weight=1)
   return(root)

def layout(root) :
    top = Frame(root,bg="#86C8BC")
    top.grid(row=0,columnspan=2,sticky="news")
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)

    left = Frame(root,bg="#BFEAF5",width=200,height=80)
    left.grid(row=1,column=0,ipadx=10,sticky="news")
    left.rowconfigure((0,1),weight=1)
    left.columnconfigure((0,1),weight=1)

    mleft = Frame(root,bg="#FFFFFF",width=190,height=130)
    mleft.grid(row=1,column=0,ipadx=10,padx=15,pady=15,sticky="news")
    mleft.rowconfigure(0,weight=1)
    mleft.rowconfigure((1,2),weight=1)
    mleft.columnconfigure((0,1,2,3),weight=1)

    right = Frame(root,bg="#FFF6BD",width=200,height=10)
    right.grid(row=1,column=1,sticky="news")
    right.rowconfigure(0,weight=2)
    right.columnconfigure(0,weight=1)

    skright = Frame(root,bg="#FFFFFF",width=190,height=10)
    skright.grid(row=1,column=1,ipadx=10,padx=15,pady=15,sticky="news")
    skright.rowconfigure((0,1),weight=0)
    skright.columnconfigure(0,weight=1)

    bottom = Frame(root,bg="#FFD4B2")
    bottom.grid(row=2,column=0,columnspan=2,sticky="news")
    bottom.rowconfigure(0,weight=2)
    bottom.columnconfigure((0,1,2,3),weight=4)
    return(top,left,right,bottom,mleft,skright)

def topwidget(top) :
    title = Label(top,text="Dashbroad by Tipparida Rujisunkuntorn",bg="#86C8BC",fg="#00425A")
    title.grid(row=0,columnspan=2)

def leftwidget(left) :
    pic = Label(mleft,image=female,bg="#FFFFFF")
    pic.grid(row=1,column=0,sticky=N)
    txt1 = Label(mleft,text="Miss Tipparida Rujisunkuntorn",font='Helvetica 16',bg="#FFFFFF",fg="#AA8B56")
    txt1.place(x= 150,y= 40) #ถ้า txt ยาวให้ใช้พวกนี้ จะกำหนดค่าแนวตั้งแนวนอนของข้อความโดยไม่ต้องใช้ .grid
    txt2 = Label(mleft,text="Undergraduate",font='Helvetica 10',bg="#FFFFFF",fg="#AA8B54")
    txt2.place(x= 150,y= 73)
    txt3 = Label(mleft,text="Information Technology and Innovation",font='Helvetica 10',bg="#FFFFFF",fg="#AA8B54")
    txt3.place(x= 150,y= 105)

    green = Frame(mleft,bg='#379237')
    green.grid(row= 2,column= 0,sticky='new',ipadx= 10)
    green.rowconfigure((0),weight= 1)
    green.columnconfigure((0),weight= 1)
    age = Label(green,text= "19\nAge",fg="#FFFFFF",bg="#379237",font='Helvetica 15 bold')
    age.grid(row= 2,column= 0,sticky='news',ipadx= 10)

    yellow = Frame(mleft,bg='#F5C344')
    yellow.grid(row= 2,column= 1,sticky='new',ipadx= 10)
    yellow.rowconfigure((0),weight= 1)
    yellow.columnconfigure((0),weight= 1)
    weight = Label(yellow,text= "74\nWeight",fg="#FFFFFF",bg="#F5C344",font='Helvetica 15 bold')
    weight.grid(row= 2,columnspan= 1,sticky='news',ipadx= 5,)

    blue = Frame(mleft,bg='#4BA0B5')
    blue.grid(row= 2,column= 2,sticky='new',ipadx = 10)
    blue.rowconfigure((0),weight= 1) 
    blue.columnconfigure((0),weight= 1)
    height = Label(blue,text= "167\nHeight",fg="#FFFFFF",bg="#4BA0B5",font='Helvetica 15 bold')
    height.grid(row= 2,columnspan= 1,sticky='news',ipadx= 10)

    red = Frame(mleft,bg='#CB444A')
    red.grid(row= 2,column= 3,sticky='new',ipadx = 10)
    red.rowconfigure((0),weight= 1) 
    red.columnconfigure((0),weight= 1)
    skill = Label(red,text = "5\nSkill",fg="#FFFFFF",bg='#CB444A',font='Helvetica 15 bold')
    skill.grid(row= 2,columnspan= 1,sticky='news',ipadx= 10)
    return(green,yellow,blue,red)


def rightwidget(right) :
    txt3 = Label(skright,text="My English Skill",bg="#FFFFFF",fg="#153462",font='Helvetica 16')
    txt3.grid(row=0,column=0,sticky=NW,padx=10,pady=10)
    picsk = Label(skright,image=skill,bg="#FFFFFF")
    picsk.grid(row=1,column=0,sticky="news",pady=10)

def bottomwidget(bottom) :                                         #คำสั่งปุ่ม 3 มิติ
    btn1 = Button(bottom,text="Click me 1",borderwidth=5,relief = GROOVE,command=clickme1)
    btn1.grid(row=0,column=0,ipady=5)
    btn2 = Button(bottom,text="Click me 2",borderwidth=5,relief = GROOVE,command=clickme2)
    btn2.grid(row=0,column=1,ipady=5)
    btn3 = Button(bottom,text="Click me 3",borderwidth=5,relief = GROOVE,command=clickme3)
    btn3.grid(row=0,column=2,ipady=5)
    btn4 = Button(bottom,text="Exit Program",borderwidth=5,relief = GROOVE,command=root.destroy)
    btn4.grid(row=0, column=4,padx=15, sticky= E)

def clickme1() : #คำสั่งโชว์เมสเสจที่ให้คลิก
    messagebox.showinfo("tipparida said :","Click me 1 clicked")

def clickme2() :
    messagebox.showinfo("tipparida said :","Click me 2 clicked")

def clickme3() :
    messagebox.showinfo("tipparida said :","Click me 3 clicked")

root = mainwindow()
female = PhotoImage(file="hw3-images/female.png").subsample(4,4)
skill = PhotoImage(file="hw3-images/skill.png").subsample(2,2)
icon = PhotoImage(file="hw3-images/icon2.png")
root.iconphoto(False,icon) #คำสั่งเปลี่ยนหัวไอคอน window

top,left,right,bottom,mleft,skright = layout(root)
topwidget(top)
leftwidget(left)
rightwidget(right)
bottomwidget(bottom)
root.mainloop()