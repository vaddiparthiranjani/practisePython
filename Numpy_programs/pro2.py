# program to compute sum of all elements, sum of each column and sum of each row of a given array.

import numpy as np

x=np.array([[1,2,3],[3,4,5]])

print(x)

print("sum of all elements ", np.sum(x))
print("sum of each column ", np.sum(x, axis=0))
print("sum of each row ", np.sum(x, axis=1))





