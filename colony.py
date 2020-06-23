from bacteria import bacteria
import matplotlib.pyplot as plt
import numpy as np
import math as math


class colony:

    def __init__(self, Pdeath, Nm, length, C, sensi=0, Ptol=0, time_tol_max=0,
                 PmutS=0, PmutT=0, sigmaS=0, sigmaT=0):

        self.Pdeath = Pdeath
        self.Nm = Nm
        self.length = length
        self.C = C
        self.sensi = sensi
        self.Ptol = Ptol
        self.time_tol_max = time_tol_max
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
                                     self.Ptol
                                     + self.sigmaT*np.random.randn(),
                                     int(self.time_tol_max
                                         + np.random.randn())))

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
                                        i.Ptol,
                                        i.time_tol_max))

                if i.mutate(self.PmutT):

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.Ptol
                                        + self.sigmaT * np.random.randn(),
                                        i.time_tol_max))

                if i.mutate(self.PmutT):

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.Ptol,
                                        int(i.time_tol_max
                                            + np.random.randn())))
                else:

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.Ptol,
                                        i.time_tol_max))

            i.tolerance()

            if i.death(self.C):
                death.append(self.pop.index(i))

        death = death[::-1]

        for i in range(len(death)):
            self.pop.pop(death[i])

        self.pop += div
        self.C = .75 * self.C

    def stats(self):
        # nbTol = 0
        # for i in self.pop:
        #     if i.state == 0:
        #         nbTol += 1

        # print(nbTol/len(self.pop))

        moyS = 0
        moyT = 0
        moyD = 0
        for i in self.pop:
            moyS += i.sensi
            moyT += i.Ptol
            moyD += i.time_tol_max
        # print(moyS/(len(self.pop)+1))
        # print(moyT/(len(self.pop)+1))
        # print("\n")

        return (len(self.pop), moyS/(len(self.pop)+1), moyT/(len(self.pop)+1),
                moyD/(len(self.pop)+1))

    def run(self, T):

        ret = [self.stats()]

        for t in range(T):
            print(t, len(self.pop), self.C)
            # print(self.stats())
            self.updatePop()
            ret.append(self.stats())

            if t % 10 == 0:
                self.C = .2*t

            if len(self.pop) == 0:
                print("oh no")
                return 1

        return ret


if __name__ == "__main__":

    Nm = 100000
    Pdeath = 0.1
    length = 100
    C = 1.2
    sensi = .5
    Ptol = 0.01
    time_tol_max = 1
    PmutS = 0.01
    PmutT = 0.01
    sigmaS = 0.1
    sigmaT = 0.1
    T = 100

    c = colony(Pdeath, Nm, length, C, sensi, Ptol, time_tol_max, PmutS, PmutT,
               sigmaS, sigmaT)
    results = c.run(T)

    # plt.plot(range(T+1), [results[i][0] for i in range(len(results))])
    plt.plot(range(T+1), [results[i][1] for i in range(len(results))])
    plt.plot(range(T+1), [results[i][2] for i in range(len(results))])
    plt.plot(range(T+1), [results[i][3] for i in range(len(results))])
    plt.show()

    # review 2019
