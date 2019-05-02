# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:51:42 2018

 Prints the longest substring of s in which the letters occur in alphabetical order. 
 For example, if s = 'azcbobobegghakl', then your program should print  beggh.

"""
low = 0
high = 100
ans = int((low + high)/2.0)

print('Please think of a number between 0 and 100!')
print('Is your secret number '+ str(ans) + '?')
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while guess != 'c':
    if guess == 'h':
        high = ans
    elif guess == 'l':
        low = ans
    else: 
        print('Sorry, I did not understand your input.')
        
    ans = int((low + high)/2.0)
    print('Is your secret number '+str(ans)+' ?')
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print('Game over. Your secret number was: '+str(ans))