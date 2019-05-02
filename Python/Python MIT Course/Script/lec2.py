# -*- coding: utf-8 -*-
"""
STRINGS, BRANCHING, ITERATION
"""


"""
STRINGS
"""

# STRINGS: ENCLOSED IN QUOTATION MARKS OR SINGLE QUOTES (HEREAFTER WE USE DOUBLE QUOTE)
# DOUBLE QUOTE IS HANDY IN INTEPRETING STRINGS CONTAINING APOSTROPHE
hi = " hello there"
greetings = 'hello'

# CONCATENATE STRINGS
name = "eric"
greet = hi + name
greeting = hi + " " + name

# OPERATIONS ON STRINGS
hi = 'ab'+'cd' # CONCATENATION
hi1 = 3*'eric' # SUCCESSIVE CONCATENATION
hi2 = len('eric') # THE LENGTH, ALSO INCLUDES THE SPACE
hi3 = 'eric'[1] # INDEXING, BEGINS WITH INDEX 0, THIS RETURNS r
hi4 = 'eric'[1:3] # SLICING, EXTRACTS SEQUENCE STARTING AT FIRST INDEX AND ENDING BEFORE THE 3 INDEX
                  # 'eric'[1:] (AFTER 1), 'eric'[:3] (BEFORE 3), 'eric'[:] (COPY), 'eric'[-1] (BACKWARDS)


# STRING OPERATION EXAMPLES
str1 = 'hello'
str2 = ','
str3 = 'world'
               
'a' in str3 # bool, False, in/not in ARE TWO BASIC PYTHON MEMBERSHIP OPERATORS
'HELLO' == str1 # bool, False
str4 = str1 + str3 # STRING CONCATENATION
'low' in str4 # bool, True
str3[:-1] # string, worl
str4[1:9:2] # string, elwr, EXTRACT THE LETTERS WITH INDEX 1,3,5,7
str4[::-1] # string, dlrowolleh, (REVERSE ORDER)


#　STRING COMPARISONS　>,<,<=,>=,==,!=
# PYTHON COMPARES STRING LEXICOGRAPHICALLY (USING ASCII VLAUE OF CHARACTERS)
# e.g. Str1 = "Mary", Str2 = "Mac", THE FIRST TWO CHARS ARE M = M, THE SECOND CHARS ARE THEN COMPARED a,a
# ARE STILL EQUAL, THE THIRD TWO CHARS ARE THEN COMPARED r(ASCII 114) > c (ASCII 099)
# A<B<C<...<Z<a<b<c<...<x<y<z

"tim" == "tie" # False
"free" != "freedom" # True
"arrow" > "aron" # True
"right" >= "left" # True
"teeth" < "tee" # False
"yellow" <= "fellow" # False
"abc">"" # True, NOTE THE EMPTY STRING "" IS SMALLER THAN ALL OTHER STRINGS


#STRINGS ARE IMMUTABE
s =  "hello" # s[0] = "y" WILL NOT CHANGE "h" to "y"
s = "y" + s[1:len(s)] # WE CAN STILL CHANGE IT BY DOING THIS
 
"""
INPUT/OUTPUT
"""

# INPUT/OUTPUT: print
x = 1
print(x)
x_str = str(x) # CONVERT X INTO STRING
print("my fav num is", x, ".", "x = ", x) # PRINT IN THIS WAY YOU CANNOT CONTROL THE SPACE
print("my fav num is " + x_str + ". " + "x = " + x_str) # WE SUGGEST TO CONVERT THE EXPRESSION TO 
                                                        # A SINGLE STRING
                                                        
# INPUT/OUTPUT: input("")
text = input ("Type anything ...") # input EXPECTS EVERYTHING TYPED AS A STRING 
print(5*text)
num = int(input("Type a number ...")) # TURN THE INPUT TO A NUMBER BEFORE WE CAN USE IT


"""
ITERATIONS/for/while/break
"""

# CONTRL FLOW while LOOPS , range(start,stop,step)
n = 0
while n<5: # CTRL + c IN THE CONSOLE TO STOP THE PROGRAM
    print(n)
    n = n+1

# CONTROL FLOW for LOOPS
for n in range(5): # SHORTCUT WITH FOR LOOP, RANGE(5) GIVES US 0,1,2,3,4
    print(n)       # range(20) = range(0,20)
    
mysum = 0
for i in range(7,10): # i IS 7,8,9, NOT 10 (RAGNE FOR NUMBERS)
    mysum = mysum + i
print(mysum) # 24

mysum = 0 
for i in range(5,11,2): # 5,7,9, NOT 11 
    mysum = mysum +i
print(mysum) # 21

for letter in 'hola': # h, o ,l, a (for CAN LOOP CHARACTERS IN THE STRING)
    print(letter)

# break STATEMENT
mysum = 0
for i in range(5,11,2):
    mysum = mysum + i
    if mysum == 5:
        break
print(mysum)


# ITERATION
x = 3
ans = 0
itersLeft = x
while(itersLeft != 0):
    ans = ans +x
    itersLeft = itersLeft - 1
print(str(x)+'*'+str(x)+'='+str(ans))


# CLASSES OF ALGORITHMS
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans +1
if ans**3 != abs(x):
    print(str(x)+' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cude root of '+ str(x) + ' is '+ str(ans))
    

# GUESS-AND-CHECK-cube root
cube = 28
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess 
    print('Cube root of ' + str(cube) + ' is ' + str(guess))
    







