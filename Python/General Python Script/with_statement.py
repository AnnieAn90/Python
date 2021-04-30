# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:30:24 2021

@author: User
"""

#In python if you want to operate some file then you have to use some specific function for that after using that we can read or manipulates the data of the file.
# And for operating the file we use open() function. open returns the file object, from which we can access functions and attributes for performing file operation by opening the file.

#In the normal file operation we have to follow some rules, like opening the file using 'open()' method then read the file data using 'read()' method after that print the data of file and when all operation gets over we need to close the file using 'close()' method.
# Example:

file = open('abc.txt')
data = file.read()
print data
file.close() #file closing is must or it will throw error

#Using with statement we can get automatic exception handelling and better syntax.
#at the end there is no need of write closing of file it automatically get space cleared by with statement.
#Example:

with open('abc.txt') as file: # refer file as object for file object
data = file.read()
print data
