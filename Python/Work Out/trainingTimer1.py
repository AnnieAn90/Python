# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:02:27 2019

@author: User
"""

import time

# Wait for 5 seconds
# time.sleep(5)
 
# Wait for 300 milliseconds
# .3 can also be used
# time.sleep(.300)

sets = input("How many sets?")
duration = input("Hold on for how long?")
rest = input("Rest time in between?")

sets = int(sets)
duration = int(duration)
rest = int(rest)

for i in range(1,sets+1): # note range(1,3) gievs 1,2; range(2) gives 0,1
    print("Set "+ str(i))
    for j in range(1,duration+rest+1):
        if j <= duration:
            print("Hold on for "+ str(j))
        else:
            print("Rest for "+ str(j-5))  
        time.sleep(1)
        
    
        