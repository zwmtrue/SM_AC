# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:40:17 2016
B1

Generalize the program markov_pi.py to implement an efficient Markov-chain Monte Carlo algorithm to sample uniformly distributed points inside the d-dimensional unit sphere, using the following hints:

Represent the configuration point as a list: x = [x_0, x_1,...., x_k, ..., x_{d - 1}]

Start the simulation at the origin [0.0, 0.0, 0.0, ... 0.0] (you can program this as: x = [0] * d), as in Sections A2 and A3.

Instead of modifying all components of x at a time, as we did in markov_pi.py, modify only one component at each iteration i (with i=0, 1, 2,...., n_trials). This can be done as in:

Then you should accept the move if the new radius is <1, and reject otherwise (remaining in the same configuration).

Use an optimized way of computing the new radius (useful when d is large):

Do not forget to initialize correctly the variable old_radius_square, and to update it as needed.

Once the code is ready:

    Upload your program, which works for a general d.
@author: zwmtrue
"""
import random,math,pylab

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

def q(d,n_trials):
#q(d) calculates <Q_d+1>
    x = [0]*d
    old_radius_suqre = 0.0
    delta = 0.1
    #n_trials = 400000
    n_hits = 0
   # r =[]
    for i in range(n_trials):
        k =random.randint(0,d-1)
        x_old_k = x[k]
        x_new_k = x_old_k + random.uniform(-delta,delta)
        new_radius_square = old_radius_suqre +x_new_k**2 - x_old_k**2
        if new_radius_square<=1:
            x[k] = x_new_k
            old_radius_suqre = new_radius_square
            #r.append(math.sqrt(new_radius_square))
        alpha = random.uniform(-1.0, 1.0)
        if (new_radius_square +alpha**2)< 1.0: n_hits += 1
    
    Q_d_plus_1 = 2.0*n_hits / float(n_trials)
    #print '<Q_',d+1,'>=',  Q_d_plus_1
    return Q_d_plus_1

Q_dplus1_ave ={}
d_max = 199
n_vec  =[10,100,1000,10000,100000]#,1000000]
n = len(n_vec)
d_vec = range(1,d_max+1)
V_sph_ave = {}
n_runs = 10
V_sph_ave[1] =[2]*n
V_sph_sq_ave = {}
V_sph_sq_ave[1] =[4]*n
 
for d in d_vec:
    Q_dplus1_ave[d] = [0]*n
    V_sph_ave[d+1] = [0]*n
    V_sph_sq_ave[d+1] = [0]*n
 
    for iN in range(n):
        n_trails = n_vec[iN]
        V_sph_d = []
        V_sph_sq_d = []
        qd = []
 
        for run in range(n_runs):
    
            qd.append(q(d,n_trails))
            V_sph_d.append(V_sph_ave[d][iN]*qd[-1])
            V_sph_sq_d.append(V_sph_d[-1]**2)
        
        Q_dplus1_ave[d][iN] = sum(qd)/len(qd)
        V_sph_ave[d+1][iN] = sum(V_sph_d)/len(V_sph_d)
        V_sph_sq_ave[d+1][iN] = sum(V_sph_sq_d)/len(V_sph_sq_d)        
        
        print '\nn_trails=',n_trails,'Average of',n_runs,'runs' 
        print '<Q_',d+1,'>=',Q_dplus1_ave[d][iN]
        print '<V_sph[',d+1,']>=',V_sph_ave[d+1][iN]
        print '<V_sph[',d+1,']^2> =',V_sph_sq_ave[d+1][iN]
        #estimate the error on the average as 
        #sqrt(<V_sph(20)^2> - <V_sph(20)>^2)/sqrt(n_runs)
        diff = abs(V_sph_sq_ave[d+1][iN] - V_sph_ave[d+1][iN]**2)
        print 'Error = ',math.sqrt(diff)/math.sqrt(n_runs)
        
        

"""    
V_vec = [V_sph_d[v] for v in d_vec ]
V_anl_vec =[V_sph(d) for d in d_vec]
np, = pylab.plot(d_vec,V_vec,label ='Numercial') 
ap, = pylab.plot(d_vec,V_anl_vec,label = 'Analytical')
pylab.yscale('log')
pylab.legend(handles=[np,ap])
pylab.savefig('V_sph(d)_Numercial_vs_Analytical.png')
""" 