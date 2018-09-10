#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:48:45 2018

@author: Arpit
"""

from data import Data
from utils import pre_process_data, load_data, decode, encode_string
from decisionTree import get_decision_tree
import numpy as np

"""
prints the prediction accuracy by quering the decision tree
"""
def check_accuracy(root, data):
    cnt = 0
    for row in data:
        row = list(row)
        target = row.pop()
        if root.predict(row) == target:
            cnt += 1
    print("accuracy ", cnt/data.shape[0])

x = pre_process_data(load_data('training.csv'))

# randomly choose 70% rows for training and rest 30% for validation
t_rows = list(np.random.choice(len(x), int(len(x) * 0.7), replace=False))
v_rows = list(set(list(range(len(x))))^set(t_rows))

# Split training set into training and validation set
x_training = x[np.array(t_rows), :]
x_validation = x[np.array(v_rows), :]

data = Data(x_training)
alphas = [1, 0.05, 0.01, 0.005]    #Build a tree for each alpha
for alpha in alphas:
    root = get_decision_tree(data, alpha)  #Building the decision tree using training set
    check_accuracy(root, x_validation)  #Checking prediction accuracy on validation set
    check_accuracy(root, x_training)    #Checking prediction accuracy on training set
    print()

# Predicting testing set and writing it to a file
f = open('prediction.csv','w')
f.write("id,class\n")
y = load_data('testing.csv')
for row in y:
    idx = row[0]
    seq = encode_string(row[1])
    prediction = decode(root.predict(seq))
    f.write(str(idx) + "," + prediction + "\n")
f.close()

