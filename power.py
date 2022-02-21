from turtle import color
import numpy as np
import random
import matplotlib.pyplot as plt

def taylor(x,c):
    ts = [1]
    n=1
    while len(ts) < ncoef:
        ts.append(x**n)
        if len(ts) < ncoef:
            ts.append(n*np.cos(x))
        n+=1
    return np.dot(np.array(c),np.array(ts))

def fourier(x,c):
    fs = [1]
    n=1
    while len(fs) < ncoef:
        fs.append(np.sin(n*x))
        if len(fs) < ncoef:
            fs.append(np.cos(n*x))
        n+=1
    return np.dot(np.array(c),np.array(fs)) 

def sigmoid(z,E):
    return 1/(1+np.exp(-100*(z-Pmax(E))))

def Pd(x,c):
    return fourier(x,c)

def g(x):
    return 0

def P(x,v,c,E):
    PD = Pd(x,c) - .95*sigmoid(Pd(x,c),E)* Pd(x,c) + g(x)*v
    if PD >= 0:
        return PD
    if PD < 0:
        return 0

def F(v):
    return b*v + C #add guassian for turns

def Pmax(E):
    return -(P0max/Emax**2)*x**2 + P0max


Emax = 200
P0max = 50
distance = 1
b = .2
C = 7
G = 2
bestcoeffs = 'none'
bestt = 1
ncoef = 20
dt = .001
attempt = 1
nattempts = 1000
while attempt <= nattempts:
    print(attempt)
    c = [random.uniform(0,1.5*P0max)]
    while len(c) < ncoef:
        rand = random.uniform(-1.5*P0max,1.5*P0max)
        c.append(rand)
    x = .001
    v = .001
    E = 0
    t=0
    stopped = False
    noE = False
    while x < distance:
        f = F(v)
        p = P(x,v,c,E)
        v = p/f
        x += v*dt
        E += Pd(x,c)*dt
        t += dt

        if  v <= 0:
            stopped = True
            break
        if E >= Emax:
            noE = True
            break
        if t > bestt:
            break

    if (t < bestt) and (not stopped) and (not noE):
        bestt = t
        bestv = v
        bestcoeffs = c
        print(bestt)
    attempt += 1
print(bestcoeffs)
print(bestt)

c = bestcoeffs
x = .001
v = .001
E = 0
t=0
dt = .001
stopped = False
noE = False
while x < distance:
    f = F(v)
    p = P(x,v,c,E)
    v = p/f
    x += v*dt
    E += Pd(x,c)*dt
    t += dt
    plt.scatter(x,Pd(x,c), color = "b", marker=".")
    plt.scatter(x,Pd(x,c), color = "b", marker=".")
    #plt.scatter(x, 10*np.sin(10*x) + 9, color = "r", marker="." )
    if v <= 0:
        stopped = True
        break
    if E > Emax:
        noE = True
        break
    if t > bestt:
        break
plt.show()
