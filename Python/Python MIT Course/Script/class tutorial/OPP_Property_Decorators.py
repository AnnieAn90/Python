# -*- coding: utf-8 -*-
"""
PROPERTY DECORATOR- GETTERS/SETTERS/DELETERS
"""
class Employee: # Employee class
    # class variable
    raise_amount = 1.04
    # method 
    def __init__(self,first,last): # self by convention
            # attributes, instance variable
            self.first = first 
            self.last = last
            
    @property # we define email in our class like a method, but we can access it like an attribute
    def email(self): # self arugment is required
        return '{}.{}@email.com'.format(self.first,self.last)  # basic formatting
    
    # new method
    @property
    def fullname(self): # self arugment is required
        return '{} {}'.format(self.first,self.last)  # basic formatting
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
        
emp_1 = Employee('John','Smith')


emp_1.fullname = 'Corey Schafer' # set the full name of an employee

print(emp_1.first)
print(emp_1.email) # access it like an attribute
print(emp_1.fullname)

del(emp_1.fullname) # delete the full name of an employee