# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:25:42 2021

@author: User
"""

import numpy as np, matplotlib.pyplot as plt
from scipy.optimize import linprog

# First program: max(x + y) with 2x + y ≤ 4, x + 2y ≤ 3, x ≥ 0, y ≥ 0
# We obtained the value 7/3 at the point (5/3, 2/3)
c1 = [-1, -1]
A1 = [[2,1], [1,2]]
b1 = [4,3]
x0_bnds = (0, None) # This means literally 0 ≤ x0 < ∞
x1_bnds = (0, None) # and this, 0 ≤ x1 < ∞

# Second program: max(2x + y) with −x + y ≤ 1, x − 2y ≤ 2, x ≥ 0, y ≥ 0
# The program is unbounded
c2 = [-2, -1]
A2 = [[-1, 1], [1, -2]]
b2 = [1, 2]

# optimization successful
linprog(c1, A1, b1, bounds=(x0_bnds, x1_bnds), method='simplex')

# optimization failed
linprog(c2, A2, b2, bounds=(x0_bnds, x1_bnds), method='simplex')