# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:00:16 2018

@author: User

CREATE STRUCTURE WITH DECOMPOSITION AND ABSTRACTION

A docstring is a string literal that occurs as the first statement in 
a module, function, class, or method definition. Such a docstring 
becomes the __doc__ special attribute of that object.
docstrings : 文档字符串
"""

"""
FUNCTIONS
ARE NOT RUN IN A PROGRAM UNTIL THEY ARE CALLED/INVIKED
THEY HAVE: NAME, PARAMETERS (0, OR MORE), DOCSTRING(EXPLAIN WHAT A FUNCTION DOES) , BODY
"""
def is_even(i): # def IS A KEYWORD, IS_EVEN (NAME), i is PARAMETER/ARGUMENT
    """
    INPUT: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("hi")
    return i%2 == 0 # None, if no return given, only one return executed inside a function
                    # code insider function but after return statement noe excuted

x = is_even(3) # x is False

def func_a(): # no parameter
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a)) # call func_c, takes one parameter, another function (a func invokes another func)

# INSIDE A FUCNTION, CAN ACCESS A VARIABLE DEFINED OUTSIDE
# INSIDE A FUCNTION, CANNOT MODIFY A VARIABLE DEFINED OUTSIDE
def g(y):
    print(x)
    print(x+1) # x = x+1 is not valid
x = 5
g(x)
print(x)


"""
A FUNCTION DEFINED INSIDE ANOTHER FUNCTION
"""
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x = ', x)
    h()
    return x

x = 3
z = g(x)

"""
KWYWORD ARGUMENTS AND DEFAULT VALUES
"""
def printName(firstName,lastName,reverse):
    if reverse:
        print(lastName + ','+firstName)
    else:
        print(firstName,lastName)
        
# EACH OF RHESE ONVOCATIONS IS EQUIVALENT
printName('Zipeng','Huang',False)
printName('Zipeng','Huang',reverse = False)
printName('Zipeng',lastName = 'Huang',reverse = False)
# THE LAST INVOCATION IS RECOMMENDED SINCE IT IS ROBUST 
printName(lastName = 'Huang',firstName = 'Zipeng', reverse = False)

"""
WE CAN ALSO SPECIFY THAT SOME ARGUMENTS HAVE DEFAULT VALUES, SO IF NO VALUE
SUPPLIED, JUST USE THAT VALUE
"""
def printName(firstName,lastName,reverse = False):
    if reverse:
        print(lastName + ','+firstName)
    else:
        print(firstName,lastName)

printName('Zipeng','Huang')
printName('Zipeng','Huang',True)


"""
STRING METHOD: EVERYTHING IN PYTHON IS AN OBJECT. OBJECTS ARE SPECIAL BECAUSE WE 
CAN ASSOCIATE SPECIAL FUNCTIONS, REFERRED TO AS OBJECT METHODS, WITH THE OBJECT. 
HERE, WE WILL WOTK WITH STRING OBJECTS, AND THEIR BUILT-IN METHODS
(SEE THE LINK FOR AVAILABLE METHODS TO STRING OBJECTS)
https://docs.python.org/3/library/stdtypes.html#string-methods
"""
s = 'abc'
s.capitalize # returns the function type
s.capitalize() # invoke the function and returns Abc
s.upper() # Return a copy of the string with all the cased chars converted to uppercase
s.isupper() # Return true if all cased characters in the string are uppercase
            # and there is at least one cased character, false otherwise.
s.islower() # similar to s.isupper
s.swapcase() #Return a copy of the string with uppercase chars converted to lowercase, vice versa.
s.find('e') # Return the lowest index in the string where substring 'e' is found,-1 if sub is not found
s.index('e') # Like find(), but raise ValueError when the substring is not found.
s.count('e') # Return the number of non-overlapping occurrences of substring e
s.repalce('old','new') # Return a copy of the str, all occurrences of substr 'old' replaced by 'new'


"""
RECURSION PROBLEM (DIVIDE AND CONQUER, A FUNCTION CALLS ITSELF)
1. RECURSIVE STEP: THINK HOW TO REDUCE PROBLEM TO A SIMPLER/SMALLER VERSION OF SAME PROBLEM.
2. BASE CASE: KEEP REDUCING RPOBLEM UNTIL REACH A SIMPLE CASE THAT CAN BE SOLVED DIRECTLY.

ITERATION vs. RECURSION (DOES THE SAME THING)
1. RECURSION MAY BE SIMPLER, MORE INTUITIVE 
2. RECURSION MAY BE EFFICIENT FROM PROGRAMMER'S POINT OF VIEW
3. RECURSION MAY NOT BE EFFICIENT FROM COMPUTER POINT OF VIEW
"""
# MULTIPLICATION-RECURSIVE SOLUTION
# MATHEMATICAL INDUCTION REASONING OF THE CODE
def mult(a,b):
    if b == 1: # BASE CASE
        return a
    else: # RECURSIVE STEP
        return a + mult(a,b-1)

# FACTORIAL 
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
# TOWERS OF HANOI (THINK RECURSIVELY! )
# SOLVE A SMALLER PROBELM/ SOLVE A BASIC PROBLEM
# fr: from stack (INITAL TOWER); to: to stack (FINAL TOWER); spare: (SPARE TOWER);  
def printMove(fr,to):
    print('move from'+str(fr)+'to'+str(to))

def Towers(n,fr,to,spare):
    if n==1: 
        printMove(fr,to)
    else:
        # WE CAN HAVE MULTIPLE RECURSIVE CALLS INSIDE A FUNCTION
        # THINK IT RECURSIVELY
        Towers(n-1,fr,spare,to) # move the stack size of n-1 to a spare disc
        Towers(1,fr,to,spare) # move the bottom to the direed disc
        Towers(n-1,spare,to,fr) # move the n-1 back to the deisred disc 

print(Towers(2,'P1','P2','P3'))


# RECURSION WITH MULTIPLE BASE CASES
# FIBONACCI NUMBERS
def fib(x):
    """assumes x an int >=0, returns Fibonacci of x """
    if x == 0 or x ==1: # base cases
        return 1
    else: 
        return fib(x-1)+ fib(x-2) # we have two recurisve functions calls in a return

# RECURSION ON NON-NUMERICS (STRINGS)
def isPalindrome(s):
    def toChars(s): # convert string to all lower cases
        s = s.lower() # convert to lower case
        ans = ''
        for c in s: # remove all the punctuations/space
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
        
    def isPal(s):
        if len(s)<= 1: # recursive base case
            return True
        else: 
            return s[0] == s[-1] and isPal(s[1:-1]) # recursive step happens here
                                                    # we compare the fisrt and last letter then
                                                    # we convert the problem to a smaller probelm
    
    return isPal(toChars(s))
    

"""
DIVIDE AND CONQUER
WE SOLVE A HARD PROBLEM BY BREAKING IT INTO A SET OF SUBPROBLEMS SUCH THAT:
SUB-PROBLEMS ARE EASIER TO SOLVE THAN THE ORIGINAL
SOLUTIONS OF THE SUB-PROBELMS CAN BE COMBINED TO SOLVE THE ORIGINAL
"""
    
    
"""
MODULES
A MODULE IS A .py FILE CONTAINING A COLLECTION PYTHON DEFINITINS AND STATEMENTS
"""    
# the file circle.py contains 
pi = 3.14159
def area(radius):
    return pi*(radius**2)
def circumference(radius):
    return 2*pi*radius
    
# then we can import and use this module
import circle
pi = 3   # can still define the pi in the shell
print(pi) # 3
print(circle.pi) # 3.14159, look for pi defined in the module
print(circle.circumference(3)) # 18.84953999  
    
# if we don't want to refer to functions and vars by their module, and the names don't
# collide with other bindings, then we can use:
from circle import* # means from the module, import everything (denoted by the star sign)
print(pi)
print(area(3)) # we can refer them by calling their own name
    
    
"""
WRITE/READ FILES
"""
nameHandle = open('kids','w') # 'kid': name of file; w: write command
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name+ '\n')
nameHandle.close()    
    
nameHandle = open('kids','r') # read
for line in nameHandle:
    print(line)
nameHandle.close()    
    
    
    




