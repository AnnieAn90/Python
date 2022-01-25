# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:17:26 2021

@author: User
"""

from casadi import *
import time
import numpy


# Symbols/expressions
x = MX.sym('x')
y = MX.sym('y')
z = MX.sym('z')

# formulate cost function
f = (x + 2*y-3)**2 + (3*y-8*x+2*z-2)**2 + (y+z-3)**2
# g = x+y-10
g = vertcat(3-x-2*y-z,2-2*x-z,-2+x-2*y+z)

qp = {}                 # NLP declaration
qp['x']= vertcat(x,y,z) # decision vars
qp['f'] = f             # objective
qp['g'] = g             # constraints

# Create solver instance
F = qpsol('F','qpoases',qp);

start_time = time.time() # start time
# lbg = lower bound of g; ubg = upper bound of g; lbx; ubx are defined in a similar way
# Solve the problem using a guess
r = F(lbg=0)

print("--- %s seconds ---" % (time.time() - start_time)) # print out the exectuion time


x_opt = r['x']
f_opt = r['f']

print('x_opt: ', x_opt)
print('f_opt: ', f_opt)