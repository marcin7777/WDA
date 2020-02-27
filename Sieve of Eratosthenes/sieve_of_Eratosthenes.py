import numpy as np
import time
from sieve_mechanism import siever

n = int(input("Podaj ostatnią liczbę naturalną przedziału: "))

if n <= 2: print("Granica przedziału musi być większa bądź równa 2!")
else:
    sieve_list = list(range(2, n + 1))
    sieve_dictionary = {i : '' for i in range(2, n + 1)}
    sieve_numpy_array = np.array([i for i in range(2, n + 1)])

    start = time.time()
    siever(n, sieve_list)
    end = time.time()
    print("Algorytm przy użyciu listy wykonany w czasie %d s" % (end - start))

    start = time.time()
    siever(n, sieve_dictionary)
    end = time.time()
    print("Algorytm przy użyciu słownika wykonany w czasie %d s" % (end - start))

    start = time.time()
    siever(n, sieve_numpy_array)
    end = time.time()
    print("Algorytm przy użyciu tablicy z biblioteki numpy wykonany w czasie %d s\n" % (end - start))

    print("Lista liczb pierwszych w zadanym przedziale:")
    print(sieve_list)
#end if
