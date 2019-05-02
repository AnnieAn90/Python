# -*- coding: utf-8 -*
"""
We can use the idea of bisection search to determine if a character is in a string, 
so long as the string is sorted in alphabetical order.
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    def bisection(aStr,firsHalf): # Bisects the string
        if firsHalf: 
            return aStr[:(midindex(aStr))]
        else:
            return aStr[(midindex(aStr)+1):]
            
    def midindex(aStr): # Obtain the mid char index
        if len(aStr)%2 == 1: # odd
            return int((len(aStr)+1)/2-1)
        else:
            return int(len(aStr)/2-1)     
            
    def mid(aStr):# Obtain the mid char 
        if len(aStr)%2 == 1: # odd
            return aStr[int((len(aStr)+1)/2)-1]
        else:
            return aStr[int(len(aStr)/2)-1]

    if aStr == "": # check empty string
        return False
    elif char != mid(aStr):
        if len(aStr)==1:
            return False
        else: # recursive happens
            return isIn(char,bisection(aStr,char < mid(aStr)))
    else:
        return True
       
              
#print(isIn('s','ABs'))    
isIn('j', 'dijklrsv')