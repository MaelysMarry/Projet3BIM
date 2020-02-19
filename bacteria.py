import numpy as np


class bacteria:

    def __init__(self, Nm, Pdeath, resist, tol, state=0):

        self.Nm = Nm
        self.Pdeath = Pdeath
        self.resist = resist
        self.state = state  # 0 for normal, 1 for tol

    def divide(self, N):

        if self.state == 0:

            if np.random.random() < self.Pdeath + (self.Nm-N)/self.Nm:
                return True

            else:
                return False

        else:
            return False

    def death(self):

        if self.state == 0:

            if np.random.random() < self.Pdeath:
                return True

            else:
                return False
