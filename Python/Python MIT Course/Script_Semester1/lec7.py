# -*- coding: utf-8 -*-
"""
TESTING, DEBUGGING
"""

"""
ERROR MESSAGES-EASY
"""
# IndexError, test = [1,2,3] then test[4]
# TypeError, int(test), '3'/4 (mixing data types)
# NameError, referencing a non-existent variable
# SyntaxError, a = len([1,2,3] (forgetting to close parenthesis, quotation, etc)

"""
LOGIC ERRORS-HARD
"""
# think
# draw pictures
# explain the code to someone else /rubber ducky


"""
EXCEPTION AND ASSERTIONS
"""
# get an exception... to what was expected
# what to do with exceptions?
#　DEALING WITH EXCEPTIONS

# try to execute each of the instuctions in turn
try: 
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number"))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
# if a exception is raised, jump to here
except ValueError:  # separate except clauses to deal with a particular type of exception
    print("Could noe convert to a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")

# OTHER EXCEPTIONS
# else: body of this is excuetd when execution of associated try body completes with no exceptions
# finally: body of this is always executed after try, else and except clauses, even if they raised
         # another error or executed a break, continue or return
         # useful for clean-up code that should be run no matter what else happened 
         # e.g. close a file

"""
EXAMPLE EXCEPTION USAGE
"""
# 1st example
# Loop only exits when correct type of input provided
while True:
    try: 
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError: # handles ValueError
        print("Input not an integer; try again")
print("Correct input of an integer!")

# 2nd example
# Contorl input
data = []
file_name = input("Provide a name of a file of data ")

try:
    fh = open(file_name,'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh: # reading a new line
        if new != '\n':
            addIt = new[:-1].split(',') # remove trailing \n
            data.append(addIt)
    fh.close() # close file even if fail

gradesData = []
if data: # as long as a got some data
    for student in data: # loop through the data
        try: 
            name = student[0:-1]
            grades = int(student[-1]) # gives a vlaueError if the last element is not number
            gradesData.append([name,[grades]])
        except ValueError:
            gradesData.append([student[:],[]])
            
"""
EXCEPTION AS CONTROL FLOW
"""
# WE CAN RAISE A N EXCEPTION WHEN UNABLE TO PRODUCE A RESULT CONSISTENT WITH FUNCTIONS'S SPECIFICATION
def get_ratio(L1,L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers 
        Returns: a list containing L1[i]/L2[i]"""
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) # NaN = not a number
        except: # manage flow of program by raising own error
            raise ValueError('get_ratios called with bad arg')
    return ratios

# ANOTHER EXAMPLE
# GET A NEW LIST WITH AVERAGE MARKS
test_grades = [[['peter','parker'],[80.0, 70.0, 85.0]],[['bruce','wayne'],[100.0, 80.0, 74.0]],
               [['captain','america'], [8.0,10.0,96.0]],[['deadpool'],[]]]

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0],elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    try: 
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data') # no return for excetion, it actually assigns []
        return 0.0
        

"""
ASSERTIONS (GOOD WAY OF DOING DEFENSIVE PROGRAM)
"""
# Prevent circumstances from leading to unexpected results
# Ensure that execution halts whenever an expected conditons not met
# typically used to check inputs to fucntions procedures, but can be used anywhere
# can be used to check outputs of a function to avoid propagating bad values
def avg(grades):
    # function ends immediately if assertion not met
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)























