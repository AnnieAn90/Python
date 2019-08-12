# -*- coding: utf-8 -*-
"""
THIS CODE COMPUTES THE FIXED MONTHLY PAYMENT THAT REQUIRED TO PAYOFF THE BALANCE WITHIN A YEAR
USING BYSECTION SEARCH
"""

# CREATE A FREQ DICTIONARY MAPPING str:int
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics: # iterate over the list
        if word in myDict: # if the word is in the dictionary
            myDict[word] += 1 # increase the value associated with it by 1
        else:
            myDict[word] = 1
    return myDict


# FIND WORD THAT OCCURS THE MOST AND HOW MANY TIMES
# 1. use a lsit, in case there is more than one word
# 2. return a tuple(list,int) for (words_list,highest_freq)
def most_common_words(freqs):
    values = freqs.values() # all ints, note it is a special type not a list
    if values:
         best = max(values)
    else:
        best = 0
    words = []
    for k in freqs: # can iterate over keys in dictionary
        if freqs[k]==best: # is the value is the best
            words.append(k)
    return (words,best)


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
freqs_copy = freqs.copy()

print(words_often(freqs_copy,1))
