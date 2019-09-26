# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:31:07 2019

@author: dordoloy
"""

"""
- What happens if Som initialization is forgotten ?
   the script will work but the result will not be correct

- What can you expect if all the values are below zero ?
    Error -> Impossible to divide by negative value

- Translate this algorithm in the python3.x language within script of name
S1_algotools:py. You must implement this algorithm as a function that
follows prototype "function average_above_zero(table:list) returns float".    

"""


import numpy as np


def average_above_zero(table:list):
    ##
    #Function that return the table average above zero
    #Args:
    #    @param: the table
    #Returns the average
    
    som = 0
    n = 0
    for i in range(len(table)):
        if table[i] > 0:
            #print('tab[{index}={val}]'.format(index = i, val=table[i]))
            som  = som + table[i]
            n =  n + 1
    moy =  som/n
    return moy

def max_value(table:list):
    ##
    #Function that return the max value of te table and his index
    #Args:
    #   @param table: the table
    #Returns max and index
    max = 0
    index = 0
    for i in range(len(table)):
        if table[i] > max:
            max = table[i]
            index = i
    return max, index

#test section
tab_list=[1,2,3,-4,6,-9]
#tab_zeros = np.zeros(12)
tab_from_list = np.array(tab_list)
print('Average above 0 = {0}'.format(average_above_zero(tab_list)))
print('Max value = {0}'.format(max_value(tab_list)[0]))
print('Index of max value = {0}'.format(max_value(tab_list)[1]))



