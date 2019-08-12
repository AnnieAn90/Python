# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
APPROXIMATE SOLUTIONS - cube root
"""
cube = 29
epsilon = 0.01 
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess**3-cube) >= epsilon and guess <= cube: # WATCH YOUR STEP, YOU MAY OVERSHOOT
    guess += increment
    num_guesses += 1
print("num_guesses = "+ str(num_guesses))

if abs(guess**3-cube) >= epsilon:
    print("Failed on cube root of" + str(cube))
else:
    print(str(guess)+ " is close to the cube root of " + str(cube))


"""
BISECTION SEARCH - SQUARE ROOT
# REALLY RADICALLY REDUCES COMPUTATION TIME
"""
x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2-x) >= epsilon:
    print('low = '+str(low)+' high = '+str(high)+' ans = '+ str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    
print('numGuesses = '+ str(numGuesses)) 
print(str(ans) + ' is close to square root of '+ str(x))

"""
BISECTION SEARCH - CUBE ROOT
# THIS SCRIPT ALSO ADDRESSES THE CASES WHERE X IN (-1,1) AND X < 0
"""
x = -8
epsilon = 0.01
numGuesses = 0
low = 1.0
high = abs(x)

if abs(x) <= 1:
    low = 0
    high = 1

ans = (high + low)/2.0 # BISECTION METHOD

while abs(ans**3-abs(x)) >= epsilon:
    print('low = '+str(low)+' high = '+str(high)+' ans = '+ str(ans))
    numGuesses += 1
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    
if x < 0:
    ans = -ans

print('numGuesses = '+ str(numGuesses)) 
print(str(ans) + ' is close to cubic root of '+ str(x))


"""
FLOATS AND FRACTIONS (BINARY REPRESENTATION)
INTERNALLY, COMPUTER REPRESENTS NUMBERS IN BINARY
DECIMAL NUMBER: 302 = 3*100 + 0*10 + 2*1

"""
#THE FOLLOWING PROGRAM CONVERTS INTERGERS TO BINARY FORMS
num = -10
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result 
    num = num//2
if isNeg:
    result = '-'+ result
print(result)


# WHAT ABOUT FRACTIONS ?
# IF WE MULTIPLE BY A POWER OF 2 (e.g 2^3) WHICH IS BIG ENOUGH TO CONVERT INTO 
# A WHOLE NUMBER, CAN THEN CONVERT TO BINARY, AND THEN DIVIDE BY THE SAME POWER OF 2
# e.g. 3/8 = 0.375 = 3*10^-1 + 7*10^-2 + 5*10^-3
# 0.375*(2**3) = 3 (DECIMAL), THEN CONVERT TO BINARY (NOW 11)
# THEN DIVIDE BY 2**3(SHIFT RIGHT) TO GET 0.011 (BINARY)

x = float(input('Enter a decimal number between 0 and 1:'))
p = 0
while ((2**p)*x)%1 != 0: # CONVERT TO A WHOLE NUMBER
    print('Remainder = '+str((2**p)*x-int((2**p)*x)))
    p += 1
    
num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0: # CONVERT TO BINARY
    result = str(num%2) + result
    num = num//2
    
for i in range(p-len(result)):
    result = '0' + result

result = result[0:-p]+'.'+result[-p:]
print('The binary representation of the decimal '+str(x)+' is'+str(result))
    
# THERE ARE SOME PORBLEMS WITH COMPRAING TWO FLOAT POINTS BECAUSE COMPUTER TRIES TO SEE 
# IF THE BINARIES ARE SAME. WE ALWAYS USE abs(x-y)< some small number, rather than x == y


"""
NEWTON-RAPHSON (FOR ROOT FINDING OF ANY 1-VARIABLE POLYNOMIALS)
GENERAL APPROXIMATION ALGORITHM TO FIND ROOTS OF A POLYNOMIAL IN ONE VARIABLE
P(X)=a_n x^n + a_n-1 x^n-1 + ... + a_1 x + a_0 = 0
"""
# WE USE THIS METHOD TO SOLVE p(x) = x^2 -24 = 0, WHREE x IS THE SQUARE ROOT OF 24
epsilon  = 0.01 
y = 24.0 
guess = y/2.0
numGuesses = 0
  
while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2)-y)/(2*guess))
print('numGuesses = '+str(numGuesses))
print('Square root of '+str(y)+' is about '+ str(guess))


 

















