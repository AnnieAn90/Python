# -*- coding: utf-8 -*-
"""
Scalar Objects

int 
float
bool
NoneType (Special and has one value, None)

"""

# CAN USE type() TO SEE THE TYPE OF AN OBJECT: e.g. type(5)

# CAN CONVERT OBJECT OF ONE TYPE TO ANOTHER: e.g. float(3), int(3.9)

# PRINTING TO CONSOLE: e.g. print(3+2) (NO OUTPUT BECAUSE NO VALUE RETURNED)

# EXPRESSIONS: <object> <operator> <object>
# +,-,* -> IF BOTH ARE ints, RESULT IS int, IF EITHER OR BOTH ARE FLOATS, RESULT IS FLOAT
#/:  DIVISION (6/3->2.0, ALWAYS FLOAT); //: INT DIVISION (5//2->2); %: REMAINDER (5%2->1); **: POWER (2**2->4)

# PARENTHESES USED TO TELL PYTHON TO DO THSES OPERATIONS FIRST: 3(5+1)->18
# PRECEDENCE WITHOUT PARENTHESES: **>*>/>+,-, EXCUTED LEFT TO RIGHT

# BINDING VARIABLES AND VALUES: e.g pi = 3.14159
# a = a+1 <=> a += 1

# COMPARISON OPERATORS ON int and float： e.g >,>=,<,<=,== (equality test),!=(inequality test)
# PYTHON HANDLES COMPARING NUMBERS OF DIFF TYPES PERFECTLY WELL, YOU CAN COMPARE int WITH float

# LOGIC OPERATORS ON bools; e.g. not,and,or
# IF PYTHON, WE DONOT HAVE TO HAVE A false BLOCK

# CONDITIONALS, INDENTATION MATTERS
x = int(input('Enter an interger'))

if x%2 == 0:
    print('') # BLANK LINE
    print('Even')
else:
    print('')
    print('Odd')
    
print('Done with conditional')

# COMPOUND BOOLEANS
x = 1; y =2; z = 3
if x<y and x<z:
    print('x is least')
elif y<z: # ELSE IF
    print('y is least')
else:
    print('z is least')