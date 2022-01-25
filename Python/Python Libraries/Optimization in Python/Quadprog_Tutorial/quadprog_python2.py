# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:04:33 2021

@author: User
"""
import time
import numpy
import quadprog

def quadprog_solve_qp(P, q, G=None, h=None, A=None, b=None):
    qp_G = .5 * (P + P.T)   # make sure P is symmetric
    qp_a = -q
    if A is not None:
        qp_C = -numpy.vstack([A, G]).T
        qp_b = -numpy.hstack([b, h])
        meq = A.shape[0]
    else:  # no equality constraint
        qp_C = -G.T
        qp_b = -h
        meq = 0
    # quadprog.solve returns a tuple, to access the element inside it we use slice tuple.
    # https://github.com/quadprog/quadprog/blob/master/quadprog/quadprog.pyx （fore more info）
    return quadprog.solve_qp(qp_G, qp_a, qp_C, qp_b, meq)[0:2]


# Generate problem data (need to use float number)
'''
P = numpy.array([[4., 1.], [1., 2.]])
q = numpy.array([1., 1.])
G = numpy.array([[2., 0.], [0., 0.3]])
h = numpy.array([0.7, 0.7])
A = numpy.array([[1., 1.]])
b = numpy.array([1.])
'''

M = numpy.array([[1., 2., 0.], [-8., 3., 2.], [0., 1., 1.]])
P = numpy.dot(M.T, M)
q = -numpy.dot(M.T, numpy.array([3., 2., 3.]))
G = numpy.array([[1., 2., 1.], [2., 0., 1.], [-1., 2., -1.]])
h = numpy.array([3., 2., -2.]).reshape((3,))

# x is the optimizal solution, fval is the final value
try: 
    start_time = time.time() # start time
    x,fval = quadprog_solve_qp(P, q, G, h, None, None)
    print(x)
    print(fval)
    print("--- %s seconds ---" % (time.time() - start_time)) # print out the exectuion time
except:
    print('The QP Problem in infeasible!')
# x = quadprog_solve_qp(P, q, G, h, None, None)

