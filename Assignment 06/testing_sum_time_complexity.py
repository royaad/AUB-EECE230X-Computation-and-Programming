import time
import matplotlib.pyplot as plt
import numpy.random as rand

elapsed_time = []
L = rand.uniform(-1, 1, (1000, ))
n = list(range(8))

# Testing the sum function
for i in n:
    print(i)
    t0 = time.time()
    sum(L[:100*i])
    elapsed_time.append(time.time() - t0)

plt.plot(n, elapsed_time)
plt.show()
