import random,math,cmath
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
    
def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)
	
eta = .72

N_sqrt = 8
N = N_sqrt**2

two_delxy = 1.0/N_sqrt
delxy = two_delxy/2
sigma =  math.sqrt(eta/(N*math.pi))
#sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.3*sigma
n_steps = 10000


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
print"1st 1e4 run for a thermal stablized conf"
for steps in range(10000):
    a = random.choice(L)
    b = [(a[0] + random.uniform(-delta, delta))%1.0, (a[1] + random.uniform(-delta, delta))%1.0]
    min_dist = min(dist(b,c) for c in L if c != a)
  
    if not (min_dist < 2.0 * sigma):
        a[:] = b
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
 
#show_conf(L, sigma, 'Initial', 'eta=.72_10runs_64_disk_initial.png')
eta_vec = [float(et)/(100.0) for et in range( 72,0,-1)]
mean_Psi = {}
n_runs=1000
print "iterating with eta"
for i in range(len(eta_vec)):#run old final conf as new initial for ten times
    eta = eta_vec[i]
    sigma = math.sqrt(eta/(N*math.pi))
    sigma_sq = sigma ** 2
    delta = 0.3 * sigma
    mean_Psi[eta] = 0.0
    
    n_steps = 10000
    smallsteps = 100
    n_runs = n_steps/smallsteps
    for steps in range(n_steps):
        
        a = random.choice(L)
        b = [(a[0] + random.uniform(-delta, delta))%1.0, (a[1] + random.uniform(-delta, delta))%1.0]
        min_dist = min(dist(b,c) for c in L if c != a)
      
        if not (min_dist < 2.0 * sigma):
            a[:] = b
        if steps % smallsteps ==0:
            mean_Psi[eta] += abs(Psi_6(L, sigma))
    mean_Psi[eta] /= n_runs
    print "Mean Psi(",eta,")=",mean_Psi[eta]

f = open('psi_values', 'w')
for a in mean_Psi:
    f.write(str(a) + ' ' + str(mean_Psi[a]) + '\n')
f.close()
Psi_vec = [mean_Psi[v] for v in eta_vec]
pylab.plot(eta_vec,Psi_vec)
pylab.axis('scaled')
pylab.title('Psi(eta)')
pylab.xlabel('eta')
pylab.ylabel('Psi')
pylab.axis([0.0, .8, 0.0, .7])
pylab.savefig('Psi(eta)')
pylab.show()
pylab.close() 
    
    

