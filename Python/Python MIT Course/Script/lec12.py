# -*- coding: utf-8 -*-
"""
SEARCHING AND SORTING ALGORITHMS
"""

"""
USE BISECTION SEARCH
"""
# a breaking and conqure problem
# IMPLEMENTATION 1 (O(n))
def bisect_search1(L,e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half]>e:
            return bisect_search1(L[:half],e) # copy requries O(n) operations
        else:
            return bisect_search1(L[half:],e)
        
# IMPLEMENTATION 2 (O(log n))
def bisec_search2(L,e):
    def bisect_search_helper(L,e,low,high):
        if high == low:
            return L[low]==e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid-1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
    
# SEARCH A  SORTED LIST -- n is len(L)
# Linear search, O(n)
# binary search, O(log n), but assume the list is sorted
# When does it make sense to sort first then search ? 
        # SORT + O(log n) < O (n) -> SORT < O(n) - O(log n)
        # when sorting is less than O(n) -> never true ! 
        
"""
SORTING (MERGE SORT IS THE BEST SORTING ALGORTIHM)
"""
# MONKEY SORT/BUBBLE SORT/SLECTION SORT
# MERGE SORT -> DIVIDE AND CONQUER -> Split list in half until have sublists of any 1 element

def merge(left,right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    while (i < len(left)): # when right sublist is empty
        result.append(left[i])
        i += 1
        
    while (j < len(right)): # when left sublist is empty
        result.append(right[j])
        j += 1
        
    return result


def merge_sort(L):
    if len(L) < 2: # base case
        return L[:] 
    else:
        middle = len(L)//2 # divide
        left = merge_sort(L[:middle]) 
        right = merge_sort(L[middle:])
        return merge(left,right) # conquer with the merge step
    





























