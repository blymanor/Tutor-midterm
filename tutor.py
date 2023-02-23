import tkinter as tk

def mainwindow() :
    root = tk.Tk()
    root.title("Week7 : My Python GUI Application")
    root.geometry('700x700+400+30')
    root.option_add('*font','garamond 16')
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

    #left side

    #right side

def topside(top) :
    print("Hi topside")


def cakeclick() :
    pos = 0

def drinkclick() :
    pos = 0


def resetclick() :
    for i in range(len(menu1)) :
        amt1[i].set(0)
        amt2[i].set(0)

root = mainwindow()
#create top,left,right,bottom,checkout frame widgets
top = tk.Frame(root,bg='#7286D3')
left = tk.Frame(root,bg='#B9F3FC')
right = tk.Frame(root,bg='#AEE2FF')
bottom = tk.Frame(root,bg="#7286D3")
checkoutframe = tk.Frame(root,bg='#EBC7E6')
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
root.mainloop()