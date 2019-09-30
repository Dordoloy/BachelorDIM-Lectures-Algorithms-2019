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
    