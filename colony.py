from bacteria import bacteria
import matplotlib.pyplot as plt


class colony:

    def __init__(self, Pdeath, alpha, beta, length, resist=0, tol=0):

        self.Pdeath = Pdeath
        self.alpha = alpha
        self.beta = beta
        self.length = length
        self.resist = resist
        self.tol = tol

        self.pop = []

        for i in range(length):

            self.pop.append(bacteria(self.alpha,
                                     self.beta,
                                     self.Pdeath,
                                     self.resist,
                                     self.tol))

    def updatePop(self):

        for i in self.pop:

            if i.divide(len(self.pop)):

                self.pop.append(bacteria(self.alpha,
                                         self.beta,
                                         self.Pdeath,
                                         self.resist,
                                         self.tol))

        for i in self.pop:

            if i.death():
                self.pop.remove(i)

    def stats(self):
        return len(self.pop)

    def run(self, T):

        ret = [self.stats()]

        for t in range(T):
            self.updatePop()
            ret.append(self.stats())

        return ret


if __name__ == "__main__":

    alpha = 2
    beta = 1
    Pdeath = 0.1
    length = 20
    T = 10000

    c = colony(Pdeath, alpha, beta, length)
    results = c.run(T)

    plt.plot(range(T+1), results)
    plt.show()
