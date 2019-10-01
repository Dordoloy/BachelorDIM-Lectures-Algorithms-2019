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
import cv2
import random

def average_above_zero(table):
    ##
    #Function that compute the average of positive values
    #Args:
    #    @param: the table
    #Returns: the average
    #Raises ValueError if input param is not a list
    if not(isinstance(table,list)):
        raise TypeError('average_above_zero, expected a list as input')
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
        raise ZeroDivisionError('Can\'t divide by zero')
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
        raise TypeError('max_value, expected a list as input')
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
        raise TypeError('reverse_table, expected a list as input')
    if len(table)==0:
        raise ValueError('expected a non empty list as input')
        
    len_table = len(table)
    turns = int(len(table)/2)
    for i in range(turns):
        """
        lastValue = table[len_table-1]
        table.pop()#Delete the last value of the table
        table.insert(i, lastValue)
        """
        app_id = len_table-i-1
        tmp=table[i]
        table[i]=table[app_id]
        table[app_id]=tmp

    return table

#in progress     
def roi_bbox(input_image):
    ##
    #Function that return the bounding box of an image
    #Args:
    #    @param input_image: the numpy array 
    #Returns the bbox of numpy array
    #Raises Value error if input param is not a numpy aray and if the array is empty
    if not(isinstance(input_image,np.ndarray)):
        raise TypeError('roi_bbox, expected a numpy array as input')
    if len(input_image) == 0:
        raise ValueError('roi_bbox, expected a non empty array as input')
    min_raw = input_image.shape[1]
    min_col = input_image.shape[0]
    max_raw = 0
    max_col = 0
    for idraw in range(input_image.shape[0]):
        for idcol in range(input_image.shape[1]):
            pix_val=input_image[idraw, idcol]
            if pix_val == 255:
                if idcol > max_col:
                    max_col = idcol
                if idraw > max_raw:
                    max_raw = idraw
                if idcol < min_col:
                    min_col = idcol
                if idraw < min_raw:
                    min_raw = idraw
    return np.array([[min_raw,min_col],[min_raw,max_col],[max_raw,min_col],[max_raw,max_col]])

def random_fill_sparse(table, k):
    ##
    #Function that return the bounding box of an image
    #Args:
    #    @param table: the numpy array
    #    @param k: the number of 'X'
    #Returns the table filled by the 'X'
    #Raises Value error if input param is not a numpy aray and if the array is empty
    
    if not(isinstance(table,np.ndarray)):
        raise TypeError('random_fill_sparse, expected a numpy array as input')
    if len(table) == 0:
        raise ValueError('random_fill_sparse, expected a non empty array as input')
    
    i=0
    while i < k:
            rand1 = random.randint(0,table.shape[0]-1)
            rand2 = random.randint(0,table.shape[1]-1)
            if table[rand1,rand2] != 'X':
                table[rand1,rand2] = 'X'
                i+=1
    return table
    

#test section
tab_list=[1,2,3,-4,6,-9]  
matrix = np.zeros((10,10),dtype=np.int32) 
matrix[3:6, 4:8]=np.ones((3,4),dtype=np.int32)
img = cv2.imread("img.png",0)
a = np.ones((10,10),dtype=np.chararray)
a *= '-'  
#↓cv2.imshow('read image', img)
#cv2.waitKey()
#tab_zeros = np.zeros(12)
#tab_from_list = np.array(tab_list)
print('Average above 0 = {0}'.format(average_above_zero(tab_list)))
print('Max value = {0}'.format(max_value(tab_list)[0]))
print('Index of max value = {0}'.format(max_value(tab_list)[1]))
print('reverse table = {0}'.format(reverse_table(tab_list)))
print('Bounding box = \n {0}'.format(roi_bbox(img)))
print('Random fill sparse = \n {0}'.format(random_fill_sparse(a,10)))


