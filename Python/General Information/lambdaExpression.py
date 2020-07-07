# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:49:10 2020

@author: User

lambda expressions = anonymous functions = functions with no names

lambda is just a fancy way of saying function. Other than its name, 
there is nothing obscure, intimidating or cryptic about it. 
When you read the following line, replace lambda by function in your mind:

"""

# normal function
def f(x):
   return 3*x+1

print(f(1))

# lambda expression, a function has no name
lambda x: 3*x+1
# one way to use it is to give it a name
g = lambda x: 3*x+1
print(g(2))

# lambda expression with more than one inputs
# strip() removes empty space, title() capitalize the 1st letter in each word
full_name = lambda fn,ln: fn.strip().title()+ " " + ln.strip().title()
print(full_name(" leonhard","EULER"))

# general way of creating lambda expression
# lambda (no inputs): "What is my purpose?"
# lambda x (one input): 3*x+1

# A function with no name
scifi_authors = ["Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C.Clark","Frank Herbert"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower()) # use a anonymous function that extract the last name and use them to sort the names
print(scifi_authors)


# A function makes functions
def build_quadratic_function(a,b,c):
    return lambda x: a*x**2+b*x+c # return a quadratic function with input x

f = build_quadratic_function(2,3,-5) 
print(f(0)) # return -5
print(build_quadratic_function(3,0,1)(2)) # 3x^2+1 evaluated for x


# Python supports a style of programming called functional programming
# where you can pass functions to other functions to do stuff
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # we pass lambda function to filter function to filter the list
