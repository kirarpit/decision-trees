#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 21:25:01 2018

@author: Arpit
"""
import logger as lg
from statsFuncs import get_chi_square

"""
criterion object which finds the
best feature to split data on
"""
class Criterion:
    def __init__(self, data):
        self.data = data
        self.selectBestCriterion()

    """
    selects the best feature to split on
    """
    def selectBestCriterion(self):
        lg.main.debug("Selecting best criterion for split!")

        maxInfoGain = float("-inf")
        featsCnt = self.data.getFeatCnt()
        
        lg.main.debug("Trying %d features", featsCnt)
        for i in range(featsCnt):
            splits = self.data.split(i) #split data on ith feature
            infoGain = self.getInfoGain(splits)
            lg.main.debug("Info gain %s for feature %d", infoGain, i)
            
            if infoGain > maxInfoGain:
                self.bestSplits = splits
                self.bestFeature = i
                maxInfoGain = infoGain
        
        self.maxIG = maxInfoGain
        lg.main.debug("Best feature for splitting is %d with maxIG %f\n", self.bestFeature, self.maxIG)
        
    def getInfoGain(self, splits):
        lg.main.debug("Getting information gain!")
        result = self.data.getImpurity()
        totalRows = self.data.getRowCnt()
        
        for _, data in splits:
            result -= (data.getRowCnt()/totalRows) * data.getImpurity()

        return result
    
    """
    returns False if splitting needs to be stopped
    """
    def split(self, alpha):
        splitsDataDist = [x.getDist() for _, x in self.bestSplits]
        IG = get_chi_square(self.data.getDist(), splitsDataDist, alpha)    #get chi square to decide if we should split further
        
        if IG and alpha == 1 and self.maxIG == 0: IG = False
        
        if not IG:
            return False
        else:
            return self.bestSplits