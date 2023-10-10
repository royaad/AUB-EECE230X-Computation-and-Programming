import matplotlib.pyplot as plt
from math import log

n = [i for i in range(2, 31)]
# Log
log_n = [log(x, 2) for x in n]
plt.figure(1)
plt.plot(n, log_n, 'r')
plt.xlabel('n')
plt.ylabel('log_2(n)')
plt.title('Logarithmic Growth')
plt.show()
# Lin
plt.figure(2)
plt.plot(n, n, 'g')
plt.xlabel('n')
plt.ylabel('n')
plt.title('Linear Growth')
plt.show()
# LogLin
loglin_n = [x * log(x, 2) for x in n]
plt.figure(3)
plt.plot(n, loglin_n, 'b')
plt.xlabel('n')
plt.ylabel('n*log_2(n)')
plt.title('Loglinear Growth')
plt.show()
# Quad
n_2 = [x ** 2 for x in n]
plt.figure(4)
plt.plot(n, n_2, 'k')
plt.xlabel('n')
plt.ylabel('n^2')
plt.title('Quadratic Growth')
plt.show()
# Exponential
exp_2 = [2 ** x for x in n]
plt.figure(5)
plt.plot(n, exp_2, 'y')
plt.xlabel('n')
plt.ylabel('2^n')
plt.title('Exponential Growth')
plt.show()