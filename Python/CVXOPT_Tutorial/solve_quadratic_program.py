# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:02:21 2021

@author: User
"""
import time
from cvxopt import matrix, solvers

start_time = time.time() # start time

Q = 2*matrix([ [2, .5], [.5, 1] ])
p = matrix([1.0, 1.0])
G = matrix([[-1.0,0.0],[0.0,-1.0]])
h = matrix([0.0,0.0])
A = matrix([1.0, 1.0], (1,2))
b = matrix(1.0)

sol=solvers.qp(Q, p, G, h, A, b)

print(sol['x'])
print("--- %s seconds ---" % (time.time() - start_time)) # print out the exectuion time