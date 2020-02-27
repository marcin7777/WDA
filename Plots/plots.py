from sympy import Symbol, Interval, Range
from sympy.calculus.util import continuous_domain
import numpy as np
import math
import matplotlib.pyplot as plt

x = Symbol("x")
y = input("Wprowadź wzór funkcji: f(x) = ")
y = eval(y)
x1 = float(input("Podaj początek przedziału: "))
x2 = float(input("Podaj koniec przedziału: "))
domain = continuous_domain(y, x, Interval(x1, x2))
view_range = np.arange(x1, x2 + 0.1, 0.01)
index = 0

for i in view_range:
    view_range[index] = round(view_range[index], 2)
    if i not in domain:
        np.delete(view_range, index)
        index -= 1
    index += 1
#end for

x = view_range
y = eval(str(y))

plt.plot(x, y)
plt.show()
