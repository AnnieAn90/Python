# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:13:37 2021

@author: User
"""

from casadi import *
import time


# Symbols/expressions
x = MX.sym('x')
y = MX.sym('y')
z = MX.sym('z')
f = x**2+100*z**2
g = z+(1-x)**2-y

nlp = {}                 # NLP declaration
nlp['x']= vertcat(x,y,z) # decision vars
nlp['f'] = f             # objective
nlp['g'] = g             # constraints

# Create solver instance
F = nlpsol('F','ipopt',nlp);

start_time = time.time() # start time
# Solve the problem using a guess
r = F(x0=[2.5,3.0,0.75],ubg=0,lbg=0)
print("--- %s seconds ---" % (time.time() - start_time)) # print out the exectuion time


x_opt = r['x']

print('x_opt: ', x_opt)