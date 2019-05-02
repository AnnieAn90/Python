# -*- coding: utf-8 -*-
"""
SPECIAL (MAGIC/DUNDER) METHODS
DUNDER = DOUBLE UNDERSCORES
https://docs.python.org/3/reference/datamodel.html#special-method-names
"""
# THESE SPECIAL METHODS ALWAYS COME WITH DOUBLE UNDERSCORES
class Employee: # Employee class
    # class variable
    raise_amount = 1.04
    # method 
    def __init__(self,first,last,pay): # self by convention
            # attributes, instance variable
            self.first = first 
            self.last = last
            self.pay = pay
            self.email = first + '.'+last+'@company.com'
            
    # new method
    def fullname(self): # self arugment is required
        return '{} {}'.format(self.first,self.last)  # basic formatting
    
    def apply_raise(self):# we can access this class var from class itself or both instances
        self.pay = int(self.pay*self.raise_amount) # here we can use self.raise_amount
        
    def __repr__(self): # special methods 1
        return "Emplyee('{}','{}',{})".format(self.first,self.last,self.pay)
    
    def __str__(self): # special methos 2
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self,other): # define how we add two objects together
        return self.pay + other.pay
    
    def __len__(self): # there are many methods we can use
        return len(self.fullname())
    
 
emp_1 = Employee('Corey','Schafer',5000) # employee 1, instance, e.g. emp_1 passes to self
emp_2 = Employee('Test','User',6000) # employee 2


print(repr(emp_1)) # = print(emp_1.__repr__())
print(str(emp_1)) # = print(emp_1.__str__())

# equivalent
print(1+2)
print(int.__add__(1,2))

# also a special dunder method on the background
print(len('test'))
print('test'.__len__())

# Give combined  salary, wiht the defined psecial methods __add__
print(emp_1+emp_2) 
print(len(emp_1))
