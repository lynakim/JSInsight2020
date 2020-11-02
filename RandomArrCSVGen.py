import numpy as np
sum = 100
n = 10
rnd_array = np.random.multinomial(sum, np.ones(n)/n, size=10000)
print(rnd_array[0])
print(np.shape(rnd_array))
np.savetxt("/Users/hangyullynakim/Desktop/Random10digits.csv", rnd_array, delimiter=",")
