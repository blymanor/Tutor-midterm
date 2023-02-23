from tkinter import *

def mainwindow() :
    root = Tk()
    root.title("GUI3: Class Activity of Week4 created by Tipprida Rujisunkuntorn")
    root.geometry("600x500")
    root.configure(bg='lightgreen')
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.wm_attributes('-transparentcolor', 'red')
    return(root)

def layout(root) :
    top = Frame(root,bg="#62B6B7")
    top.grid(row=0, columnspan = 3, sticky='news')
    top.grid_columnconfigure((0,1),weight=1)
    top.grid_rowconfigure(0,weight=1)

    left = Frame(root,bg="#CBEDD5",width=200)
    left.grid(row=1,column=0,sticky='news')

    right = Frame(root,bg="#97DECE",width=200)
    right.grid(row=1,column=1,sticky='news')

    bottom = Frame(root,bg="#62B6B7")
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(top,left,right,bottom)

def topside(top) :
    title = Label(top,text="My Cake Shop by Tipparida",font='Helvetica 15',bg="#62B6B7",fg="#00425A",width=100).grid(row=0, sticky='e', ipady=10)


def calculate_total():
    total = 0
    total += price1 * int(sptxt1.get())
    total += price2 * int(sptxt2.get())
    total += price3 * int(sptxt3.get())
    showtotal.config(font='Helvetica 15',text='Total : ' + str(total) + " Bahts",bg="#79B4B7", fg="blue")
    
def leftside(left) :
    product1 = Label(left,image=cake1,bg="#CBEDD5")
    product1.grid(row=0,padx=15,pady=5)

    txt1 = Label(left,text="Chocolate Cake\nPrice 160 bahts",font='Helvetica 10',bg="#CBEDD5")
    txt1.grid(row=0,column=1,sticky=N,pady=15)
    global sptxt1
    sptxt1 = Spinbox(left, from_=0,to=20,bg='white',command=calculate_total)
    sptxt1.grid(row=0,column=1,pady=55)

    product2 = Label(left,image=cake2,bg="#CBEDD5")
    product2.grid(row=1,padx=15,pady=5)

    txt2 = Label(left,text="Strawberry Cake\nPrice 170 bahts",font='Helvetica 10',bg="#CBEDD5")
    txt2.grid(row=1,column=1,sticky=N,pady=15)
    global sptxt2
    sptxt2 = Spinbox(left, from_=0,to=20,bg='white',command=calculate_total)
    sptxt2.grid(row=1,column=1,pady=55)

    product3 = Label(left,image=cake3,bg="#CBEDD5")
    product3.grid(row=2,padx=15,pady=5)

    txt3 = Label(left,text="Donut Party\nPrice 45 bahts",font='Helvetica 10',bg="#CBEDD5")
    txt3.grid(row=2,column=1,sticky=N,pady=15)
    global sptxt3
    sptxt3 = Spinbox(left, from_=0,to=20,bg='white',command=calculate_total)
    sptxt3.grid(row=2,column=1,pady=55)

def rightside(right) :
    txt = Label(right,text="\tThank You for your shopping\n\tTotal Price is",font='Helvetica 12',bg="#97DECE")
    txt.grid(row=0,column=1,columnspan=2)
    global showtotal
    showtotal = Label(right,font='Helvetica 15', text='Total : 0 Bahts',bg="#79B4B7", fg="blue")
    showtotal.grid(row=3, column=2,pady=60)

def bottomside(bottom) :
    btn = Button(bottom,text="Exit Program",borderwidth=5,relief = GROOVE,command=quit)
    btn.grid(row=2,ipadx=20,padx=450,pady=20)

price1 = 160
price2 = 170
price3 = 45
root = mainwindow()
top,left,right,bottom = layout(root)
cake1 = PhotoImage(file="image/cake1.png")
cake2 = PhotoImage(file="image/cake2.png")
cake3 = PhotoImage(file="image/cake3.png")
topside(top)
bottomside(bottom)
leftside(left)
rightside(right)
root.mainloop()