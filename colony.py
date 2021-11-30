from bacteria import bacteria
import matplotlib.pyplot as plt
import numpy as np
import math as math


class colony:

    """To describe a bacteria and the function of her evolution

        Attributes
        ----------
        Pdeath : int
            Probability for a bacteria to die, without antibiotic effect.
        Nm : int
            Limite size of bacteria population.
        length : int
            Actually size of bacteria population.
        C : int
            Concentration of antibiotic.
        sensi : int
            Resistance to the antibiotic (absolute value). If 0, bacteria is totally resistante
        Ptol : int
            Probability for the bacteria to become resistante.
        time_tol_max : int
            Number of maximum turn that a bacteria can stop her metabolism
        PmutS : int
            Probability for the bacteria to change her sensibility.
        PmutT : int
            Probability for the bacteria to change tolerance.
        sigmaS : int
            Variance of sensibility into the colony.
        sigmaT : int
            Variance of tolerance into the colony.
        pop : list of bacteria
            List of bacteria into the colony.


    """

#constructeur de l'objet colony
    def __init__(self, Pdeath, Nm, length, C, sensi=0, Ptol=0, time_tol_max=0,
                 PmutS=0, PmutT=0, sigmaS=0, sigmaT=0):

        """To initialize bacteria object

            Parameters
            ----------
            Pdeath : int
                Probability for a bacteria to die, without antibiotic effect.
            Nm : int
                Limite size of bacteria population.
            length : int
                Actually size of bacteria population.
            C : int
                Concentration of antibiotic.
            sensi : int
                Resistance to the antibiotic (absolute value). If 0, bacteria is totally resistante
            Ptol : int
                Probability for the bacteria to become resistante.
            time_tol_max : int
                Number of maximum turn that a bacteria can stop her metabolism
            PmutS : int
                Probability for the bacteria to change her sensibility.
            PmutT : int
                Probability for the bacteria to change tolerance.
            sigmaS : int
                Variance of sensibility into the colony.
            sigmaT : int
                Variance of tolerance into the colony.

        """

        self.Pdeath = Pdeath #probabilité de mort naturelle
        self.Nm = Nm #population limite de la colonie
        self.length = length #population actuelle de la colonie
        self.C = C #concentration d'antibiotique
        self.sensi = sensi #sensibilité des bactéries
        self.Ptol = Ptol #probabilité de stopper son métabolisme
        self.time_tol_max = time_tol_max #nombre de tours consécutifs pendant lesquels la bactérie tolérante peut stopper son métabolisme.
        self.PmutS = PmutS #probabilité que la sensibilité de la bactérie change
        self.PmutT = PmutT #probabilité que Ptol varie
        self.sigmaS = sigmaS #variance de la sensibilité au sein de la colonie
        self.sigmaT = sigmaT #variance de la tolérance au sein de la colonie

        self.pop = [] #liste contenant toutes les bactéries de la colonie

#initialisation de la colonie de bactéries
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

        """To change saw the state of population at time t+1

            Note
            ----
            Change pop and C of colony object           

        """

        div = []
        death = []

        for i in self.pop:
#si une bactérie se divise....
            if i.divide(len(self.pop)):
#la nouvelle bactérie peut avoir une sensibilité différente
                if i.mutate(self.PmutS):

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi
                                        + self.sigmaS * np.random.randn(),
                                        i.Ptol,
                                        i.time_tol_max))
#et/ou une autre probabilité de tolérance
                if i.mutate(self.PmutT):

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.Ptol
                                        + self.sigmaT * np.random.randn(),
                                        i.time_tol_max))
#et/ou pouvoir stopper son métabolisme plus longtemps
                if i.mutate(self.PmutT):

                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.Ptol,
                                        int(i.time_tol_max
                                            + np.random.randn())))
                else:
#ou être identique à sa mère
                    div.append(bacteria(i.Nm,
                                        i.Pdeath,
                                        i.sensi,
                                        i.Ptol,
                                        i.time_tol_max))

            i.tolerance()
#la bactérie peut mourir 
            if i.death(self.C):
                death.append(self.pop.index(i))

        death = death[::-1]
#On retire les bactérie mortes de la population de la colonie
        for i in range(len(death)):
            self.pop.pop(death[i])
#On rajoute les bactéries issus de la division à la colonie
        self.pop += div
#La concentration d'antibiotiques baisse au sein de la colonie
        self.C = .75 * self.C

#Fonction pour retourner la taille de la colonie, la sensibilité moyenne, la tolérance moyenne et le temps maximal moyen de tolérance.
    def stats(self):

        """To extract few information of colony object

            Returns
            -------
            len(self.pop) : int
                Size of population
            moyS/(len(self.pop)+1) : int
                Mean sensibility of the colony
            moyT/(len(self.pop)+1) : int
                Mean tolerance of the colony
            moyD/(len(self.pop)+1) : int
                Mean of maximal time in tolerance       

        """

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

#fonction pour lancer la simulation, le paramètre T est le nombre de tours.
    def run(self, T):

        """To turn the simualtion

            Parameters
            ----------
            T : int
                Number of turn

            Returns
            -------
            ret : list of list of int
                List of population size, mean of sensibility, tolerance and maximal time in tolerance for each turn      

        """

        ret = [self.stats()]

        for t in range(T):
            print(t, len(self.pop), self.C)
            # print(self.stats())
            self.updatePop()
            ret.append(self.stats())
#Ajout d'antibiotique tous les 10 tours, de concentration croissante.
            if t % 10 == 0:
                self.C = .2*t
#Arrêt de la simulation en cas de mort totale de la colonie
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
