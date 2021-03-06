
##Rita Abani 19244

##Dated : 22nd October 2021

''' This code pertains to a part of the parameter file required to tackle the question D.12  for the full state with integrator system'''


import numpy as np
import control as cnt
import sys
sys.path.append('..')  # add parent directory
import springParam as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
force_max = P.force_max  # limit on control signal
m = P.m
ell = P.ell
g = P.g
integrator_pole = -5

#  tuning parameters
tr = 2
zeta = 0.7

# State Space Equations
# xdot = A*x + B*u
# y = C*x
A = np.matrix([[0.0, 1.0],
               [-0.6, -0.1]])

B = np.matrix([[0.0],
               [0.2]])

C = np.matrix([[1.0, 0.0]])

# form augmented system
A1 = np.matrix([[0.0, 1.0, 0.0],
               [-0.6, -0.1, 0.0],
               [-1.0, 0.0, 0.0]])

B1 = np.matrix([[0.0],
               [0.2],
               [0.0]])

# gain calculation
wn = 2.2/tr  # natural frequency
des_char_poly = np.convolve(
    [1, 2*zeta*wn, wn**2],
    np.poly(integrator_pole))
des_poles = np.roots(des_char_poly)

# Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A1, B1)) != 3:
    print("The system is not controllable")
else:
    K1 = cnt.acker(A1, B1, des_poles)
    K = np.matrix([K1.item(0), K1.item(1)])
    ki = K1.item(2)

print('K: ', K)
print('ki: ', ki)
