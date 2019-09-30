#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: dordoloy
"""

import pytest
import S1_algotools as s1

def inc_(x):
    return x+1

def test_inc():
    assert inc_(3)==4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
        
"""
   Unit Test avege above zero
"""

def test_average_above_zero():
    assert s1.average_above_zero(s1.tab_list) == 3

def test_average_above_zero_not_a_list():
    with pytest.raises(ValueError):
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