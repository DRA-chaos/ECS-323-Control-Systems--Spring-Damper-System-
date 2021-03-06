# Rita Abani 19244
#This is the code for PD controller, for D.7
import numpy as np
import Parameters for D.8 as P
import sys
sys.path.append('..')  # add parent directory
import springParam as P0
from PD controller for the spring mass system import PDControl


class springController:

    def __init__(self):
        # Instantiates the PD object
        self.thetaCtrl = PDControl(P.kp, P.kd, P0.tau_max, P.beta, P.Ts)
        self.limit = P0.tau_max

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        theta_r = y_r[0]
        theta = y[0]

        # compute equilibrium torque tau_e
        tau_e = P0.k * np.float64(theta)
        # compute the linearized torque using PD
        tau_tilde = self.thetaCtrl.PD(theta_r, theta, False)
        # compute total torque
        tau = tau_e + tau_tilde
        tau = self.saturate(tau)
        return [tau]

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u

