# -*- coding: utf-8 -*-


"""
FOUR DIFF WAYS TO COLLECT THINGS TOGETHER INTO COMPOUND DATA STRUTURES
strings/tuples/ranges/lists
"""
# COMMON OPERATIONS
seq[i] #  i^th element of sequence
len(seq) # length of sequence
seq1+seq2 # concatenation of sequences (not range)
n*seq # sequence that repeats seq n times (not range)
seq[start:end] # slice of sequence
e in seq # True if e contained in sequence
e not in seq # True if e is not contained in sequence
for e in seq: # iterates over elements of sequence
    
# PROPERTIES
#Type   Type of elements  Example           Mutable
#str    characters        '','a','abc'      No
#tuple  any type          (),(3,),('abc',4) No
#range  integers          range(10)         No
#list   any type         [],[3],['abc',4]   Yes
    
    
"""
DICTIONARIES
"""
# messy if have a lot of diff info to keep track of
def get_grade(student,name_list,grade_list,course_list):
    i = name_list.index(student)
    grade = grade_list[i]
    course = course_list [i]
    return (course,grade)
# A better way and cleaner way - A dictionary
# nice to index (custom index) item of interest directly (not always int)
# key, value
my_dict = {} # cell array in Matlab
grades = {'Ana':'B','John':'A+','Denise':'A','Katy':'A'}
grades['John'] # returns 'A+'    

# DICTIONARY OPERATIONS
grades['Sylvan'] = 'A' # add an entry, only works in dict
'John' in grades # returns True, test to see if a key is in the dictionary
'Daniel' in grades # returns False
del(grades['Ana']) # can remove an entry

grades.keys() # grdaes.key is a method, need type () to call the method, ['John', 'Denise', 'Katy']
grades.values() # ['A+', 'A', 'A']
grades2 = grades.copy() # copy the dictionary
grades.get('Huang',0) # The safe way to get value from key 'Huang', if 'Huang' is 
                     # not a key, then it returns 0

# values in dictionary: can be any type
# keys: must be unique, immutable type (int, float, string,tuple,bool)
d = {1:{1:0},(1,3):"twelve",'const':[3.14,2.7,8.44]}

# list vs dict
# lsit: ordered sequence of elements,look up by an integer index, indices have an order, index is an integer
# dict: matches "keys" to "values", look up one item by another item, no order is guaranteed, key can be any
# immutable type.

"""
EXAMPLE: 3 FUNCTIONS TO ANALYZE SONG LYRICS
"""
# CREATE A FREQ DICTIONARY MAPPING str:int
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics: # iterate over the list
        if word in myDict: # if the word is in the dictionary
            myDict[word] += 1 # increase the value associated with it by 1
        else:
            myDict[word] = 1
    return myDict # returns a dictionary

# FIND WORD THAT OCCURS THE MOST AND HOW MANY TIMES
# 1. use a lsit, in case there is more than one word
# 2. return a tuple(list,int) for (words_list,highest_freq)
def most_common_words(freqs): # freqs is a dictionary
    values = freqs.values() # all ints， note it is a special type not a list
    if vlaues: # find the maxium is values is not empty
        best = max(values)
    else:
         best = 0
    words = []
    for k in freqs: # can iterate over keys in dictionary
        if freqs[k]==best: # is the value is the best
            words.append(k) # append works for list only
    return (words,best) # returns a tuple


# FIND THE WORDS THAT OCCUR AT LEAST X TIMES
# let user choose "at least X times", return a lsit of tuples, each tuple is a (list,int)
# containing the list of words ordered by their frequency
# IDEA: from song dictionary, find most frequent word, delete most common word, repeat. 
def words_often(freqs,minTimes):
    result = []
    done = False # an initial flag
    while not done:
        temp = most_common_words(freqs)
        if temp[1]>= minTimes: # do this untile the most common words appear leass than minTimes
            result.append(temp)
            for w in temp[0]:
                del(freqs[w]) # can directly mutate dictionary; makes it easier to iterate
        else:
            done = True
    return result

lyrics = ['I','love','you','I','love','you','I']
freqs = lyrics_to_frequencies(lyrics)
freqs_copy = freqs.copy() # get a copy of the original dicitonary so that we will not change the original one

print(words_often(freqs_copy,1))


"""
FIBONACCI AND DICTIONARIES (VERY EFFICIENT)
GLOBAL VARIABLES/ TRACKING EFFICIENCY
"""
# ORIGINALLY, WE HAD THIS RESURSIVE FUNCTION
# TWO BASE CASES, CALL ITSELF TWICE, INEFFICIENT
def fib(n):
    global numFibCalls # global variable, we can access outside of the function
    numFibcalls += 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fib(n-1)+fib(n-2)
# INSTEAD OF RECALCULATING THE SAME VALUES MANY TIMES
# WE COULD KEEP TRACK IF ALREADY CALCULATED VALUES (FIBONACCI WITH A DICTIONARY)
# USING A DICTONARY TO HOLD ON THE VALUES I HAVE ALREADY CALCULATED
def fib_efficient(n,d):
    global numFibCalls # accessible from outside scope of function
    numFibcalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans # strore the ans in adcitinary
        return ans
    
numFibCalls = 0
fibArg = 12

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0
d = {1:1,2:2} # base cases in a dictionary, memoization: create a memo for youself
print(fib_efficient(fibArg,d))
print('function calls', numFibCalls)






















