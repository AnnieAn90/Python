# -*- coding: utf-8 -*-
"""
Created on Sat May  8 08:48:35 2021

@author: User
"""
# https://www.tutorialspoint.com/python/tk_label.htm

from tkinter import *
import time
import math
import os

i = 1

def tick():
    time_string = time.strftime("%H:%M")
    global i 
    if 0<i%60<=45 :
        output_string = "Lap "+ str(math.ceil(i/60)) + '/10' + ' Study '+ str(i%60) + '/45' + 'min' + os.linesep + time_string
    else: 
        if i%60==0:
            output_string = "Lap "+ str(math.ceil(i/60)) + '/10' + ' Rest ' + '15/15' + 'min' +  os.linesep + time_string
        else:
            output_string = "Lap "+ str(math.ceil(i/60)) + '/10' + ' Rest '+ str(i%60-45) + '/15' + 'min' + os.linesep + time_string
    label.config(text=output_string)
    if i < 601:
        i = i+1
        label.after(1000*60,tick) 

root = Tk()
label = Label(root,font=("times",100,"bold"),bg="blue") # Add text
label.grid(row=0,column=1)
label.pack()

tick()
root.mainloop()