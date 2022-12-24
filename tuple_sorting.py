# -*- coding: utf-8 -*-
"""Tuple_Sorting.ipynb


#Python Program for Sorting non-empty tuples

def last(n):
    return n[-1] 

def sort(tuples):
    return sorted(tuples, key=last)
 #Sample 
a=[(5, 7), (1, 1), (3, 5), (8, 4), (2, 3)]
print("Sorted:")
print(sort(a))

