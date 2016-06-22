import random, math,pylab

x = 0.2
delta = 0.5
n_trials = 10000
data = []
for trial in xrange(n_trials):
    x_new = x + random.uniform(-delta, delta)
    if x_new > 0.0 and x_new < 1.0:
        #if random.uniform(0.0, 1.0) <  math.sqrt(x) / math.sqrt(x_new): 
        if random.uniform(0.0,1.0)< x**2/(x_new**2):
            x = x_new 
            data.append(x_new)
            
pylab.hist(data)