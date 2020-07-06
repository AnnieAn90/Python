# -*- coding: utf-8 -*-
from tkinter import *
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 

You can have a button: something happens if you left click it and something else
happens if you right click it.

One widget that can handle multiple events

"""
# just a blank window，with min/max/close three buttons
root = Tk() 

def leftClick(event):
    print("Left")
    
def rightClick(event):
    print("Right")

def middleClick(event):
    print("Middle")
    
frame = Frame(root, width=300, height=250) # 300 pixel, root is our main window
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick) # not working, 4 for scroll up, 5 for down
frame.bind("<Button-3>",rightClick) 

frame.pack() # display the frame

# an infinite loop that never ends, your window constantly displays
root.mainloop()
