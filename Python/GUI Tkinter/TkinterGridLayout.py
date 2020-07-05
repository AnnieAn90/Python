# -*- coding: utf-8 -*-
from tkinter import *
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 

we use an intuitive grid layout

"""
# just a blank window，with min/max/close three buttons
root = Tk() 

label_1 = Label(root,text="Name") # text
label_2 = Label(root,text="Password")
entry_1 = Entry(root) # allow the user to enter input (name/password)
entry_2 = Entry(root) # input fileds

label_1.grid(row=0,sticky=E) # default column is 0, previously we used pack()
label_2.grid(row=1,sticky=E) # E means east (right alignment)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2) # two columns, in one row and merges two columns


# an infinite loop that never ends, your window constantly displays
root.mainloop()
