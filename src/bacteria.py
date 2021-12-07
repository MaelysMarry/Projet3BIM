import numpy as np #import de numpy pour la génération de nombres pseudo-aléatoires
import functions as fc #import du fichier functions.

class bacteria:

    """To describe a bacteria and the function of her evolution

        Attributes
        ----------
        Nm : int
            Limite size of bacteria population.
        Pdeath : int
            Probability for a bacteria to die, without antibiotic effect.
        sensi : int
            Resistance to the antibiotic (absolute value). If 0, bacteria is totally resistante
        Ptol : int
            Probability for the bacteria to become resistante.
        time_tol_max : int
            Number of maximum turn that a bacteria can stop her metabolism
        state : bool
            State of the bacteria. O : bacteria stop her metabolism. 1 : normal metabolism
        time_tol : int
            To count the turn where bacteria stop her metabolism.

    """

#constructeur de l'objet bacteria
    def __init__(self, Nm, Pdeath, sensi, Ptol, time_tol_max, state=1):

        """To initialize bacteria object

            Parameters
            ----------
            Nm : int
                Limite size of bacteria population.
            Pdeath : int
                Probability for a bacteria to die, without antibiotic effect.
            sensi : int
                Resistance to the antibiotic (absolute value). If 0, bacteria is totally resistante
            Ptol : int
                Probability for the bacteria to become resistante.
            time_tol_max : int
                Number of maximum turn that a bacteria can stop her metabolism
            state : bool
                State of the bacteria. O : bacteria stop her metabolism. 1 : normal metabolism
            time_tol : int
                To count the turn where bacteria stop her metabolism.

        """

        self.Nm = Nm #Population limite. Si elle est atteinte, les bactéries cessent de se multiplier
        self.Pdeath = Pdeath #Probabilité de mort basale, sans prendre en compte l'effet de l'antibiotique
        self.sensi = sensi #Sensibilité de la bactérie à l'antibiotique. C'est une valeur absolue. A zéro, la bactérie est complètement résistante à l'antibiotique. 

        if Ptol < 0:
            self.Ptol = 0 #probabilité de devenir tolérante.
        elif Ptol > 1:
            self.Ptol = 1
        else:
            self.Ptol = Ptol

        self.time_tol_max = time_tol_max #nombre de tours consécutifs pendant lesquels la bactérie peut stopper son métabolisme.
        self.state = state  #A 0, la bactérie a stoppé son métabolisme pour être tolérante, à 1 elle est dans son état métabolique normal.
        self.time_tol = 0 #Compteur indiquant le nombre de tours consécutifs pendant lesquels la bactérie tolérante a stoppé son métabolisme.

#Les paramètres de probabilités ont des valeurs comprises entre 0 et 1. On génère un nombre pseudo-aléatoire entre 0 et 1 et si la valeur obtenue est inférieure au paramètre de probabilité, l'événement associé au paramètre est validé.

#événement division 
    def divide(self,N):

        """To know if bacteria divide her

            Parameters
            ----------
            N : int
                Size of population.

            Returns
            -------
            bool
                True if the bacteria divide and False if not divide.

        """
        
        return (self.state == 1 and np.random.random() < fc.Pdi(N, self.Nm, self.Pdeath, 1e-5))
#événement mutation
    def mutate(self, Pmut):

        """To know if bacteria mutate or not

            Parameters
            ----------
            Pmut : int
                Probability of mutation for the bacteria.

            Returns
            -------
            bool
                True if the bacteria mutate and False if not mutate.

        """

        return np.random.random() < Pmut

#événement mort
    def death(self, C):

        """To know if bacteria die or not

            Parameters
            ----------
            C : int
                Concentration of antibiotic.

            Returns
            -------
            bool
                True if the bacteria die and False if not die.

        """

        return np.random.random() < fc.Pde(self.Pdeath, C, self.sensi,
                                           self.state)
#événements liés à la tolérance
    def tolerance(self):

        """To know if bacteria change her tolerance or not

        Note
        ----
        Change state of bacteria object

        """

#la bactérie déclenche l'arrêt de son métabolisme
        if self.state == 1 and np.random.random() < self.Ptol:
            self.state = not self.state
#la bactérie ayant stoppé son métabolisme reste dans cet état
        elif self.state == 0 and self.time_tol < self.time_tol_max:
            self.time_tol += 1
#la bactérie ayant stoppé son métabolisme le réactive
        elif self.state == 0 and self.time_tol >= self.time_tol_max:
            self.state = not self.state
