import numpy as np

rand_a = np.random.rand(2, 5)
print(rand_a)
print()

rand_b = np.random.rand(1, 5) * 100
print(rand_b)
print()

rand_c = np.vstack((rand_a, rand_b))
print(rand_c)
print()

rand_c = np.hstack((rand_a, np.random.rand(2, 1)))
print(rand_c)
print()

X = rand_c[:, 2]
print(X)
print()


a = 3
b = 8
y = a * X + b
print(y)
print()

X = np.random.randint(low=0, high=10, size=10)
print(X)
print()

X = X * 10
print(X)
print()

idx = np.random.choice(X.shape[0], size=3, replace=False)
print(X)
print(idx)
print(X[idx])