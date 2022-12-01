#1
import numpy as np
a = np.array([1,1,-1,2,-1,3,1,2,1])
a1 = a.reshape(3,3)
b = np.array([0,9,8])
x = np.linalg.solve(a1,b)
print(x)