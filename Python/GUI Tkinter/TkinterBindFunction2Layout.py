# -*- coding: utf-8 -*-
from tkinter import *
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 

Binding a function to a widget to make GUI to interact with our computer programs

"""
# just a blank window，with min/max/close three buttons
root = Tk() 

# print name function
def printName():
    print("Hello, my name is Mike!")

# an event(button click/mouse move/a user can do) means sth occurs 
# when some specific event occurs then call specific function accordingly
def printName2(event):
    print("Hello, Mike again!")    

# Binding a function to a widget  
button_1 = Button(root,text="Print my name",command=printName) # a new parameter called command, whenever i click this run certain function   
button_1.pack() # make this button visible on screen

# another way of Binding a function to a widget  
button_2 = Button(root,text="Print my name2") 
button_2.bind("<Button-1>", printName2) # <Button-1> represents left mouse click
button_2.pack() 


# an infinite loop that never ends, your window constantly displays
root.mainloop()
