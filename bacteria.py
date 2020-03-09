import numpy as np
import functions as fc


class bacteria:

    def __init__(self, Nm, Pdeath, sensi, tol, Pmut, state=1):

        self.Nm = Nm
        self.Pdeath = Pdeath
        self.sensi = sensi
        self.tol = tol
        self.Pmut = Pmut
        self.state = state  # 0 for tol, 1 for normal

    def divide(self, N):

        return (self.state == 1 and
                np.random.random() < fc.Pdi(N, self.Nm, self.Pdeath, 1e-5))

    def mutate(self, Pmut):

        return np.random.random() < self.Pmut

    def death(self, C):

        return np.random.random() < fc.Pde(self.Pdeath, C, self.sensi,
                                           self.state)

    def tolerance(self):

        if np.random.random() < self.tol and self.state == 1:
            self.state = not self.state

        elif np.random.random() < 1-self.tol and self.state == 0:
            self.state = not self.state
