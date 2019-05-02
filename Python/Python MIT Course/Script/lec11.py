# -*- coding: utf-8 -*-
"""
UNDERSTANDING PROGRAM EFFICIENCY
"""

"""
TRADEOFF BETWEEN TIME AND EFFICIENCY-FOCUS ON TIME EFFICIENCY
"""
# HWO TO EVALUATE EFFICIENCY OF PROGRAMS
# timer/count/order of growth(most appropriate way)

# TIMING A PROGRAM
# NOT SO GOOD - VARY DEPENDING ON COMPUTES/ALOGORITHM/IMPLEMENTATIONS
import time # bring that class into your own file

def c_to_f(c):
    return c*9/5 + 32

t0 = time.clock()
c_to_f(100000)
t1 = time.clock()-t0
print("t =",t0,":",t1,"s,")

# COUNTING OPERATIONS
def c_to_f(c):
    return c*9.0/5+32 # 3 ops

# total op = 1+(1+2)n， n-> iterations
def mysum(x):
    total = 0 # 1 op
    for i in range(x+1): # 1 op/ ite
        total += i # 2 ops /ite
    return total

# ORDER OF GROWTH
# want to evaluate program's efficiency when input is very big
# express the growth of program's run time as input size grows
# upper bound on growth/ don't have to be precise
# tyoes of orders of growth: constant/linear/quadratic/logrithmic/nlogn/expoential

# O() is used to describe worst case - > whats is the behavior when as the problem input size
# get really big
    
def fact_iter(n):
    """ assumes a an int >= 0, computes factorial """
    answer = 1
    while n>1:
        answer *= n
        n -= 1 # two steps
    return answer

# in toal 1+ 5n + 1 operations
# worst case asymptotic complecity: O(n)
    # ignore additive constants
    # ignore multiplicative constants
# n^2 +2n + 2 -> O(n^2)

for i in range(n):
    print('a')  # O(n)
    
for j in range(n*n):
    print('b')  # O(n*n)
    
# O(n) + O(n*n) = O(n+n^2) = O(n^2)
# O(f(n))*O(g(n)) = O(f(n)*g(n))

"""
COMPLEXITY CLASSES
"""
    
    
    
    
    
    
    