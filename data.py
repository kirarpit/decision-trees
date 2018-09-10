#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 22:03:37 2018

@author: Arpit
"""
import numpy as np
from statsFuncs import get_impurity
import logger as lg

"""
Data class which wraps around nginx data array
and provides useful functions over raw data
"""
class Data:
    def __init__(self, data):
        lg.main.debug("New data object of shape %s created", data.shape)
        self.data = data
        self.classDist = {}
        self.classify() #get distribution of the classes
        
    def classify(self):
        classes = self.data[:, -1]
        for target in classes:
            if target in self.classDist:
                self.classDist[target] += 1
            else:
                self.classDist[target] = 1

    """
    split data on a particular column
    return the list of smaller datasets with this column feature value as key
    """
    def split(self, idx):
        lg.main.debug("Splitting data of shape %s on index %d", self.data.shape, idx)
        splits = {}
        
        for row in self.data:
            if row[idx] in splits:
                splits[row[idx]] = np.vstack((splits[row[idx]], np.delete(row, idx)))
            else:
                splits[row[idx]] = np.array([np.delete(row, idx)])
        
        return [(key, Data(value)) for key, value in splits.items()]
    
    def getImpurity(self):
        lg.main.debug("Getting impurity for data shape %s and class dist %s", self.data.shape, self.classDist)
        impurity = get_impurity(self.getDist())
        lg.main.debug("Calculated impurity %f", impurity)
        return impurity
        
    def getDist(self):
        return self.classDist
    
    """
    get the number of available features
    """
    def getFeatCnt(self):
        return self.data.shape[1] - 1
    
    def getRowCnt(self):
        return self.data.shape[0]