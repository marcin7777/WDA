import numpy as np

def siever(n, registery):
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            if j > i and j % i == 0 and j in registery:
                if isinstance(registery, list): registery.remove(j)
                elif isinstance(registery, dict): del registery[j]
                elif isinstance(registery, np.ndarray):
                    registery = np.delete(registery, np.where(registery == j))
            #end if
        #end for
    #end for
            
    return registery
#end siever
