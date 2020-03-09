from math import exp


def Pdi(N, Nm, Pde, r):

    # print(N)
    # print(exp(r*Nm))

    a = (Pde-1)/(Pde*exp(r*Nm)-1)
    return (1-a)/(1-a*exp(r*N))


def Pdi2(N, Nm, Pde):

    return Pde*(1+(Nm-N)/Nm)


def Pde(Pdeath, C, s, state):

    # print(Pdeath+s*C)
    return Pdeath+abs(s)*C*state
