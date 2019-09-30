#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: dordoloy
"""

import pytest
import cv2
import numpy as np
import S1_algotools as s1

def inc_(x):
    return x+1

def test_inc():
    assert inc_(3)==4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
        
"""
   UnitTest average_above_zero 
"""
def test_average_above_zero():
    assert s1.average_above_zero(s1.tab_list) == 3

def test_average_above_zero_not_a_list():
    with pytest.raises(TypeError):
        s1.average_above_zero(3)
        
def test_average_above_zero_empty_list():
    with pytest.raises(ValueError):
        s1.average_above_zero([])
    
def test_average_above_zero_not_a_number_list():
    with pytest.raises(ValueError):
        s1.average_above_zero(['3',''])
        
def test_average_above_zero_division():
    tab_list=[-1,-2,-3,-6]  
    with pytest.raises(ZeroDivisionError):
        s1.average_above_zero(tab_list)

"""
    UnitTest max_value
"""
def test_max_value():
    tab_list=[1,2,3,-4,6,-9]  
    assert s1.max_value(tab_list) == (6,4)

def test_max_value_not_a_list():
    with pytest.raises(TypeError):
        s1.max_value(3)
        
def test_max_value_empty_list():
    with pytest.raises(ValueError):
        s1.max_value([])
    
def test_max_value_a_number_list():
    with pytest.raises(ValueError):
        s1.max_value(['3',''])



"""
    UnitTest reverse_table
"""
def test_reverse_table():
    tab_list=[1,2,3,-4,6,-9]  
    assert s1.reverse_table(tab_list) == [-9,6,-4,3,2,1]

def test_reverse_table_not_a_list():
    with pytest.raises(TypeError):
        s1.reverse_table(3)
        
def test_reverse_table_empty_list():
    with pytest.raises(ValueError):
        s1.reverse_table([])


"""
    UnitTest roi_bbox
"""
def test_roi_bbox():
    img = cv2.imread("img.png",0)
    assert(s1.roi_bbox(img) == np.array([[124,236],[124,732],[424,236],[424,732]])).prod()

def test_roi_bbox_not_an_array():
    with pytest.raises(TypeError):
        s1.roi_bbox(3)
        
def test_roi_bbox_empty_array():
    with pytest.raises(ValueError):
        s1.roi_bbox(np.array([]))

"""
    UnitTest random_fill_sparse
"""
def test_random_fill_sparse():
    a = np.ones((10,10),dtype=np.chararray)
    a *= '-' 
    result = s1.random_fill_sparse(a,10)
    assert len(np.argwhere(result == 'X')) == 10

def test_random_fill_sparse_not_an_array():
    with pytest.raises(TypeError):
        s1.random_fill_sparse(3,10)
        
def test_random_fill_sparse_empty_array():
    with pytest.raises(ValueError):
        s1.random_fill_sparse(np.array([]),10)


