# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 10:05:06 2016

@author: zwmtrue
"""

import random, math

n_trials = 400000
n_hits = 0
var = 0.0
ls_Obs = []
ls_Obs_sq = []
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    Obs_sq = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
        Obs_sq = 16.0
        
    ls_Obs.append(Obs)
    ls_Obs_sq.append(Obs_sq)    
    Obs_mean = sum(ls_Obs)/float(len(ls_Obs))
    Obs_sq_mean = sum(ls_Obs_sq)/float(len(ls_Obs_sq))
 
    var += Obs_sq_mean - (Obs_mean)**2
    
print 4.0 * n_hits / float(n_trials), math.sqrt(var / n_trials)