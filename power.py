from cProfile import label
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
    return 1/(1+np.exp(-100*(z-Pmax(E))))

def Pd(x,c):
    return fourier(x,c)

def g(x):
    return G*(x-.5)

def P(x,v,c,E):
    PD = Pd(x,c) - .95*sigmoid(Pd(x,c),E)* Pd(x,c) + g(x)*v
    if PD >= 0:
        return PD
    if PD < 0:
        return 0

def F(x,v):
    return b*v + C + s*(v**2)*np.exp(-((x-xturn)/(.2*wturn))**2) 

def Pmax(E):
    return -(P0max/Emax**2)*x**2 + P0max

xturn = .5
wturn = .05
s = .3
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
    t=0
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

c = bestcoeffs
x = .001
v = .001
E = 0
t=0
dt = .001
stopped = False
noE = False
while x < distance:
    f = F(x,v)
    p = P(x,v,c,E)
    v = p/f
    x += v*dt
    E += Pd(x,c)*dt
    t += dt
    plt.scatter(x,10*v, color = "g", marker=".")
    plt.scatter(x,Pd(x,c), color = "b", marker=".")
    #plt.scatter(x, 5*(x-.5)**2 + 9, color = "r", marker="." )
    if v < 0:
        stopped = True
        break
    if E > Emax:
        noE = True
        break
    if t > bestt:
        break
plt.show()

print(bestcoeffs)
print("Attemt {} was successful".format(successful))
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
    f = F(v)
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

    G_.append(g(x)* 5)
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

yy= plt.plot(X_,G_, label = "g(x)")
plt.legend()
plt.xlim(0,1)
plt.ylim(-200,700)
plt.grid()

    # plt.title("Energy spent is{}".format(sum(E_), "right"))
    # plt.fill_between(xx,0,yy)
plt.legend()

plt.show()



# fig = plt.figure()

# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)

# ax1.plot(X_,P_)
# ax2.plot(X_,E_)
# ax3.plot(X_,V_)
# ax4.plot(X_,G_)

# ax1.title.set_text('Power vs. position')
# ax2.title.set_text('Energy vs. position')
# ax3.title.set_text('Velocity vs. position')
# ax4.title.set_text('Gravity vs. position')


# ax[2].plot(P_,V_ , label="P-V")
# plt.show()
