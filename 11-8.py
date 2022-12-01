#q
import numpy as np
a = np.arange(0,24).reshape(4,3,2)
print('  index  |  element')
for i in range (0,4):
    for j in range(0,3):
        for k in range(0,2):
            print('({},{},{})  | '.format(i,j,k),a[i,j,k])


#2
b = np.concatenate((a[0,0],a[1,0]),axis = 0)
print(b)

c = np.concatenate((a[0,0],a[2,1]),axis = 0)
print(c)

d = np.concatenate((a[0],a[1]),axis=0)
print(d)

e = np.concatenate((a[0,0],a[1,0],a[0,1],a[1,1],a[0,2],a[1,2]),axis=0)
print(e.reshape(3,4))