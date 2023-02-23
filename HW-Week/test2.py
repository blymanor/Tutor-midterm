from cProfile import label
import tkinter as tk
from turtle import title

def mainwindow() :
  root = tk.Tk()
  root.title("Week6 : Menu widget") 
  root.geometry('700x600')
  root.option_add('*font','garamond 14')
  root.config(bg='#6096B4')
  return(root)

def productmenu() :
  frame1 = tk.Frame(root,bg='#93BFCF')
  frame1.place(x=0,y=0,width=700,height=600)
  frame1.columnconfigure((0,1),weight=1) 
  pos = 0
  pos2 = 0 
  for i,menu in enumerate(menu1) :
    tk.Label(frame1,bg="#93BFCF",fg='blue',text=menu).grid(row=[pos],column=0) 
    tk.Label(frame1,bg="#93BFCF",image=cakes[i]).grid(row=pos+1,column=0,pady=10) 
    tk.Label(frame1,bg="#93BFCF",text="Price : "+str(price1[i])).grid(row=pos+2,column=0,pady=10) 
    tk.Spinbox(frame1,from_=0,to=100,width=10,justify='center',textvariable=amt1[i]).grid(row=pos+3,column=0,pady=10) 
    pos += 4

  for i,menu in enumerate(menu2) :
    tk.Label(frame1,bg="#93BFCF",fg='blue',text=menu).grid(row=[pos2],column=1) 
    tk.Label(frame1,bg="#93BFCF",image=drinks[i]).grid(row=pos2+1,column=1,pady=10) 
    tk.Label(frame1,bg="#93BFCF",text="Price : "+str(price2[i])).grid(row=pos2+2,column=1,pady=10) 
    tk.Spinbox(frame1,from_=0,to=100,width=10,justify='center',textvariable=amt2[i]).grid(row=pos2+3,column=1,pady=10) 
    pos2 += 4

def checkout() :
  global total1,total2
  total1,total2 = 0,0
  frame2 = tk.Frame(root,bg='#BDCDD6')
  frame2.place(x=0,y=0,width=700,height=600)
  frame2.rowconfigure((0,1,2,3,4,5),weight=1)
  frame2.columnconfigure((0,1,2,3),weight=1)
  menulist = ["Menu List","Amount","Price","Total(Bahts)"]
  productlist = ['Strawberry Cake',"Cheese Cake",'Strawberry Mixed','Orange Mixed']
  #type your code here
  for i,title in enumerate(menulist) :
    tk.Label(frame2,bg="#BDCDD6",text=title).grid(row=0,column=i)
    tk.Label(frame2,bg="#BDCDD6",text=productlist[i],fg='blue').grid(row=i+1,column=0,sticky='e')
  pos = 1
  for i in range(len(menu1)) :
    tk.Label(frame2,bg="#BDCDD6",text=str(amt1[i].get())).grid(row=pos,column=1)
    tk.Label(frame2,bg="#BDCDD6",text=str(price1[i])).grid(row=pos,column=2)
    totalcake = amt1[i].get() * price1[i]
    total1 += totalcake
    tk.Label(frame2,bg="#BDCDD6",text=str(totalcake)).grid(row=pos,column=3)
    pos += 1
  for i in range(len(menu2)) :
    tk.Label(frame2,bg="#BDCDD6",text=str(amt2[i].get())).grid(row=pos,column=1)
    tk.Label(frame2,bg="#BDCDD6",text=str(price2[i])).grid(row=pos,column=2)
    totaldrink = amt2[i].get() * price2[i]
    total1 += totaldrink
    tk.Label(frame2,bg="#BDCDD6",text=str(totaldrink)).grid(row=pos,column=3)
    pos += 1

  tk.Label(frame2,bg='#F8CBA6',fg='blue',font=("Garamond",22,'bold'),textvariable=output).grid(row=pos+2,pady=10,columnspan=4)
  total = total1 + total2
  print("Total = ",total)
  output.set("Total price = %0.2f"%total)
    
def createmenu(root) :
  menubar = tk.Menu(root)
  #use method add_command to add menu and take user action from click
  menubar.add_command(label="Product Menu",command=productmenu)
  menubar.add_command(label="Check out",command=checkout)
  menubar.add_command(label="Exit Program",command=root.quit)
  root.configure(bg="pink",menu=menubar)

root = mainwindow()
img1 = tk.PhotoImage(file="image/myshop.png")
img2 = tk.PhotoImage(file="image/drink1.png")
img3 = tk.PhotoImage(file="image/drink2.png")
img4 = tk.PhotoImage(file="image/cake1.png")
img5 = tk.PhotoImage(file="image/cake2.png")
drinks = [img2,img3]
cakes = [img4,img5]
menu1 = ['Strawberry Cake',"Cheese Cake"]
menu2 = ['Strawberry Mixed','Orange Mixed']
price1 = [85,95]
price2 = [120,140]
amt1 = [tk.IntVar() for x in menu1] #spy of cake
amt2 = [tk.IntVar() for x in menu2] #spy of drink
total = 0.0
total1 = 0.0            #to correct total of cake price
total2 = 0.0            #to correct total of drink price
output = tk.StringVar() #spy of output label
createmenu(root)        #call function to create menubar
productmenu()
root.mainloop()
