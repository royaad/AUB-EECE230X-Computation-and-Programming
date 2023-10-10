import matplotlib.pyplot as plt
from math import log

n = [i for i in range(2, 31)]
# Log
log_n = [log(x, 2) for x in n]
plt.plot(n, log_n, 'r')
# Lin
plt.plot(n, n, 'g')
# LogLin
loglin_n = [x * log(x, 2) for x in n]
plt.plot(n, loglin_n, 'b')
# Quad
n_2 = [x ** 2 for x in n]
plt.plot(n, n_2, 'k')
# Exponential
exp_2 = [2 ** x for x in n]
plt.plot(n, exp_2, 'y')
plt.xlabel('n')
plt.title('All on the same figure')
plt.yscale('log')
plt.show()