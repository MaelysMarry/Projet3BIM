from math import exp

#Fonction probabilité de division
def Pdi(N, Nm, Pde, r):

    """To calculate the division probability

            Parameters
            ----------
            N : int
                Size of population
            Nm : int
                Limite size of bacteria population.
            Pde : int
                Probability for a bacteria to die, without antibiotic effect.
            r : int
                Why not

            Returns
            -------
            (1-a)/(1-a*exp(r*N)) : int
                Division probability      

    """

    # print(N)
    # print(exp(r*Nm))

    a = (Pde-1)/(Pde*exp(r*Nm)-1)
    return (1-a)/(1-a*exp(r*N))

#Autre fonction probabilité de division non utilisée
def Pdi2(N, Nm, Pde):

    """To calculate the division probability

            Parameters
            ----------
            N : int
                Size of population.
            Nm : int
                Limite size of bacteria population.
            Pde : int
                Probability for a bacteria to die, without antibiotic effect.

            Returns
            -------
            Pde*(1+(Nm-N)/Nm) : int
                Division probability      

    """

    return Pde*(1+(Nm-N)/Nm)

#Probabilité de mort générale. Une bactérie tolérante qui a stoppé son métabolisme ne sera pas affectée par l'antibiotique. 
def Pde(Pdeath, C, s, state):

    """To calculate the division probability

            Parameters
            ----------
            Pdeath : int
                Probability for a bacteria to die, without antibiotic effect.
            C : int
                Concentration of antibiotic.
            s : int
                Resistance to the antibiotic (absolute value). If 0, bacteria is totally resistante
            state : bool
                State of the bacteria. O : bacteria stop her metabolism. 1 : normal metabolism

            Returns
            -------
            Pdeath+abs(s)*C*state : int
                probability for a bacteria to die naturally      

    """

    return Pdeath+abs(s)*C*state