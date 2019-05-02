# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:32:20 2019

@author: Zipeng
"""
#　ｉｍｐｏｒｔ　ｔｈｉｓ　ｌｉｂｒａｒｙ
from scipy.io import loadmat
import numpy as np

# load matlab_data as a dictionary
randomData = loadmat('waypoints.mat')

# the data variabl is saved as 'waypoints' in matlab
# NewData is a numpy.ndarray object, where ndarray means n-dimensional array, and numpy is a python library for 
# scientific computin, e.g. large array,matrices.
goal = randomData['waypoints']

# save the goal data to a txt file
np.savetxt("waypoints.txt",goal)

#　ｃｏｎｖｅｒｔ　ａｒｒａｙ　ｔｏ　ａ　ｎｅｓｔｅｄ　ｌｉｓｔ
goal_list = goal.tolist();

y = np.loadtxt("test.txt")

# we can then access the data as newData_list[1][1]
print(goal_list[0][0])
print(goal_list[0][1])
print(goal_list[0][2])
print(goal_list[0][3])
print(goal_list[0][4])

# print the number stored in a 
print(2*(y[0][4]))