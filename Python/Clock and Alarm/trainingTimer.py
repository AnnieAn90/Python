# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:43:37 2019

@author: User
"""
from tkinter import*
import time

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(100,tick) # .after(delay in ms, callback function) similar to time.sleep
                          # https://riptutorial.com/tkinter/example/22870/-after--
                          # update the time_string every 100 ms
    
root = Tk()  # just a blank window
clock = Label(root,font=("times",100,"bold"),bg="blue") # Add text
clock.grid(row=0,column=1)
tick()
root.mainloop() # an infinite loop that never ends, your window constantly displays


