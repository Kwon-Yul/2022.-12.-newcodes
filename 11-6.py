#1.
import numpy as np
a = np.random.randint(1,100, size = 15)
b = a.reshape(3,5)
print(b)
#2.
print(b.min(axis = 0))
print(b.max(axis = 0))
print(b.mean(axis = 0))
#3
print(b.min(axis = 1))
print(b.max(axis = 1))
print(b.mean(axis = 1))
