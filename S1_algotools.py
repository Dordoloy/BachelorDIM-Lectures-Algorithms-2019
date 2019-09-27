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


def average_above_zero(table):
    ##
    #Function that compute the average of positive values
    #Args:
    #    @param: the table
    #Returns: the average
    #Raises ValueError if input param is not a list
    if not(isinstance(table,list)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(table)==0:
        raise ValueError('expected a non empty list as input')
    if not(isinstance(table[0],(int, float))):
        raise ValueError('average_above_zero, expected a list of numbers')
        
    som = 0
    n = 0
    for i in range(len(table)):
        if table[i] > 0:
            #print('tab[{index}={val}]'.format(index = i, val=table[i]))
            som  = som + table[i]
            n =  n + 1
    if n==0:
        raise ValueError('Can\'t divide by zero')
    moy =  som/n
    return moy

def max_value(table):
    ##
    #Function that return the max value of te table and his index
    #Args:
    #   @param table: the table
    #Returns: max and index
    #Raises ValueError if input param is not a list
    if not(isinstance(table,list)):
        raise ValueError('max_value, expected a list as input')
    if len(table)==0:
        raise ValueError('expected a non empty list as input')
    if not(isinstance(table[0],(int, float))):
        raise ValueError('max_value, expected a list of numbers')
        
    max = 0
    index = 0
    for i in range(len(table)):
        if table[i] > max:
            max = table[i]
            index = i
    return max, index

def reverse_table(table):
    ##
    #Function that reverse the table
    #Args:
    #   @params table: the table
    #Returns: the reverse table
    #Raises ValueError if input param is not a list
    if not(isinstance(table,list)):
        raise ValueError('reverse_table, expected a list as input')
    if len(table)==0:
        raise ValueError('expected a non empty list as input')
    if not(isinstance(table[0],(int, float))):
        raise ValueError('reverse_table, expected a list of numbers')
        
    len_table = len(table)
    for i in range(len_table):
        lastValue = table[len_table-1]
        table.pop()#Delete the last value of the table
        table.insert(i, lastValue)
    return table

#in progress     
def roi_bbox(input_image):
    box = np.array([])
    for i in range(len(input_image)):
        for j in range(len(input_image)):
            lim = input_image[i][j]
            print(lim)
    return lim
    

#test section
tab_list=[1,2,3,-4,6,-9]
img=[]
#tab_zeros = np.zeros(12)
tab_from_list = np.array(tab_list)
print('Average above 0 = {0}'.format(average_above_zero(tab_list)))
print('Max value = {0}'.format(max_value(tab_list)[0]))
print('Index of max value = {0}'.format(max_value(tab_list)[1]))
print('reverse table = {0}'.format(reverse_table(tab_list)))



