import numpy as np

# a = np.random.random((20, 20))
# print(np.arange(10))
# print(np.sort(a))

b = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.float64).T
print((b >= 4))
print(b[b >= 4])
print(b[1:2, 2:2])
print(np.sum(b, axis=0))
