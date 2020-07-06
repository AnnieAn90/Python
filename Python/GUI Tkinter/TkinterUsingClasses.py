# -*- coding: utf-8 -*-
from tkinter import *
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 

Using classes with Tkinter

"""

class MyButtons:
    def __init__(self, master):
        frame = Frame(master) # root is our master
        frame.pack()
        
        self.printButton = Button(frame,text="Print Message", command=self.printMessage) # printMessage is our print function
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(frame,text="Quit", command=frame.quit) # frame.quit is built-in, we do not need to write a new function
        self.quitButton.pack(side=LEFT)
    
    def printMessage(self):
         print("Nice work!")

# just a blank window，with min/max/close three buttons
root = Tk() 

# creat an object from MyButton class
b = MyButtons(root)

# an infinite loop that never ends, your window constantly displays
root.mainloop()
