import numpy as np

def n_solutions(n, sc, sfe):
    x = np.linalg.solve(sc, sfe)

    print("Układ posiada rozwiązania: ")
    for i in range(0, n):
        print(round(x[i], 2))
    #end for
#end n_solutions

def no_or_inf_solutions(n, sc, sfe):
    for i in range(0, n):
        W_of_variable = np.copy(sc)
        for j in range(0, n):
            W_of_variable[j, i] = sfe[j]
        #end for
        if np.linalg.det(W_of_variable) != 0: return "Układ sprzeczny"
        #end if
    #end for
    return "Układ nieoznaczony"
#end no_or_inf_solutions
