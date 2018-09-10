#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 00:43:51 2018

@author: Arpit
"""
from data import Data
from utils import pre_process_data, load_data, decode, encode_string
from decisionTree import get_decision_tree
import numpy as np
import operator

x = pre_process_data(load_data('training.csv'))

"""
buils 17 trees with 60% of the training set randomly chosen without replacement
"""
roots = []
for i in range(17):
    t_rows = list(np.random.choice(len(x), int(len(x) * 0.6), replace=False))
    x_training = x[np.array(t_rows), :]
    root = get_decision_tree(Data(x_training), 0.01)
    roots.append(root)

"""
gets prediction of the complete training set from all trees
and choses the class with max votes
"""
cnt = 0
for row in x:
    row = list(row)
    target = row.pop()
    
    d = {4:0, 5:0, 6:0}
    for root in roots:
        d[root.predict(row)] += 1
    if max(d.values()) == 9: print(d)
        
    if max(d.items(), key=operator.itemgetter(1))[0] == target:
        cnt += 1
print("accuracy ", cnt/x.shape[0])

"""
same voting system for predicting the prediction set
"""
f = open('prediction.csv','w')
f.write("id,class\n")
y = load_data('testing.csv')
for row in y:
    idx = row[0]
    seq = encode_string(row[1])
    
    d = {4:0, 5:0, 6:0}
    for root in roots:
        d[root.predict(seq)] += 1

    prediction = decode(max(d.items(), key=operator.itemgetter(1))[0])
    f.write(str(idx) + "," + prediction + "\n")
f.close()

