# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox

"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tkiner.Tk().
Another way is to use "import tkinter as gui", use gui.TK(), alising! 

Include images and icons (i.e. feather)
"""
    
# just a blank window，with min/max/close three buttons
root =Tk() 
root.title("Images and Icons")
#root.geometry("500x300") # dimension of root window

# **** icon ****
root.iconbitmap()

#photo = PhotoImage(file="pic1.jpg")
#label = Label(root,image=photo)
#label.pack()

root.mainloop()
