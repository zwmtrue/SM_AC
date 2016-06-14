# -*- coding: utf-8 -*-
"""
Created on Tue May 31 01:02:56 2016
This homework session 1 of Statistical Mechanics: Algorithms and Computations is divided into three parts (A, B, C).

In the first part, you estimate pi (the mathematical constant) by using a direct-sampling algorithm and determine the statistical error of your numerical calculation.

In the second part, you again estimate pi, but this time for a Markov-chain algorithm. The precision of the result depends on the step size delta, which itself changes the rejection rate. You will see that performance is best when delta is chosen such that about half of the proposed moves are accepted. This is called the "1/2 rule". It is a rule of thumb, not a mathematical law.

Finally, in the third part, you quantify the error associated with the Markov-chain algorithm using the powerful bunching algorithm.

NB 1: Please use pylab (inside Python) for graphics output (if possible), following the examples that are provided. To get started this first week, many of the programs are provided - don't hesitate to study them. They are all modifications of the programs available from the Coursera website (see the forum if necessary).

NB 2: The passing grade for this homework session is 25%.
@author: zwmtrue
A

We first study the direct-sampling algorithm direct_pi.py and modify it somewhat.

A1

Consider the program "direct_pi_multirun.py". Modify it so that it computes the root mean square (rms) deviation:

rms deviation=1n_runs∑i=0n_runs−1(πiest−π)2

, where pi^est_i is the estimation of pi in run i of direct_pi_multirun.py, while pi = 3.1415926... is the mathematical constant.

NB: In the rms deviation, one squares the difference so that positive and negative deviations add up, rather than compensate each other. At the end, one takes a square root in order to "undo" the squaring. Take n_runs = 500, and plot the rms deviation according to the above formula as a function of n_trials for n_trials = 2^4, 2^5,...,2^12 (use log-log-scaling of axes).

For convenience (week 1 bonus), find below the code that does all this for you. 
"""

import random, math, pylab

def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits

n_runs = 500
n_trials_list = []
sigmasqs = []
for poweroftwo in range(4, 13):
    n_trials = 2 ** poweroftwo
    sigmasq = 0.0
    for run in range(n_runs):
        pi_est = 4.0 * direct_pi(n_trials) / float(n_trials)
        sigmasq += (pi_est - math.pi) ** 2
    sigmasqs.append(math.sqrt(sigmasq/(n_runs)))
    n_trials_list.append(n_trials)

pylab.plot(n_trials_list, sigmasqs, 'o')
pylab.plot([10.0, 10000.0], [1.642 / math.sqrt(10.0), 1.642 / math.sqrt(10000.0)])
pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel('number of trials')
pylab.ylabel('root mean square deviation')
pylab.title('Direct sampling of pi: root mean square deviation vs. n_trials')
pylab.savefig('direct_sampling_rms_deviation.png')
pylab.show()