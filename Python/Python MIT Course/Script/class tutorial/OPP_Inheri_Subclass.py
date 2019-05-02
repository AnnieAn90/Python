# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:52:18 2018

@author: Zipeng
"""

"""
INHERITANCE-CREATING SUBCLASSES
ALLOWS US TO INHERIT ATTRIVUTES AND METHODS FROM A PARENT CLASS
"""
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
     
# Develop Subclass
class Developer(Employee): # Inherited from employee class, all the attributes/methods
    raise_amount = 1.10 # we can make changes to our subclasses without breaking anything 
                        # from the main class, here developers requrie more raise than other
                        # employees
    def __init__(self,first,last,pay,prog_lang): # develop has prog_lang attributes
        super().__init__(first,last,pay) # let the super class handle first,last,pay attributes
        self.prog_lang = prog_lang

# Manager Subclass
class Manager(Employee): # Inherited from employee class
    def __init__(self,first,last,pay,employees=None): # employees default is None
        super().__init__(first,last,pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self,emp): # add 
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp): # remove
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self): # print out all the employees from that list (currently supervise)
        for emp in self.employees:
            print('-->',emp.fullname())

dev_1 = Developer('Corey','Schafer',5000,'Python') # employee 1, instance, e.g. emp_1 passes to self
dev_2 = Developer('Test','User',6000,'Java') # employee   

#print(help(Developer)) # for visulization

mar_1 = Manager('Sue','Smith',90000,[dev_1])

print(mar_1.email)

mar_1.add_emp(dev_2)
mar_1.remove_emp(dev_1)
mar_1.print_emps() 

# PYTHON HAS TWO BUILT-IN FUNCTIONS THAT TELL IF A SUBSEJCT IS INSTANCE OR SUBCLASS
print(isinstance(mar_1,Manager)) # check if mar_1 is an instance of  Manager
print(issubclass(Developer,Employee)) # in the manner of is subclass