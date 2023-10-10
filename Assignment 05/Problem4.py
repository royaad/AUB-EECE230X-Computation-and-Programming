import numpy.random as rand
import matplotlib.pyplot as plt
from math import pi

def monteCarloPiApproximation(N):
    
    # Number of points in the cirlce
    m = 0
    # Approximation of pi
    approximatePi = []
    for i in range(N):
        x = rand.uniform(-1, 1)
        y = rand.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            m += 1
        approximatePi.append(4*m/(i+1))
    return approximatePi

N = 10000

x = [i for i in range(N)]
y = monteCarloPiApproximation(N)
error = [abs(i - pi) for i in y]

plt.subplot(2,1,1)
plt.plot(x, y, 'r', label = 'approximation')
plt.plot([0, N], [pi, pi], 'k', label = 'pi')
plt.legend()
plt.xlabel('n')
plt.subplot(2,1,2)
plt.plot(x, error, 'k')
plt.yscale('log')
plt.ylabel('Absolute value of\napproximation error')
plt.xlabel('n')
plt.show()