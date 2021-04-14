# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:00:41 2021

@author: User

https://sums-of-squares.github.io/sos/
"""

import sympy as sp
import numpy as np
from SumOfSquares import SOSProblem, poly_opt_prob

"""
Example 1: Checking if a polynomial is SOS
"""
# Case 1
# Defines symbolic variables and polynomial
x, y = sp.symbols('x y')
p = 2*x**4 + 2*x**3*y - x**2*y**2 + 5*y**4

# initlaize a SOS problem
prob = SOSProblem()

# Adds Sum-of-Squares constaint and solves problem
const = prob.add_sos_constraint(p, [x, y])
prob.solve()

# Prints Sum-of-Squares decomposition
print(sum(const.get_sos_decomp()))

"""
Example 2: Parametric SOS problems
"""
# Case 1
x, y, s, t = sp.symbols('x y s t') # define varibale
# define polynomial
p = s*x**6 + t*y**6 - x**4*y**2 - x**2*y**4 - x**4 \
    + 3*x**2*y**2 - y**4 - x**2 - y**2 + 1 
# define SOS problem    
prob = SOSProblem() 
# add cibstraints, x, y are indep vars
prob.add_sos_constraint(p, [x, y]) 
# s, t are decision variables whereas x,y are independent vars
sv, tv = prob.sym_to_var(s), prob.sym_to_var(t)
# set objectives 
prob.set_objective('min', sv+tv) 
# solver
prob.solve()
print(sv.value, tv.value)

# Case 2; Muliple SOS constraints
x, y, t = sp.symbols('x y t')

p1 = t*(1 + x*y)**2 - x*y + (1 - y)**2 # poly 1
p2 = (1 - x*y)**2 + x*y + t*(1 + y)**2 # poly 2

prob = SOSProblem()
prob.add_sos_constraint(p1, [x, y])
prob.add_sos_constraint(p2, [x, y])

tv = prob.sym_to_var(t) # convert t to decision variable
# set objective
prob.set_objective('min', tv)
prob.solve()
print(tv.value)

"""
Example 3: Global polynomial optimization
"""
# Case 1
# define var
x, y, t = sp.symbols('x y t')
# define poly
p = x**4 + x**2 - 3*x**2*y**2 + y**6
# define SOS problem
prob = SOSProblem()
# Use Newton polytope reduction
prob.add_sos_constraint(p-t, [x, y], sparse=True)
# set objective with t as our decision variable
prob.set_objective('max', prob.sym_to_var(t))
# solve SOS problem
prob.solve()
print(prob.value)
# Returns the lower bound -.177979

# Case 2
# define vars
x, y, t = sp.symbols('x y t')
# define poly
p = x**4 + x**2 - 3*x**2*y**2 + y**6
# define a ploynomial optimal probelm
prob = poly_opt_prob([x, y], p)
prob.solve()
print(prob.value)
# Returns the lower bound -.177979

"""
Example 4: Constrained polynomial optimization
"""
# Case 1
# define variable
x, y = sp.symbols('x y')
# define poly optimal probelm 
prob = poly_opt_prob([x, y], x - y, eqs=[x**2-x, y**2-y], deg=1)
prob.solve()
print(prob.value)
# returns t = -1

# Case 2
# define var
x, y = sp.symbols('x y')
# define polynomial optimal problem with eqaulity constraints and inequality constraints
prob = poly_opt_prob([x, y], x + y, eqs=[x**2+y**2-1, y-x**2-0.5],
                     ineqs=[x, y-0.5], deg=2)
prob.solve()
print(prob.value)
# returns t ~ 1.3911










