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

"""
uses a tree to predict the class of a row
given the selected features the tree was trained on
"""
def predict(root, row, columns):
    newRow = [] #a modified row which contains only the features that this particular tree was trained on
    columns = list(set(columns[:-1]))
    for index in sorted(columns, reverse=False):
        newRow.append(row[index])
    return root.predict(newRow)

#loads and encodes the training set and returns it as a numpy array
x = pre_process_data(load_data('training.csv'))

"""
builds trees with 50% of the rows and features from the
training set chosen randomly without replacement
"""
t_rows = {} #contains the rows selected for ith tree
t_columns = {}  #contains the features selected for ith tree
roots = []  #list of the roots of all the generated trees
for i in range(49):
    t_rows[i] = list(np.random.choice(len(x), int(len(x) * 0.50), replace=False))
    x_training = x[np.array(t_rows[i]), :]
    
    t_columns[i] = list(np.random.choice(len(x[0])-1, int(len(x[0]) * 0.50), replace=False))
    t_columns[i].append(len(x[0])-1)
    t_columns[i].sort()
    x_training = x_training[:, np.array(t_columns[i])]

    root = get_decision_tree(Data(x_training), 0.01)
    roots.append(root)

"""
Calculates the accuracy of the predictions on the training set;
For each row, predictions are made using all the trees
and then choosing the class with max votes.
"""
cnt = 0
for row in x:
    row = list(row)
    target = row.pop()
    
    d = {4:0, 5:0, 6:0}
    for i, root in enumerate(roots):
        d[predict(root, row, t_columns[i])] += 1
        
    if max(d.items(), key=operator.itemgetter(1))[0] == target:
        cnt += 1
print("accuracy ", cnt/x.shape[0])

"""
Calculates the accuracy of the predictions on the training set;
For each row, predictions are made using the trees that did not
use this particular row for training. And then choosing the class
with max votes.
"""
cnt = 0
total = 0
for i, row in enumerate(x):
    row = list(row)
    target = row.pop()
    
    d = {4:0, 5:0, 6:0}
    for key, t_row in t_rows.items():
        if i not in t_row:
            d[predict(roots[key], row, t_columns[key])] += 1
    
    if max(d.values()) != 0:
        total += 1
        if max(d.items(), key=operator.itemgetter(1))[0] == target:
            cnt += 1
print("accuracy ", cnt/total)
    
    
"""
Predictions are made on the testing set using all the trees
"""
f = open('prediction.csv','w')
f.write("id,class\n")
y = load_data('testing.csv')
for row in y:
    idx = row[0]
    seq = encode_string(row[1])
    
    d = {4:0, 5:0, 6:0}
    for i, root in enumerate(roots):
        d[predict(root, seq, t_columns[i])] += 1

    prediction = decode(max(d.items(), key=operator.itemgetter(1))[0])
    f.write(str(idx) + "," + prediction + "\n")
f.close()