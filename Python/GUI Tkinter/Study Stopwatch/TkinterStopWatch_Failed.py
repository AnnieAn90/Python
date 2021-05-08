# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:39:00 2021

@author: User
"""

from tkinter import *
import time
import math

# Let's create the Tkinter window
window = Tk()

# Then, you will define the size of the window in width(312) and height(324) using the 'geometry' method
window.geometry("312x374")

# In order to prevent the window from getting resized you will call 'resizable' method on the window
window.resizable(0, 0)

#Finally, define the title of the window
window.title("Stop Watch")


# Let's now define the required functions for the Calculator to function properly.
# click button
def btn_click(item):
    global expression
    expression = item
    print(expression)
    input_text.set(str(expression))
    
# start button
def btn_start():
    global expression
    print('Satrt the program')
    print(expression)
    tick()
    expression = ""

# fucntion counts how much time has passed
def counter_study(minitues,lap,hours):
    # j is a global conuter
    global j
    output_str = 'Lap'+str(lap)+'/'+ str(hours) +': '+ 'Study ' + str(j) + '/45 min'
    print(output_str)
    label.config(text=output_str)
    if j<minitues:
        j = j+1
        label.after(1000,counter_study(minitues,lap,hours))
  
def counter_rest(minitues,lap,hours):
    global j
    output_str = 'Lap'+str(lap)+'/'+ str(hours) +': '+ 'Rest ' + str(j) + '/15 min'
    label.config(text=output_str)
    if j<minitues:
        j = j+1
        label.after(1000,counter_rest(minitues,lap,hours))                 
        
# function does our main loop    
def stopwatch(hours):
    global j
    print('Start the count down')
    if hours>1:
         for i in range(1,hours+1):
             j = 0
             counter_study(45,i,hours)
             j = 0
             counter_rest(15,i,hours)  
         label.config("You have finished your study!")    
    else:
         print('Start first study count')
         j = 0
         counter_study(45,1,hours);
         print('Start first rest count')
         j = 0
         counter_rest(15,1,hours);
         label.config("You have finished your study!")  
                  
def tick():
    global i 
    if i < 5:
        time_string = "This is lap # "+ str(i)
    else:
        time_string = "This is lap # "+ str(i) + "Rest !"
    label.config(text=time_string)
    if i < 10:
        i = i+1
        label.after(1000,tick) 

   
# empty expression
expression = ""
# In order to get the instance of the input field 'StringVar()' is used
input_text = StringVar()    

# The first thing is to create a frame for the input field
input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

# Then you will create an input field inside the 'Frame' that was created in the previous step. Here the digits or the output will be displayed as 'right' aligned
input_field = Entry(input_frame, font = ('arial', 18, 'bold'),textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = CENTER)
input_field.grid(row = 0, column = 0,padx = 1, pady = 1)
input_field.pack(ipady = 10) # 'ipady' is an internal padding to increase the height of input field

label_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
label_frame.pack()

label = Label(label_frame, font=("times",18,"bold"), bg = "blue", bd = 0,justify = CENTER)
label.grid(row = 0, column = 0,padx = 1, pady = 1) # Add text                   
label.pack(ipady = 10) # 'ipady' is an internal padding to increase the height of input field



# Once you have the input field defined then you need a separate frame which will incorporate all the buttons inside it below the 'input field'
btns_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

# The 1st row will comprise of the buttons '7', '8', '9' 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 0, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 0, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 0, column = 2, padx = 1, pady = 1)
              
# The 2nd row will comprise of the buttons '4', '5', '6' 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 1, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 1, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 1, column = 2, padx = 1, pady = 1)    
             
# The 3rd row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 2, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 2, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 2, column = 2, padx = 1, pady = 1)

# Finally, the 4th row include 10 and the satrt button
ten = Button(btns_frame, text = "10", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(10)).grid(row = 3, column = 0, padx = 1, pady = 1)
start_button = Button(btns_frame, text = "Start", fg = "black", width = 21, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: tick()).grid(row = 3, column = 1, columnspan = 2, padx = 1, pady = 1)   
     
                                           
window.mainloop()