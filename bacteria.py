import numpy as np
import functions as fc


class bacteria:

    def __init__(self, Nm, Pdeath, sensi, tol, state=0):

        self.Nm = Nm
        self.Pdeath = Pdeath
        self.sensi = sensi
        self.state = state  # 0 for normal, 1 for tol

    def divide(self, N):

        if self.state == 0:

            if np.random.random() < fc.Pdi2(N, self.Nm, self.Pdeath):  # -1e-4):
                # print(fc.Pdi(N, self.Nm, self.Pdeath, 0.1))
                return True

            else:
                return False

        else:
            return False

    def death(self, C):

        if self.state == 0:

            if np.random.random() < self.Pdeath:
                return True

            else:
                return False
