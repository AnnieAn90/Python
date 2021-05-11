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
f = 2*x**2+y**2+x*y+x+y
# g = x+y-10
g = vertcat(x+y-1, 1-x-y,0.7-2*x,0.7-0.3*y)

qp = {}                 # NLP declaration
qp['x']= vertcat(x,y) # decision vars
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