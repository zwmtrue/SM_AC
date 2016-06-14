# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:08:50 2016

@author: William
"""
"""
import random, math
N = 20
position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = []
for iter in range(1000000):
    dir = random.choice([-1, 1])
    new_position = (position + dir) % N
    if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]:
        position = new_position
        pos_list.append(position)

"""
"""
import random, math
N = 20
position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = [] 
for iter in range(1000000):
    dir = random.choice([-1, 1])
    new_position = (position + dir) % N
    if random.uniform(0.0, 1.0) < weight[position] / weight[new_position]:
        position = new_position
    pos_list.append(position)
    

import random, math
N = 20
position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = []
for iter in range(1000000):
    dir = random.choice([-1, 1])
    new_position = (position + dir) % N
    if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]:
        position = new_position
    pos_list.append(position)

"""
"""
import random, math
N = 20; position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = [] 
for iter in range(1000000):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.5: 
        new_position = (position + 1) % N
        if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]: 
            position = new_position
        pos_list.append(position)
"""
"""
import random, math
N = 20; position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = []
for iter in range(1000000):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.5: 
        new_position = (position + 1) % N
        if random.uniform(0.0, 1.0) < weight[position] / weight[new_position]: 
            position = new_position
    pos_list.append(position)        
"""
import random, math
N = 20; position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = [] 
for iter in range(1000000):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.5: 
        new_position = (position + 1) % N
        if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]: 
            position = new_position
    pos_list.append(position)
import pylab
import numpy as np
pylab.figure(1)        
pylab.hist(pos_list,20,normed =1)
adj_weight = weight/(np.ones(len(weight))*sum(weight))
pylab.plot(adj_weight,'ro')