import numpy as np


class bacteria:

    def __init__(self, alpha, beta, Pdeath, resist, tol, state=0):

        self.alpha = alpha
        self.beta = beta
        self.Pdeath = Pdeath
        self.resist = resist
        self.state = state  # 0 for normal, 1 for tol

    def divide(self, N):

        if self.state == 0:

            if np.random.random() < self.alpha/(N-self.beta):
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
