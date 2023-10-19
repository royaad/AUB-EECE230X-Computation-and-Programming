import timeit
import matplotlib.pyplot as plt
import numpy.random as rand

elapsed_time = []
L = rand.uniform(-1, 1, (100000, ))
n = list(range(1000))

# Testing the sum function
for i in n:
    t0 = timeit.default_timer()
    sum(L[:100*i])
    sumtime = timeit.default_timer() - t0
    elapsed_time.append(sumtime)

plt.plot(n, elapsed_time)
plt.show()