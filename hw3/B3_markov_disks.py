import random,math
import pylab
import os

#filename = 'disk_configuration.txt'
def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)
	
def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()

	
eta = .72

N_sqrt = 16
N = N_sqrt**2

two_delxy = 1.0/N_sqrt
delxy = two_delxy/2
sigma =  math.sqrt(eta/(N*math.pi))
#sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.3*sigma
n_steps = 1000


filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)

if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
    print 'starting from a new random configuration'


f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
show_conf(L, sigma, 'MCMC', '256_disk_initial.png')

for steps in range(n_steps):
    a = random.choice(L)
    b = [(a[0] + random.uniform(-delta, delta))%1.0, (a[1] + random.uniform(-delta, delta))%1.0]
    min_dist = min(dist(b,c) for c in L if c != a)
  
    if not (min_dist < 2.0 * sigma):
        a[:] = b
print L



show_conf(L, sigma, 'MCMC', '256_disk_final.png')