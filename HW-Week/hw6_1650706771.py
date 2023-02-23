import tkinter as tk

def mainwindow() :
  root = tk.Tk()
  root.title("Week6 : Menu widget by Tipparida Rujisunkuntorn") 
  root.geometry('700x600')
  root.option_add('*font','garamond 14')
  root.config(bg='#EAE7B1')
  return(root)

def productmenu() :
  frame1 = tk.Frame(root,bg='#CEE5D0')
  frame1.place(x=0,y=0,width=700,height=600)
  frame1.columnconfigure((0,1,2,3),weight=1) 

  pos = 0
  for i,menu in enumerate(menu1) :
    tk.Label(frame1,bg="#CEE5D0",fg='blue',text=menu).grid(row=[pos],column=0,pady=10) 
    tk.Label(frame1,bg="#CEE5D0",fg='blue',text="Price : "+str(price1[i])).grid(row=pos+1,column=0,pady=5,sticky='N') 
    tk.Spinbox(frame1,from_=0,to=100,width=10,justify='center',textvariable=amt1[i]).grid(row=pos+2,column=0,pady=10) 
    pos += 3
  pos = 0
  for i in range(len(cakes)) :
    tk.Label(frame1,bg="#CEE5D0",image=cakes[i]).grid(row=pos+1,column=1)
    pos += 3    

  pos = 0
  for i,menu in enumerate(menu2) :
    tk.Label(frame1,bg="#CEE5D0",fg='blue',text=menu).grid(row=[pos],column=2,pady=10) 
    tk.Label(frame1,bg="#CEE5D0",fg='blue',text="Price : "+str(price2[i])).grid(row=pos+1,column=2,pady=5,sticky='N') 
    tk.Spinbox(frame1,from_=0,to=100,width=10,justify='center',textvariable=amt2[i]).grid(row=pos+2,column=2,pady=10) 
    pos += 3
  pos = 0
  for i in range(len(drinks)) :
    tk.Label(frame1,bg="#CEE5D0",image=drinks[i]).grid(row=pos+1,column=3) 
    pos += 3
      

def checkout() :
  global total,total1,total2
  total1,total2 = 0,0
  frame2 = tk.Frame(root,bg='#A6BB8D')
  frame2.place(x=0,y=0,width=700,height=600)
  frame2.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
  frame2.columnconfigure((0,1,2,3),weight=1)
  menulist = ["Menu List","Amount","Price","Total(Bahts)"]
  productlist = ['Strawberry Cake',"Cheese Cake","DIY Cake",'Strawberry Mixed','Orange Mixed','Coffee']
  for i,title in enumerate(menulist) :
      tk.Label(frame2,bg="#A6BB8D",text=title).grid(row=0,column=i)
  for i,product in enumerate(productlist) :
      tk.Label(frame2,bg="#A6BB8D",fg="blue",text=product).grid(row=i+1,column=0,sticky="e")

  pos = 1
  for i in range(len(menu1)) :
      tk.Label(frame2,bg="#A6BB8D",text=str(amt1[i].get())).grid(row=pos,column=1)
      tk.Label(frame2,bg="#A6BB8D",text=str(price1[i])).grid(row=pos,column=2)
      totalcake = amt1[i].get() * price1[i]
      total1 += totalcake
      tk.Label(frame2,bg="#A6BB8D",text=str(totalcake)).grid(row=pos,column=3)
      pos += 1

  for i in range(len(menu2)) :
      tk.Label(frame2,bg="#A6BB8D",text=str(amt2[i].get())).grid(row=pos,column=1)
      tk.Label(frame2,bg="#A6BB8D",text=str(price2[i])).grid(row=pos,column=2)
      totaldrink = amt2[i].get() * price2[i]
      total2 += totaldrink
      tk.Label(frame2,bg="#A6BB8D",text=str(totaldrink)).grid(row=pos,column=3)
      pos += 1

  tk.Checkbutton(frame2,text="HAVE A MEMBER : (Click) YES (Discount 10%) or (Blank) NOT A MEMBER",bg="#A6BB1D",font=("Garamond",16),variable=spy,command=discount).grid(row=7,columnspan=4)
  tk.Label(frame2,bg="#A6BB8D",fg="blue",font=("Garamond",16,"bold"),textvariable=output).grid(row=8,columnspan=4)
  total = total1 + total2
  print("Total = ",total)
  output.set("Total Price = %.2f"%total)

def discount() :
  global total
  if spy.get() == 1 :
    dis = total * 10/100
    dis_total = total - dis
    output.set("Total Price = %.2f"%dis_total)
  else :
    output.set("Total Price = %.2f"%total)

def createmenu(root) :
  menubar = tk.Menu(root)
  menubar.add_command(label="Product Menu",command=productmenu)
  menubar.add_command(label="Check out",command=checkout)
  menubar.add_command(label="Exit Program",command=root.quit)
  root.configure(bg="#EAE7B1",menu=menubar)

root = mainwindow()
img1 = tk.PhotoImage(file="image/drink1.png")
img2 = tk.PhotoImage(file="image/drink2.png")
img3 = tk.PhotoImage(file="image/coffee1.png")
img4 = tk.PhotoImage(file="image/cake1.png")
img5 = tk.PhotoImage(file="image/cake2.png")
img6 = tk.PhotoImage(file="image/cake4.png")
drinks = [img1,img2,img3]
cakes = [img4,img5,img6]
menu1 = ['Strawberry Cake',"Cheese Cake","DIY Cake"]
menu2 = ['Strawberry Mixed','Orange Mixed','Coffee']
price1 = [85,95,100]
price2 = [120,140,80]
amt1 = [tk.IntVar() for x in menu1] 
amt2 = [tk.IntVar() for x in menu2] 
total = checkout
total1 = 0.0            
total2 = 0.0
spy = tk.IntVar()            
output = tk.StringVar()
productmenu()
createmenu(root)
root.mainloop()