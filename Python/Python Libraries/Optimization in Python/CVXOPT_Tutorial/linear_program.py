# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:25:35 2021

@author: User
"""
import time
from cvxopt import matrix, solvers

start_time = time.time() # start time

c = matrix([-4., -5.])
G = matrix([[2., 1., -1., 0.], [1., 2., 0., -1.]])
h = matrix([3., 3., 0., 0.])
sol = solvers.lp(c, G, h)


print(sol['x'])
print("--- %s seconds ---" % (time.time() - start_time)) # print out the exectuion time
