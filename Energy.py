import math

# Relevant physical quantities
E = 2000 # The total energy that a rider can use pedaling the bike forward; unit of KJ
D = 10000 # The total distance of a race track; unit of m
g = 9.81 # The acceleration due to gravity on the surface of the earth; unit of m/s^2
x = 0 # The distance the rider has cycled; starts at 0; unit of m
dt = .01 # The increment of time added in each iteration; unit of s

# Initializing lists to keep track of different physical quantities
E_ = [E,E] # energy
X_ = [0.0, 0.001] # distance cycled
F_ = [0,0] # External forces acting on the rider-bike system,
# i.e. gravity, rolling friction, air resistance
V_ = [0.0,0.1] # Velocity of the rider-bike system
T_ = [0,0] # Time, each element will be dt greater than the previous one
A_ = [0,0] # Acceleration of the rider-bike system

# Relevant physical constants
G = 0 # gradient of the road, negative values denote downhill, positive ones denote uphill
M = 85 # assumed mass of the rider-bike system; in unit of kg
mu = 0.02 # coefficient of rolling friction
v = 0.1 # m/s
A = 0.38 # frontal surface area of the rider-bike system; in unit of m^2
rho = 1.2 # air density at sea level; in unit of kg/m^3
Cd = 0.5 # drag coefficient
Constant = Cd * A * rho # variable to make the code more readable


# Returns the net force acting against the rider-bike system
# @param  x, the distance traveled by the rider as of the last time increment
# @param  v, the velocity of the rider as of the last time increment
# @return F_net, the net force acting against the rider-bike system

def F(x, v):
    F_g = g * math.sin(math.atan(G)) * M
    F_r = F_g * mu
    F_a = 0.5 * Constant * v**2
    F_net = -(F_g+F_r+F_a)
    return F_net

def W(x):
	return x**2

# while the distance traveled is less than the total distance of the course
while X_[-1] < D:
    # distance traveled since the last time increment
	delta_x = X_[-1] - X_[-2]
    # work done by the rider since the last time increment
    delta_w = W(X_[-1])
    # net force working against the rider-bike system during the last time increment
    delta_f = F(X_[-1],V_[-1])
    # work that was translated to velocity since the last time increment
    # calculated by subtracting work used to overcome the resistive forces
    # from work put in by the rider
    work_vel = delta_w - delta_f * delta_x
    
    accel_cur = work_vel / (M * delta_x)
	A_.append(accel_cur)

	vel_cur = V_[-1] + A_[-1] * dt
	V_.append(vel_cur)

	x_cur = X_[-1] + V_[-1]*dt
	X_.append(x_cur)
    
	T_.append(T_[-1]+dt)

print(T_[-1])
