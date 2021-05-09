# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:17:26 2021

@author: User
"""

from casadi import *
import time


# Symbols/expressions
x = MX.sym('x')
y = MX.sym('y')
f = x**2+y**2
# g = x+y-10
g = vertcat(x+y-10, 4-x)

qp = {}                 # NLP declaration
qp['x']= vertcat(x,y) # decision vars
qp['f'] = f             # objective
qp['g'] = g             # constraints

# Create solver instance
F = qpsol('F','qpoases',qp);

start_time = time.time() # start time
# Solve the problem using a guess
r = F(lbg=0)

print("--- %s seconds ---" % (time.time() - start_time)) # print out the exectuion time


x_opt = r['x']

print('x_opt: ', x_opt)