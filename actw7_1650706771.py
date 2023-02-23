from operator import le
import tkinter as tk
from tkinter.ttk import Button

def mainwindow() :
    root = tk.Tk()
    root.title("Week7 : My Python GUI Application")
    root.geometry('700x700+400+30') #+400+30 คือขยับ mainwin อยู่ center หน้าจอ
    root.option_add('*font','garamond 15')
    root.config(bg='pink')
    root.grid_rowconfigure((0,2),weight=1)
    root.grid_rowconfigure(1,weight=5)
    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=5)
    return(root)

def layout() :
    #top side
    top.grid(row=0,column=0,columnspan=2,sticky='news')
    top.grid_columnconfigure((0,1,2),weight=1)
    top.grid_rowconfigure(0,weight=1)
    #bottom side
    bottom.grid(row=2,columnspan=2,sticky='news')
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure((0,1),weight=1) 
    #left side
    left.grid(row=1,column=0,sticky='news')
    left.columnconfigure(0,weight=1)
    left.rowconfigure((0,1,2,3,4,5),weight=1)
    #right side
    right.grid(row=1,column=1,sticky='news')
    right.rowconfigure((0,1,2),weight=1)
    right.columnconfigure((0,1),weight=1)


def topside(top) :
    tk.Button(top,text="Cake Menu",image=b1,compound='top',command=cakeclick).grid(row=0,column=0,sticky='news')
    tk.Button(top,text="Drink Menu",image=b2,compound='top',command=drinkclick).grid(row=0,column=1,sticky='news')
    tk.Button(top,text="Check out",image=b3,compound='top',command=checkout).grid(row=0,column=2,sticky='news')

def bottomside(bottom) :
    tk.Button(bottom,text="Reset submit",command=resetclick).grid(row=0,column=0,sticky='news')
    tk.Button(bottom,text="Exit Program",image=b4,compound='left',command=quit).grid(row=0,column=1,sticky='news')

def cakeclick() :
    checkoutframe.grid_forget()
    layout()
    pos = 0
    for i,menu in enumerate(menu1) :
        tk.Label(left,text=menu,bg='#FFD495').grid(row=pos,ipadx=15)
        tk.Label(left,image=cakes[i],bg='#FFD495').grid(row=pos+1,ipadx=15,ipady=15) #ใช้ ipadx ipady เผื่อขยับไม่ให้ภาพซ้อยทับกัน
        tk.Label(right,text="( Price : "+str(price1[i])+") Amount : ",bg='#FAAB78').grid(row=i,column=0,sticky='e',ipadx=15)
        tk.Spinbox(right,from_=0,to=100,width=10,justify='center',textvariable=amt1[i]).grid(row=i,column=1)
        #tk.Entry(right,width=10,justify='center',textvariable=amt1[i]).grid(row=i,column=1)
        pos += 2

def drinkclick() :
    checkoutframe.grid_forget()
    layout()
    pos = 0
    for i,menu in enumerate(menu2) :
        tk.Label(left,text=menu,bg='#FFD495').grid(row=pos)
        tk.Label(left,image=drinks[i],bg='#FFD495').grid(row=pos+1)
        tk.Label(right,text="( Price : "+str(price2[i])+") Amount : ",bg='#FAAB78').grid(row=i,column=0,sticky='e',ipadx=15)
        tk.Spinbox(right,from_=0,to=100,width=10,justify='center',textvariable=amt2[i]).grid(row=i,column=1)
        #tk.Entry(right,width=10,justify='center',textvariable=amt2[i]).grid(row=i,column=1)
        pos += 2

def resetclick() :
    for i in range(len(menu1)) :
        amt1[i].set(0)
        amt2[i].set(0)

def checkout() :
    left.grid_forget()
    right.grid_forget()
    checkoutframe.grid(row=1,columnspan=2,sticky='news')
    checkoutframe.columnconfigure(0,weight=1)
    checkoutframe.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    tk.Label(checkoutframe,bg='#FFFBAC',text="   Summary of Cakes/Drinks   ",font=("Comic Sans Ms",22,'bold'),fg='blue').grid(row=2)
    #calculator
    sumc,sumd = 0,0
    for  i in range(len(menu1)) :
        sumc += amt1[i].get() * price1[i]
        sumd += amt2[i].get() * price2[i]
    showc = tk.StringVar()
    tk.Label(checkoutframe,bg='#FFD495',textvariable=showc).grid(row=3,sticky='news')
    showc.set("Total cakes price = %0.2f Baths"%sumc)
    showd = tk.StringVar()
    tk.Label(checkoutframe,bg='#FAAB78',textvariable=showd).grid(row=4,sticky='news')
    showd.set("Total drinks price = %0.2f Baths"%sumd)
    output = tk.StringVar()
    tk.Label(checkoutframe,bg='#FFFBAC',textvariable=output,font=("Comic Sans Ms",22,'bold'),fg='blue').grid(row=6)
    output.set("Total prices = %0.2f Baths"%(sumc+sumd))

#calculator_discount
 #global total
  #if spy.get() == 1 :
   #dis = total * 10/100
   #dis_total = total - dis
   # output.set("Total Price = %.2f"%dis_total)   (ใช้ Set สำหรับหาค่าที่ไม่ซ้ำกันภายในลิสต์ ตรวจสอบข้อมูลที่มีอยู่แล้ว)
  #else :
   # output.set("Total Price = %.2f"%total)


root = mainwindow()
#create top,left,right,bottom,checkout frame widgets
top = tk.Frame(root,bg='#D7E9B9')
left = tk.Frame(root,bg='#FFD495')
right = tk.Frame(root,bg='#FAAB78')
bottom = tk.Frame(root,bg="#D7E9B9")
checkoutframe = tk.Frame(root,bg='#FFFBAC')
#define images for using in this program
img1 = tk.PhotoImage(file="image/drink1.png")
img2 = tk.PhotoImage(file="image/drink2.png")
img3 = tk.PhotoImage(file="image/drink3.png")
img4 = tk.PhotoImage(file="image/cake3.png")
img5 = tk.PhotoImage(file="image/cake2.png")
img6 = tk.PhotoImage(file="image/cake4.png")
b1 = tk.PhotoImage(file="image/cake-button.png")
b2 = tk.PhotoImage(file="image/drink-button.png")
b3 = tk.PhotoImage(file="image/checkout.png")
b4 = tk.PhotoImage(file="image/exit.png")
drinks = [img1,img2,img3]
cakes = [img4,img5,img6]
menu1 = [' Strawberry Cake '," Cheese   Cake  ","Newyork Cheese Cake"]
menu2 = ['| Orange   Mixed |',' Lemonade Mixed ',"| Mojito  Miexd  Berry |"]
price1 = [145,120,130]
price2 = [120,100,90]
amt1 = [tk.IntVar() for x in menu1] #spy of cake
amt2 = [tk.IntVar() for x in menu2] #spy of drink
total = 0
discount = 0
net = 0
layout()
topside(top)
bottomside(bottom)
root.mainloop()