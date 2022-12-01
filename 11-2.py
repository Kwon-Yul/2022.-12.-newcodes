#1.
import numpy as nd
a = nd.array([23,45,67,7,2,30,34,82])
print(a.max())
print(a.min())
print(a.mean())

#2.
b = nd.random.randint(0,99, size = 10)
print(b.max())
print(b.min())
print(b.mean())

#3.
c = nd.append(a,b)
print(c)
