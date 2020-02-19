from bacteria import bacteria
import matplotlib.pyplot as plt


class colony:

    def __init__(self, Pdeath, Nm, length, resist=0, tol=0):

        self.Pdeath = Pdeath
        self.Nm = Nm
        self.length = length
        self.resist = resist
        self.tol = tol

        self.pop = []

        for i in range(length):

            self.pop.append(bacteria(self.Nm,
                                     self.Pdeath,
                                     self.resist,
                                     self.tol))

    def updatePop(self):

        for i in self.pop:

            if i.divide(len(self.pop)):

                self.pop.append(bacteria(self.Nm,
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

    Nm = 4000
    Pdeath = 0.1
    length = 100
    T = 100

    c = colony(Pdeath, Nm, length)
    results = c.run(T)

    plt.plot(range(T+1), results)
    plt.show()
