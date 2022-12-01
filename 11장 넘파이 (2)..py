import numpy as np
a = np.array([1,2,3], dtype = 'int32')
b = np.array([4,5,6], dtype = 'int64')

print(a.dtype)
print(b.dtype)

c = a + b
print(c.dtype)