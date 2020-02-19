from bacteria import bacteria


class colony:

    def __init__(self, nutr, Pdeath, Pdivmax, Kx, length, resist, tol):

        self.nutr = nutr
        self.Pdeath = Pdeath
        self.Pdivmax = Pdivmax
        self.Kx = Kx, self.length = length
        self.resist = resist
        self.tol = tol

        self.pop = []

        for i in range(length):

            self.pop.append(bacteria(self.Pdivmax,
                self.Kx,
                self.Pdeath,
                self.resist,
                self.tol)

    def updatePop(self):

        for i in self.pop:

            if i.divide():

                self.pop.append(bacteria(self.Pdivmax,
                    self.Kx,
                    self.Pdeath,
                    self.resist,
                    self.tol)

        for i in self.pop:

            if i.death():
                self.pop(i)
