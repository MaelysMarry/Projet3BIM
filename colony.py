from bacteria import bacteria


class colony:

    def __init__(self, nutr, Pdeath, Pdivmax, Kx, length, resist=0, tol=0):

        self.nutr = nutr
        self.Pdeath = Pdeath
        self.Pdivmax = Pdivmax
        self.Kx = Kx
        self.length = length
        self.resist = resist
        self.tol = tol

        self.pop = []

        for i in range(length):

            self.pop.append(bacteria(self.Pdivmax,
                                     self.Kx,
                                     self.Pdeath,
                                     self.resist,
                                     self.tol))

    def updatePop(self):

        for i in self.pop:

            if i.divide(self.nutr):

                self.pop.append(bacteria(self.Pdivmax,
                                         self.Kx,
                                         self.Pdeath,
                                         self.resist,
                                         self.tol))

        for i in self.pop:

            if i.death():
                self.pop.remove(i)

    def run(self, T):

        for t in range(T):
            self.updatePop()


if __name__ == "__main__":

    nutr = 1
    Pdeath = 0.1
    Pdivmax = 0.6
    Kx = 0.1
    length = 20

    c = colony(nutr, Pdeath, Pdivmax, Kx, length)
    c.run(10)
