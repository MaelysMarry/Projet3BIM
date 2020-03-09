from bacteria import bacteria
import matplotlib.pyplot as plt


class colony:

    def __init__(self, Pdeath, Nm, length, C, sensi=0, tol=0):

        self.Pdeath = Pdeath
        self.Nm = Nm
        self.length = length
        self.C = C
        self.sensi = sensi
        self.tol = tol

        self.pop = []

        for i in range(length):

            self.pop.append(bacteria(self.Nm,
                                     self.Pdeath,
                                     self.sensi,
                                     self.tol))

    def updatePop(self):

        countDiv = 0
        countDeath = 0

        for i in self.pop:

            if i.divide(len(self.pop)):
                countDiv += 1

            i.tolerance()

            if i.death(self.C):
                countDeath += 1

        for i in range(countDiv):

            self.pop.append(bacteria(self.Nm,
                                     self.Pdeath,
                                     self.sensi,
                                     self.tol))

        for i in range(countDeath):

            self.pop.pop()

    def stats(self):
        # nbTol = 0
        # for i in self.pop:
        #     if i.state == 0:
        #         nbTol += 1

        # print(nbTol/len(self.pop))
        return len(self.pop)

    def run(self, T):

        ret = [self.stats()]

        for t in range(T):
            print(t)
            # print(self.stats())
            self.updatePop()
            ret.append(self.stats())

        return ret


if __name__ == "__main__":

    Nm = 10000
    Pdeath = 0.1
    length = 100
    C = .3
    sensi = 0
    tol = 0.1
    T = 40

    c = colony(Pdeath, Nm, length, C, sensi, tol)
    results = c.run(T)

    plt.plot(range(T+1), results)
    plt.show()
