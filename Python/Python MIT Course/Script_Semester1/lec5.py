# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 23:40:55 2018

@author: User
"""

"""
TUPLES(元组): AN ORDERED (INDEXING) SEQUENCE OF ELEMENTS, CAN MIX ELEMENT TYPES
IMMUTABLE: CANNOT CHANGE ELEMENT VALUES
THE USAGE OF TUPLES IN SIMILAR WITH CELL ARRAYS IN MATLAB EXCEPT THAT TUPLES ARE IMMUTABLE
"""
te = () # empty tuple
t = (2,"one",3) # () indicates a tuple type
ts = (5,) #When a tuple has only one element, you must specify it　ｗｉｔｈ　ｃｏｍｍａ
len(t) # returns 3
t[0] # evaluates to 2, using [] to index, we cannot change element inside tuple, t[1] = 4 not work
(2,"one",3)+(5,6) # concatenate two tuples, evaluates (2,"one",3,5,6)
t[1:2] # slice tuple, ("one",) also give a comma which tells us it's a tuple
x = (1, 2, (3, 'John', 4), 'Hi') # a tuple inside a tuple
x[2][2] # returns int 4, double index
x[-1][-1] # returns string 'i', tricky one 
# CONVENIENTLY USED TO SWAP VARIABLE VALUES
(x,y) = (y,x)

# USED TO RETURN MORE THAN ONE VALUE FROM A FUNCTION
def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return(q,r)

(quot,rem) = quotient_and_remainder(4,5)

# CAN ITERATE OVER TUPLES
def get_data(aTuple): # aTuple is a tuple of tuples
    nums = ()
    words = ()
    for t in aTuple: # interate over a tuple
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums) # find the min value inside the integer tuples
    max_nums = max(nums)
    unique_words = len(words) # return number of unique tuples
    return (min_nums,max_nums,unique_words)

(small,large,words) = get_data(((1,'mine'),(3,'yours'),(5,'ours'),(7,'mine')))


"""
LISTS(列表): ORDERED SEQUENCE OF INFO, ACCESSIBLE BY INDEX
DENOTED BY SQUARE BRACKETS, []
CONTAINS ELEMENTS: USUALLY HOMOGENEOUS (i.e. ALL INTEGERS), CAN CONTAIN MIXED TYPES
LIST ELEMENTS CAN BE CHANGED: MUTABLE (THE DIFFERENCE BETWEEN TUPLE AND LISTS)
"""
# LIST OPERATIONS
# L[i],L[i:j],L[i,j,k],+,len(),min(),max(),del(L[i]),L.append(),L.extend()
# L.count(),L.index(),L.insert(),L.pop(),L.remove(), L.reverse(),L.sort()

import webbrowser
webbrowser.open('https://docs.python.org/3/tutorial/datastructures.html')
a_list = [] #ｅｍｐｔｙ　ｌｉｓｔ，　ｉｎｄｉｃｅｓ　ｓｔａｒｔ　ａｔ　０
b_list = [2,'a',4,True]
L = [2,1,3]

len(L) # 3
L[0] # 2
L[2]+1 # 4
L[3] # error
i = 2
L[i-1] # 1

# CHANGING ELEMENTS (MUTABLE)
L = [2,1,3]
L[1] = 5 # L is now [2,5,3] 

# ITERATING OVER LIST, LIKE STRINGS, CAN ITERATE OVER LIST ELEMENTS DIRECTLY
# NOTE: INDEX 0 TO len(L)-1, range(n) GOES FROM 0 to n-1
total = 0
for i in L:
    total += i
print(total)

# OPERATION ON LISTS (ADD)
L1 = [2,1,3]
L.append(5) # L is now [2,1,3,5], only works for list
# lists are python objects, everything in python is an object
# objects have data/methods/functions/
# access this info by object_name.do_something()
L2 = [4,5,6]
L3 = L1 + L2 # [2,1,3,4,5,6]  concatenation +
L1.extend([0,6]) # mutated L1 to [2,1,3,0,6]

# OPERATION ON LISTS (REMOVE)
del(L1[3]) # delete element at a specific index
L = [2,1,3,6,3,7,0]
L.remove(2) # remove a specific element,[1,3,6,3,7,0]
L.remove(3) # L = [1,6,3,7,0], if an element appears multiple times, only remove the first instance
del(L[1]) # l = [1,3,7,0]
L.pop() # returns o and  mutates L = [1,3,7]

# CONVERT LISTS to STRINGS AND BACK
s = 'I <3 cs' # string
list(s) # returns ['I','', '<','3','','c','s']
s.split('<') # retruns['I ', '3 cs'], splits on spaces if called without a parameter
L = ['a','b','c'] # list
''.join(L) # returns 'abc'
'_'.join(L) # returns 'a_b_c'

# OTHER LIST OPERATIONS
# MORE 
L = [9,6,0,3]
sorted(L) # returns sorted list, does not mutate
L.sort() # mutates, L = [0,3,6,9]
L.reverse() # mutates L = [9,6,3,0]

# BRINGING TOGETHER LOOPS, FUNCTION, range, and LISTS
# range returns sth that behaves like a tuple! doesn't generate elements at once,
# rather it generates the first element, and provides and iteration method by which subsequent
# elements can be generated
range(5) # equivalent to tuple (0,1,2,3,4)
range(2,6) # equivalent to (2,3,4,5)
range(5,2,-1) # equivalent to (5,4,3)
for var in range (5):
    # expression
for var in (0,1,2,3,4):
    #expression


# ALIASING
warm = ['red','yellow','orange']
hot = warm # warm points to exact address, different name, but points the same thing
hot.append('pink')
hot # returns ['red','yellow','orange','pink']
warm # also returns ['red','yellow','orange','pink']

# if two lists print the same thing, does not mean they are the same structure
cool = ['blue','green','grey']
chill = ['blue','green','grey']

cool == chill # return True, == returns True if the objects refereed to by the varibales are equal
cool is chill # return False, is returns True if two variables point to the same object

print(cool) # ['blue','green','grey']
print(chill) # ['blue','green','grey']
chill[2] = 'blue'
print(cool) # ['blue','green','grey']
print(chill) # ['blue','green','blue']

#CLONG A LIST
cool = ['blue','green','grey']
chill = cool[:] # clone cool to chill
chill.append('black')
print(chill) # ['blue','green','grey','black']
print(cool) # ['blue','green','grey']

# SORTING LISTS
sort() # mutates the list, returns nothing
sorted() # does not mutate list, must assign result to a variable
warm = ['red','yellow','orange']
sortedwarm = warm.sort() # note wortedwarm is none type, since sort does not return anything
print(warm)
print(sortedwarm)

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool) # sorted returns the sorted version, thus should be assigned to a variable
print(cool)
print(sortedcool)


# NESTED LIST, ALIASING EFFECT EXISTS
warm = ['yellow','orange']
hot = ['red']
brightcolors = [warm]

brightcolors.append(hot) # list of list
print(brightcolors) # [['yellow','orange'],['red']]

hot.append('pink')
print(hot) # ['red','pink']
print(brightcolors) # [['yellow','orange'],['red','pink']], also mutates

print(hot+warm)
print(hot)

# MUTATION AND ITERATION
# avoid mutating a list as you are interating over it
# remove duplates from two lists
def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1,L2) # This returns [2,3,4], not [3,4], you cannot iterate the list while mutating it
                   # Python has an internal counter for the list, say you at 1, you removed 1, 
                   # it actually goes directly to the second element in L1 (3), and skips 2.

def remove_dups_new(L1,L2):
    L1_copy = L1[:]  # we use clones
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
            

"""
FUNCTION AS OBJECTS
HANDY TOOL TO HAVE
"""
# functions: have types
# particularly useful to use function as arguments when coupled with lists (higher order programming)
def applyToEach(L,f):
    """assumes L is a list, f a function, 
        mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i]=f(L[i])

 L = [1,-2,3.4]
 applyToEach(L,abs) # L = [1,-2,3.4]
 applyToEach(L,int) # L = [1,2,3]
 
 # LIST OF FUNCTIONS
 def applyFuns(L,x):
     """L is a list of functions, x is argument"""
     for f in L:
         print(f(x))
applyFuns([abs,int],4) # 4 4

# GENERALIZATION OF HOPS, map
for elt in map(abs,[1,-2,3,-4]): # simple form-a unary function and a collection of suitable arguments
    print(elt) # map gives you a struture acts like a list, but in a way that you have to iterate to 
               # get all the vlaues, 1,2,3,4
               
L1 = [1,28,36]
L2 = [2,57,9]
for elt in map(min,L1,L2): # general form- an n-ary function and n collections of arguments
    print(elt) # 1,28, 9














