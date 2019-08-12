# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:16:36 2018
OBEJCT-ORIENTED PROGRAMMING
@author: Zipeng
"""

"""
CREATE A SIMPLE CLASS
"""
class Employee: # Employee class
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
    
emp_1 = Employee('Corey','Schafer',5000) # employee 1, instance, e.g. emp_1 passes to self
emp_2 = Employee('Test','User',6000) # employee 2

# Here two lines do the exact same things, but just different call method
emp_1.fullname()
Employee.fullname(emp_1) # emp_1 is self

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname()) # fullname() means method instead of attribute




"""
CLASS VARIABLES
"""
# Class variables： are variables are shared (same) among all instances in a class
#　Instance variables: can be unique for each instance
class Employee: # Employee class
    # class variable
    num_of_emps = 0
    raise_amount = 1.04
    # method 
    def __init__(self,first,last,pay): # self by convention
            # attributes, instance variable
            self.first = first 
            self.last = last
            self.pay = pay
            self.email = first + '.'+last+'@company.com'
            Employee.num_of_emps += 1 # update number of employees
    # new method
    def fullname(self): # self arugment is required
        return '{} {}'.format(self.first,self.last)  # basic formatting
    
    def apply_raise(self):# we can access this class var from class itself or both instances
        self.pay = int(self.pay*self.raise_amount) # here we can use self.raise_amount
        
    
emp_1 = Employee('Corey','Schafer',5000) # employee 1, instance, e.g. emp_1 passes to self
emp_2 = Employee('Test','User',6000) # employee    

emp_1.raise_amount = 1.05 # create a instance attribute for emp_1

#print(emp_1.__dict__) # return the name space of emp_1
#print(Employee.__dict__)
print(emp_1.pay) 
print(emp_2.pay) 
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay) # 1.05 raise, only for emp 1
print(emp_2.pay) # 1.04 raise
print(Employee.raise_amount)  
# 2 employees
print(Employee.num_of_emps)
    

"""
CLASS METHODS AND STATIC METHODS
Regualr methods: automatically take the instance (self) as their 1st argument 
Class methods: pass the class (cls) as their first argument 
Static methods: don't pass anything automatically, just like regular functions
"""       
class Employee: # Employee class
    # class variable
    num_of_emps = 0
    raise_amt = 1.04
    # method 
    def __init__(self,first,last,pay): # self by convention
            # attributes, instance variable
            self.first = first 
            self.last = last
            self.pay = pay
            self.email = first + '.'+last+'@company.com'
            Employee.num_of_emps += 1 # update number of employees
    # new method
    def fullname(self): # self arugment is required
        return '{} {}'.format(self.first,self.last)  # basic formatting
    
    def apply_raise(self):# we can access this class var from class itself or both instances
        self.pay = int(self.pay*self.raise_amount) # here we can use self.raise_amount
    
    @classmethod # now we can receive a class as our argument, intead of a instance
    def set_raise_amt(cls,amount): # by convention we use cls for class var name
        cls.raise_amt = amount
        
    @classmethod # alternative constructor, also takes string input
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-') # split a string
        return cls(first,last,pay) # return the parsed object, a new way of creating obejcts
    
    @staticmethod # static method if you dont access instance/class anywhere within this function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # 5 = sat, 6 = sun, from 0
            return False
        return True
        
       
emp_1 = Employee('Corey','Schafer',5000) # employee 1, instance, e.g. emp_1 passes to self
emp_2 = Employee('Test','User',6000) # employee

# class method
Employee.set_raise_amt(1.05) # automatically pass the class Employee, we just need pass amount

print(Employee.raise_amt) 
print(emp_1.raise_amt) 
print(emp_2.raise_amt)     
    
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))

    
    
    