#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 21:10:14 2018

@author: Arpit
"""
import logger as lg
import operator

"""
A node object for the decision tree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.kids = {}
        self.feature = None
        
    def addChild(self, key, node):
        self.kids[key] = node
        
    def setFeature(self, idx):
        self.feature = idx
        
    """
    asks the question this node splits data on
    and then sends the remaining sequence to it's
    appropriate child node
    """
    def predict(self, seq):
        lg.main.debug("Prediction sequence %s", seq)
        
        if not len(self.kids) or seq[self.feature] not in self.kids:
            dist = self.data.getDist()
            return max(dist.items(), key=operator.itemgetter(1))[0] #returns the class with max rows
        
        newSeq = seq[:self.feature] + seq[self.feature + 1:]    #removes the character which is already used to decide next child node
        return self.kids[seq[self.feature]].predict(newSeq)