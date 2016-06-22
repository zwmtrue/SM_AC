import random

x, y = 0.0, 0.0
delta = 0.1
n_trials = 400000
n_hits = 0
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    #if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
    if (x+del_x)**2 + (y+del_y)**2<= 1.0:
        x, y = x + del_x, y + del_y
    z = random.uniform(-1.0, 1.0)
    if x**2 + y**2 + z**2 < 1.0: n_hits += 1
print '<Q_3>=',2.0 * n_hits / float(n_trials)
