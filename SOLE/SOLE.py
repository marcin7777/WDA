import numpy as np
from solver import n_solutions, no_or_inf_solutions

n = int(input("Podaj liczbę równań: "))
coefficients_list = []
right_side = []
system_coefficients = np.empty(n);

for i in range(0, n):
    for j in range(0, n + 1):
        if j != n:
            a = float(input("Podaj %d współczynnik równania %d: " % (j + 1, i + 1)))
            coefficients_list.append(a)
        #end if
        else:
            a = float(input("Podaj wyraz wolny równania %d (po prawej stronie znaku równości): " % (i + 1)))
            right_side.append(a)
        #end else
    #end for
    if i == 0: system_coefficients = np.array(coefficients_list)
    else: system_coefficients = np.vstack([system_coefficients, coefficients_list])
    coefficients_list.clear()
#end for

system_free_expressions = np.array(right_side)

try:
    n_solutions(n, system_coefficients, system_free_expressions)
except np.linalg.LinAlgError:
    print(no_or_inf_solutions(n, system_coefficients, system_free_expressions))
