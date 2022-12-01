# 0에서 9까지의 정수 값을 가지는 ndarray 객체 a를 넘파이를 이용하여 작성하여 출력하기
import numpy as nd
a = nd.array([0,1,2,3,4,5,6,7,8,9])
b = nd.array(range(0,10))
c = nd.array(range(0,10,2),dtype = 'int64')
print(a)
print(b)
print(c)
print('c.shape = ',c.shape)
print('c.ndim = ',c.ndim)
print('c.dtype = ',c.dtype)
print('c.size = ',c.size)
print('c.itemsize = ',c.itemsize)