# The goal of this project is to observe evolution of bacteria population when we submit them to an antibiotic. With that we can see antibioresistance of our bacteria population.

## It's develloped by Vincent Le Goff, Maelys Marry and Charles Nodot with the supervision of Guillaume Bellon to the 3BiM project


### Installation
To install you need to clone the github repository.
Also, you need to have several python packages : math, matplotlib, numpy


### TODO
Limitless of the model : Notre modèle nous permet de suivre les valeurs moyennes des paramètres, mais ne nous permet pas de suivre les valeurs des paramètres chez les meilleurs individus.


### An exemple
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

    plt.plot(range(T+1), [results[i][1] for i in range(len(results))])
    plt.plot(range(T+1), [results[i][2] for i in range(len(results))])
    plt.plot(range(T+1), [results[i][3] for i in range(len(results))])
    plt.show()
    
### Link to web page
https://maelysmarry.github.io/Projet3BIM/
