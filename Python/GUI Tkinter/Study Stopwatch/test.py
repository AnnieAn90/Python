# -*- coding: utf-8 -*-
"""
Created on Sat May  8 08:48:35 2021

@author: User
"""
# https://www.tutorialspoint.com/python/tk_label.htm

from tkinter import *
import time

i = 0

def tick():
    global i 
    time_string = "This is lap # "+ str(i)
    label.config(text=time_string)
    if i < 10:
        label.after(1000,tick) 
    i = i+1

root = Tk()
label = Label(root,font=("times",100,"bold"),bg="blue") # Add text
label.grid(row=0,column=1)
label.pack()
tick()
root.mainloop()