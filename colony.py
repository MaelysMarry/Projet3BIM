from bacteria import bacteria
import matplotlib.pyplot as plt
import numpy as np


class colony:

    def __init__(self, Pdeath, Nm, length, C, sensi=0, tol=0, PmutS=0, PmutT=0,
                 sigmaS=0, sigmaT=0):

        self.Pdeath = Pdeath
        self.Nm = Nm
        self.length = length
        self.C = C
        self.sensi = sensi
        self.tol = tol
        self.PmutS = PmutS
        self.PmutT = PmutT
        self.sigmaS = sigmaS
        self.sigmaT = sigmaT

        self.pop = []

        for i in range(length):

            self.pop.append(bacteria(self.Nm,
                                     self.Pdeath,
                                     self.sensi
                                     + self.sigmaS*np.random.randn(),
                                     self.tol
                                     + self.sigmaT*np.random.randn()))

    def updatePop(self):

        div = []
        death = []

        for i in self.pop:

            if i.divide(len(self.pop)):

                if i.mutate(self.PmutS):

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi
                                        + self.sigmaS * np.random.randn(),
                                        i.tol))

                if i.mutate(self.PmutT):

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.tol
                                        + self.sigmaT * np.random.randn()))

                else:

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.tol))

            i.tolerance()

            if i.death(self.C):
                death.append(self.pop.index(i))

        death = death[::-1]

        for i in range(len(death)):
            self.pop.pop(death[i])

        self.pop += div
        # self.C = .75 * self.C

    def stats(self):
        # nbTol = 0
        # for i in self.pop:
        #     if i.state == 0:
        #         nbTol += 1

        # print(nbTol/len(self.pop))

        moyS = 0
        moyT = 0
        for i in self.pop:
            moyS += i.sensi
            moyT += i.tol
        # print(moyS/(len(self.pop)+1))
        # print(moyT/(len(self.pop)+1))
        # print("\n")

        return (len(self.pop), moyS/(len(self.pop)+1), moyT/(len(self.pop)+1))

    def run(self, T):

        ret = [self.stats()]

        for t in range(T):
            print(t, len(self.pop))
            # print(self.stats())
            self.updatePop()
            ret.append(self.stats())

            if t % 100 == 0:
                self.C = 1.8
            else:
                self.C = 0

            if len(self.pop) == 0:
                print("oh no")
                return 1

        return ret


if __name__ == "__main__":

    Nm = 100000
    Pdeath = 0.1
    length = 100
    C = 3
    sensi = .5
    tol = 0.1
    PmutS = 1e-4
    PmutT = 0.01
    sigmaS = 0.01
    sigmaT = 0.01
    T = 100

    c = colony(Pdeath, Nm, length, C, sensi, tol, PmutS, PmutT, sigmaS, sigmaT)
    results = c.run(T)

    # plt.plot(range(T+1), [results[i][0] for i in range(len(results))])
    plt.plot(range(T+1), [results[i][1] for i in range(len(results))])
    plt.plot(range(T+1), [results[i][2] for i in range(len(results))])
    plt.show()

    # review 2019
