# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import*
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tkinter.Tk().
"""

root = Tk() # just a blank window
newText = Label(root, text="This is too easy!") # Add text
newText.pack() # pack the first place, tells you where to palce your text
root.mainloop() # an infinite loop that never ends, your window constantly displays


