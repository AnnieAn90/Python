# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox

"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tkiner.Tk().
Another way is to use "import tkinter as gui", use gui.TK(), alising! 

Creating a shapes and graphics
"""
    
# just a blank window，with min/max/close three buttons
root =Tk() 
#root.geometry("500x300") # dimension of root window

canvas = Canvas(root,width=200,height=100) # you can draw(make shapes) on a piece of canvas
canvas.pack()

blackLine = canvas.create_line(0,0,200,50) # 0,0 is initial, 200,50 is final
redLine = canvas.create_line(0,100,200,50,fill="red")
greenBox = canvas.create_rectangle(25,25,130,60, fill = "green") # 25,25 is position of top left point, 130 is width, 60 is height

canvas.delete(redLine) # delete an object on canvas
canvas.delete(ALL) # delete all objects on canvas

root.mainloop()
