# -*- coding: utf-8 -*-
from tkinter import *
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 
"""
# just a blank window，with min/max/close three buttons
root = Tk() 

one = Label(root,text="One",bg="red",fg="white") # bg is backgroud color, fg is frontground color(text)
one.pack() # pack this on screen
two = Label(root,text="Two",bg="green",fg="black")
two.pack(fill=X) # label size will grow in x-direction when you change the window size
three = Label(root,text="Three",bg="blue",fg="white") 
three.pack(side=LEFT,fill=Y) # gow in Y-direction

# an infinite loop that never ends, your window constantly displays
root.mainloop()
