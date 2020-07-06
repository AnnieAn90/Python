# -*- coding: utf-8 -*-
from tkinter import *
"""
NOTE using this kind of import method we do not need the . sign
or we can use "import tkinter". But with this we need to use tker.Tk().
Another way is to use "import tkinter as gui", thanint use gui.TK(), alising! 

Creating Drop Down Menus

"""

def doNothing():
    print("Hello!")
    
    
# just a blank window，with min/max/close three buttons
root = Tk() 

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu) # creat a submenu inside menu
menu.add_cascade(label="File", menu=subMenu) # cascade is the drop down menu
subMenu.add_command(label="New Project",command=doNothing) # calls do nothing function when we click the submenu
subMenu.add_command(label="Open",command=doNothing) # second dropdown menu
subMenu.add_separator() # create a line that separate one group from another
subMenu.add_command(label="Exit",command=doNothing)

eidtMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=eidtMenu)
eidtMenu.add_command(label="Redo",command=doNothing)

# an infinite loop that never ends, your window constantly displays
root.mainloop()
