# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk,Image
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
# we need ico files
root.iconbitmap('pic2.ico') # this is for icon

# **** images ****
# only works for png files if we do not import ImageTk (small case k)
my_img = ImageTk.PhotoImage(Image.open("pic1.png"))
my_label = Label(image=my_img)
my_label.pack()
#photo = PhotoImage(file="pic1.png")
#label = Label(root,image=photo)
#label.pack()

# **** exit button ****
button_quit = Button(root,text="Exit Program",command = root.destroy) # here we need to use root.destroy instead of root.quit
button_quit.pack()

root.mainloop()
