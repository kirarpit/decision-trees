#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 21:23:37 2018

@author: Arpit
"""
from node import Node
from criterion import Criterion
import logger as lg

"""
builds the decision tree
"""
def get_decision_tree(data):
    lg.main.debug("Get decision tree called!")
    
    node = Node(data)
    if not data.getImpurity():  #returns the node if there is only 1 class left in the set
        lg.main.debug("Data is pure!")
        return node
    
    criterion = Criterion(data) #creates a criterion object which finds the best feature to split on
    datasets = criterion.split()
    if not datasets:
        return node
    
    node.setFeature(criterion.bestFeature)  #node stores the feature the data is split on for quering later on
    for key, data in datasets:
        lg.main.debug("Adding a child")
        node.addChild(key, get_decision_tree(data))
    
    return node