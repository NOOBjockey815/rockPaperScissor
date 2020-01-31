import tkinter
import random
from tkinter import *

root = tkinter.Tk()
root.geometry("900x600")
root.resizable(0,0)

photo = PhotoImage(file="E:\\C code\\RPS_Home\\RPS_Game\\rck.png")
photo2 = PhotoImage(file="E:\\C code\\RPS_Home\\RPS_Game\\scr.png")
photo3 = PhotoImage(file="E:\\C code\\RPS_Home\\RPS_Game\\ppr.png")

ret = "Rock Paper Scissor"

def move(choice,x):
    human(choice,x)

def result(txt,x):
    global ret
    ret = txt
    print(ret)
    var = StringVar()
    var.set(ret)
    text_area = Label(root, textvariable = var, width = 7, height = 4, border = 0, font=("Verdana", 35))
    #text_area.pack(side = BOTTOM)
    text_area.place(relx=0.5,rely=1,anchor=S)
    list = text_area.grid_slaves()
    for l in list:
        l.destroy()
    var.set(ret)

def human(hum,x):
    lis = ["r","p","s"]
    comp = random.choice(lis)

    if(hum == comp):
        result("Draw!",x)
    elif((hum == "r" and comp == "s") or (hum =="s" and comp == "p") or (hum =="p" and comp == "r")):
        result("You Win",x)
    else:
        result("I Win",x)

rck = Button(root, image=photo, command=lambda:move('r',root), border=0,)
rck.place(relx=0.5,rely=0,anchor=N)

scr = Button(root, image=photo2, command=lambda:move('s',root), border=0)
scr.place(relx=0,rely=0.5,anchor=W)

ppr = Button(root, image=photo3, command=lambda:move('s',root), border=0,)
ppr.place(relx=1,rely=0.5,anchor=E)
'''text_area = Label(root, text = str(ret), width = 50, height = 20, border = 0, font=("Verdana", 44))
text_area.pack(side=BOTTOM, pady = 20)'''

root.mainloop()