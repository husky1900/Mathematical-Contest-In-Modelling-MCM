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
        fs.append(np.sin(n*x/distance))
        if len(fs) < ncoef:
            fs.append(np.cos(n*x/distance))
        n+=1
    return np.dot(np.array(c),np.array(fs)) 

def sigmoid(z,E):
    return 1/(1+np.exp(-10*(z-Pmax(E))))

def Pd(x,c):
    return fourier(x,c)

def g(x):
    return -G*np.sin(12*x)

def P(x,v,c,E):
    PD = Pd(x,c) - .95*sigmoid(Pd(x,c),E)* Pd(x,c) - g(x)*v #pay attension to sign
    if PD >= 0:
        return PD
    if PD < 0:
        return 0

def F(x,v):
    gaussum = 0
    i = 0
    while i < len(xturn):
        gaussum += s[i]*(v**2)*np.exp(-((x-xturn[i])/(.2*wturn[i]))**2)
        i += 1
    return b*v + C + gaussum

def Pmax(E):
    return -(P0max/Emax**2)*x**2 + P0max

xturn = [.19,.2,.72]
wturn = [.05, .05,.05]

s = [.4,.3,.3]
Emax = 100
P0max = 50
distance = 1
b = .2
C = 7
G = 2
bestcoeffs = 'none'
bestt = 2
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
    t = 0
    stopped = False
    noE = False
    while x < distance:
        f = F(x,v)
        p = P(x,v,c,E)
        v = p/f
        x += v*dt
        E += Pd(x,c)*dt
        t += dt

        if  v < 0:
            stopped = True
            break
        if E >= Emax:
            noE = True
            break
        if t > bestt:
            break

    attempt += 1
    if (t < bestt) and (not stopped) and (not noE):
        bestt = t
        bestv = v
        bestcoeffs = c
        attempt = 0
        print(bestt)
    
print(bestcoeffs)
print(bestt)

F_= []
P_= []
V_ = []
X_ = [] 
E_ = []
T_ = [] 
G_ = []
c = bestcoeffs
x = .001
v = .001
E = 0
t=0
dt = .0001
stopped = False
noE = False
while x < distance:
    f = F(x,v)
    F_.append(f)
    
    p = P(x,v,c,E)
    P_.append(Pd(x,c))
    
    v = p/f
    V_.append(v)
    
    x += v*dt
    X_.append(x)
    
    E += Pd(x,c)*dt
    E_.append(E)
    
    t += dt
    T_.append(t)

    G_.append(g(x)*v*dt)
    # plt.scatter(x,Pd(x,c), color = "b", marker=".")
    # plt.scatter(x,Pd(x,c), color = "b", marker=".")
    #plt.scatter(x, 10*np.sin(10*x) + 9, color = "r", marker="." )
    if v <= 0:
        stopped = True
        break
    if E > Emax:
        noE = True
        break
    if t > bestt:
        break

xx= plt.plot(X_, P_, label="P(x)")
plt.xlabel("Distance")
plt.ylabel("Power expendure")

#yy= plt.plot(X_,G_, label = "g(x)")
plt.legend()
plt.xlim(0,1)
plt.ylim(-200,700)
plt.grid()

    # plt.title("Energy spent is{}".format(sum(E_), "right"))
    # plt.fill_between(xx,0,yy)
plt.legend()
plt.show()


