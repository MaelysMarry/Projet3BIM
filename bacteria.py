import numpy as np
import functions as fc


class bacteria:

    def __init__(self, Nm, Pdeath, sensi, tol, state=1):

        self.Nm = Nm
        self.Pdeath = Pdeath
        self.sensi = sensi

        if tol < 0:
            self.tol = 0
        elif tol > 1:
            self.tol = 1
        else:
            self.tol = tol

        self.state = state  # 0 for tol, 1 for normal
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

        if np.random.random() < self.tol and self.state == 1:
            self.state = not self.state

        elif np.random.random() < 1-self.tol and self.state == 0:
            self.state = not self.state
