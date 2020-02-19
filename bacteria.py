import numpy as np


class bacteria:

    def __init__(self, Pdivmax, Kx, Pdeath, resist, tol, state=0):

        self.Pmax = Pdivmax
        self.Kx = Kx
        self.Pdeath = Pdeath
        self.resist = resist
        self.state = state  # 0 for normal, 1 for tol

    def divide(self, nutr):

        if self.state == 0:

            if np.random.random() < (self.Pmax*nutr)/(nutr+self.Kx):
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

        else:
            return False
