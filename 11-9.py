#1
import numpy as np
a = np.arange(0,16).reshape(4,4)
print(a)
b = a[:,1]
c = a[2, 1:4]
d = a[0:2,0:2]
e = a[1:3,1:3]
print(b)
print(c)
print(d)
print(e)

#2
f = a[0:2,0:3]
print(f.reshape(1,6))
g = a[2:4,0:4]
print(g.reshape(1,8))
h = a[1:4:2,1:]
print(h.reshape(1,6))