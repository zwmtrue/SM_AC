import random
import matplotlib.pyplot as plt
import numpy as np
N = 15
L = 10.0
sigma = 0.1
n_configs = 100
xs =[]# np.array()
plt.figure(1)
nums = np.ones(N)
for config in range(n_configs):
    x = []
    while len(x) < N:
        x.append(random.uniform(sigma, L - sigma))
        for k in range(len(x) - 1):
            if abs(x[-1] - x[k]) < 2.0 * sigma:
                x = []
                break
    
    plt.plot(nums*config,x,'bo')
    xs.append(x)
    
    #print x
plt.figure(2)
plt.plot(xs,'bo')            
