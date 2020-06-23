import numpy as np
import functions as fc


class bacteria:

    def __init__(self, Nm, Pdeath, sensi, Ptol, time_tol_max, state=1):

        self.Nm = Nm
        self.Pdeath = Pdeath
        self.sensi = sensi

        if Ptol < 0:
            self.Ptol = 0
        elif Ptol > 1:
            self.Ptol = 1
        else:
            self.Ptol = Ptol

        self.time_tol_max = time_tol_max
        self.state = state  # 0 for Ptol, 1 for normal

        self.time_tol = 0

    def divide(self, N):

        return (self.state == 1 and
                np.random.random() < fc.Pdi(N, self.Nm, self.Pdeath, 1e-5))

    def mutate(self, Pmut):

        return np.random.random() < Pmut

    def death(self, C):

        return np.random.random() < fc.Pde(self.Pdeath, C, self.sensi,
                                           self.state)

    def tolerance(self):

        if self.state == 1 and np.random.random() < self.Ptol:
            self.state = not self.state

        elif self.state == 0 and self.time_tol < self.time_tol_max:
            self.time_tol += 1

        elif self.state == 0 and self.time_tol >= self.time_tol_max:
            self.state = not self.state
