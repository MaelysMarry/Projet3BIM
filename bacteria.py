import numpy as np
import functions as fc


class bacteria:

    def __init__(self, Nm, Pdeath, sensi, tol, state=1):

        self.Nm = Nm
        self.Pdeath = Pdeath
        self.sensi = sensi
        self.tol = tol
        self.state = state  # 0 for tol, 1 for normal

    def divide(self, N):

        if self.state == 1:

            if np.random.random() < fc.Pdi2(N, self.Nm, self.Pdeath):
                # print(fc.Pdi(N, self.Nm, self.Pdeath, 0.1))
                return True

            else:
                return False

        else:
            return False

    def death(self, C):

        if np.random.random() < fc.Pde(self.Pdeath, C, self.sensi,
                                       self.state):
            return True

        else:
            return False

    def tolerance(self):

        if np.random.random() < self.tol and self.state == 1:
            self.state = not self.state

        elif np.random.random() < 1-self.tol and self.state == 0:
            self.state = not self.state
