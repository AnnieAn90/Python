# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox

"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tkiner.Tk().
Another way is to use "import tkinter as gui", use gui.TK(), alising! 

Creating a message box 

"""
    
# just a blank window，with min/max/close three buttons
root =Tk() 
root.geometry("500x300") # dimension of root window

tkinter.messagebox.showinfo('Window Title', 'Something fun!!')

answer = tkinter.messagebox.askquestion('Question 1','Do you like silly faces?')

if answer == 'yes':
    print('B==D- ')


root.mainloop()
