# -*- coding: utf-8 -*-
from tkinter import *
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 
"""
# just a blank window，with min/max/close three buttons
root = Tk() 

# top window
topFrame = Frame(root)
topFrame.pack()
# bottom window
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) # side specifies the exact location of your frame

# three buttons on top, 1 on bottom
button1 = Button(topFrame,text="Button 1",fg="red") # put button1 in top frame, fg sets color, text is button1
button2 = Button(topFrame,text="Button 2",fg="blue")
button3 = Button(topFrame,text="Button 3",fg="green")
button4 = Button(bottomFrame,text="Button 4",fg="purple")
button1.pack(side=LEFT) # display buttons on your screen
button2.pack(side=LEFT) # by default, when you pack things, they are pack on top of each other
button3.pack(side=LEFT) # however, pack(parameter)
button4.pack(side=BOTTOM)

# an infinite loop that never ends, your window constantly displays
root.mainloop()
