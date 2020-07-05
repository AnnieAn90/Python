# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import*
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 
"""
# just a blank window，with min/max/close three buttons
root = Tk() 
# Add text to the blank window, we use label to create basic text
newText = Label(root, text="This is too easy!") 
newText.pack() # pack the first place, tells you where to palce your text
 # an infinite loop that never ends, your window constantly displays
root.mainloop()


