# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:52:46 2021

@author: User
"""

import time
import math

# fucntion counts how much time has passed
def counter(minitues):
    start = time.time()
    elapsed = 0
    while elapsed < minitues*60:
        elapsed = time.time() - start
        print("loop cycle time: %f, minitues count: %02d" % (time.clock() , math.floor(elapsed/60)))
        time.sleep(60)   
        
# function does our main loop    
def stopwatch(hours):
    if hours>1:
         for i in range(1,hours+1):
             print("This is round %d",i)
             print("Study!")
             counter(45)
             print("Rest!")
             counter(15)        
    else:
        # print study and produce the beeping sound
         print("Study!")
         counter(45);
         # print rest and produce the beeping sound
         print("Rest!")
         counter(15);
              
# run the function            
stopwatch(1)