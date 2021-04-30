# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:28:52 2021

@author: User
"""

import sys
sys.version

class Foo():
    def __init__(self):
        print('__init__ called')
        self.init_var = 0
        
    def __enter__(self):
        print('__enter__ called')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit__ called')
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')
            
    def add_two(self):
        self.init_var += 2
        
        
        
        
#my_object = Foo()
#my_object.init_var
#my_object.add_two()
#my_object.init_var

with my_object as obj:
    print('inside with statement body')