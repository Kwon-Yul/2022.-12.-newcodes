#1
import numpy as np
a1 = np.arange(1,13)
print(a1)
print(a1.reshape(2,6))

#2
a2 = np.arange(1,31)
print(a2.reshape(3,10))

#3
a3 = a2.reshape(6,5)
print(a3)

#4
print(np.transpose(a3))