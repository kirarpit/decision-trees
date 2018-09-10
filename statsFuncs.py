#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 21:22:05 2018

@author: Arpit
"""
import math
import numpy as np
from utils import load_data

def get_classification_error():
    pass

def get_entropy(data):
    total = sum(data.values())

    result = 0
    for value in list(data.values()):
        if value:
            result -= (value/total) * math.log(value/total, 2)
        
    return result

def get_gini_index(data):
    total = sum(data.values())
    
    result = 1
    for value in list(data.values()):
        result -= math.pow(value/total, 2)
    
    return result

def get_impurity(data, method='GI'):    
    if method == "GI":
        impurity = get_gini_index(data)
    elif method == "CE":
        impurity = get_classification_error(data)
    else:
        impurity = get_entropy(data)
        
    return impurity

"""
looks up in chisquare table according to given dof and alpha
"""
def chi_square_lookup(dof, alpha=0.01):
    table = load_data("chiSquare.csv")
    return table[dof][np.where(table[0]==alpha)[0][0]]

"""
returns False if expected gain in information is not met
"""
def get_chi_square(dist1, dists, alpha):
    if alpha == 1: return True
    
    X2 = 0
    for dist in dists:
        for key, value in dist1.items():
            real = 0 if key not in dist else dist[key]
            expected = sum(dist.values())*value/sum(dist1.values())
            
            X2 += math.pow(real - expected, 2)/expected
    
    dof = (len(dist1) - 1)*(len(dists) - 1) #gets dof according to current parent data and not according to root node data
    return X2 >= chi_square_lookup(dof, alpha)
    