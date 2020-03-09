from bacteria import bacteria
import matplotlib.pyplot as plt
import numpy as np


class colony:

    def __init__(self, Pdeath, Nm, length, C, sensi=0, tol=0, Pmut=0, sigmaS=0,
                 sigmaT=0):

        self.Pdeath = Pdeath
        self.Nm = Nm
        self.length = length
        self.C = C
        self.sensi = sensi
        self.tol = tol
        self.Pmut = Pmut
        self.sigmaS = sigmaS
        self.sigmaT = sigmaT

        self.pop = []

        for i in range(length):

            self.pop.append(bacteria(self.Nm,
                                     self.Pdeath,
                                     self.sensi,
                                     self.tol,
                                     self.Pmut))

    def updatePop(self):

        div = []
        death = []

        for i in self.pop:

            if i.divide(len(self.pop)):

                if i.mutate():

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi
                                        + self.sigmaS * np.random.randn(),
                                        i.tol,
                                        i.Pmut))

                if i.mutate():

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.tol
                                        + self.sigmaT * np.random.randn(),
                                        i.Pmut))

                else:

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.tol,
                                        i.Pmut))

            i.tolerance()

            if i.death(self.C):
                death.append(self.pop.index(i))

        death = death[::-1]

        for i in range(len(death)):
            self.pop.pop(death[i])

        self.pop += div

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
    sensi = .5
    tol = 0.1
    Pmut = 0.01
    sigmaS = 0.01
    sigmaT = 0.01
    T = 10000

    c = colony(Pdeath, Nm, length, C, sensi, tol, Pmut, sigmaS, sigmaT)
    results = c.run(T)

    plt.plot(range(T+1), results)
    plt.show()
