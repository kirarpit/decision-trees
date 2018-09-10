#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 19:29:34 2018

@author: Arpit
"""

import os
import numpy as np
import pandas as pd

mappings = ['A', 'G', 'T', 'C', 'N', 'EI', 'IE']
ambigs = ['D', 'N', 'S', 'R']
mappings += ambigs

"""
simply loads a csv in a numpy array
"""
def load_data(filename, header=None):
    if os.path.exists(filename):
        data = pd.read_csv(filename, header=header).values
        return data
    else:
        print("Error: File " + filename + " not found!")

    return False

def pre_process_data(data):
    
    data = np.delete(data, 0, 1)    #delete the ID column from original data
    preData = np.empty((0, len(data[0][0]) + 1), dtype=object)  #create empty preprocessed data array
    for idx, row in enumerate(data):
        flag = False
        
        for ambig in ambigs:    #remove rows which contains any ambiguos characters
            if ambig in row[0]:
                flag = True
                break
        if flag: continue
                
        temp = np.append(np.array(list(row[0])), row[1])    #making each character as an element in the array
        preData = np.vstack((preData, temp))

    for idx, key in enumerate(mappings):    #map characters to their index value in mappings(encoding)
        preData[preData == key] = idx
    
    preData = np.array(preData, dtype=int)
    return preData   

def encode_string(string):
    string = list(string)
    string = [encode(x) for x in string]
    return string

def encode(char):
    return mappings.index(char)

def decode(idx):
    return mappings[idx]