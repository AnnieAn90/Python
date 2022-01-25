# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:17:26 2021

@author: User
"""

from casadi import *
import time

# well low-level implementation seems do not work either !!!!!!!

# Symbols/expressions
H = 2*DM.eye(2)
A = DM.ones(1,2)
g = DM.zeros(2)
lba = 10

qp = {}                 
qp['h']= H.sparsity() 
qp['a'] = A.sparsity()             

# Create solver instance
F = qpsol('F','qpoases',qp);

start_time = time.time() # start time
# Solve the problem using a guess
r = F(h=H,g=g,a=A,lba=lba)

print("--- %s seconds ---" % (time.time() - start_time)) # print out the exectuion time


x_opt = r['x']

print('x_opt: ', x_opt)