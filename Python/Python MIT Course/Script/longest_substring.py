# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:51:42 2018

 Prints the longest substring of s in which the letters occur in alphabetical order. 
 For example, if s = 'azcbobobegghakl', then your program should print  beggh.

"""
s = 'azcbobobegghakl'

longest_global = ""
length = len(s)
index = 0

for letter in s:
    longest_local = letter
    count = 0
    while index + count <= (length-2):
        if s[index+count]<= s[index+count+1]:
            longest_local += s[index+count+1]
            count += 1
        else:
            break
    if len(longest_local)> len(longest_global):
        longest_global = longest_local
        
    print(longest_global)
    index += 1
    
print('Longest substring in alphabetical order is: '+ longest_global)

