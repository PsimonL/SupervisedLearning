import random
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt


class Regression_Linear:
    def __init__(self, deviationX, deviationy, meanX, meany, R):
        self.deviationX = deviationX
        self.deviationy = deviationy
        self.meanX = meanX
        self.meany = meany
        self.R = R

def StandardDeviation(set, mean):
    counter = 0
    for elem in set:
        counter += (elem - mean) * (elem - mean)
    return sqrt(counter / (len(set) - 1))

def Pearson(X, y):
    n = len(X)
    meanX = np.mean(X)
    meany = np.mean(y)
    tempXY = [((X[j] - meanX) * (y[j] - meany)) for j in range(n)]
    SumTempXY = sum(tempXY)

    tempX = [(X[j] - meanX) ** 2 for j in range(n)]
    SumTempX = sum(tempX)
    tempy = [(y[j] - meany) ** 2 for j in range(n)]
    SumTempy = sum(tempy)

    squaredBottom = sqrt(SumTempX * SumTempy)
    return SumTempXY / squaredBottom
def LinearFunctionCoefficient(x):
    # y = ax + b
    # a = R * (deviationy / deviationX)
    # b = meany - (a * meanX)
    a = obj.R * (obj.deviationy / obj.deviationX)
    b = obj.meany - (a * obj.meanX)
    return a * x + b




if __name__ == "__main__":
    X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2, 1, 1, 6, 9, 4, 1, 6, 8, 10, 12])
    # X = np.array([1, 2, 3, 4, 5])
    # y = np.array([4, 6, 9, 11, 18])
    deviationX, deviationy  = StandardDeviation(X, np.mean(X)), StandardDeviation(y, np.mean(y))
    R = Pearson(X, y)
    obj = Regression_Linear(deviationX, deviationy, np.mean(X), np.mean(y), R)
    print(obj.meanX)
    print(obj.meany)
    print(obj.deviationX)
    print(obj.deviationy)
    print(obj.R)

    x = np.linspace(min(X), max(X), 30)
    print(x)
    plt.scatter(X, y)
    plt.plot(x, LinearFunctionCoefficient(x), 'r', label='Linear Regression')
    plt.xlabel('OX')
    plt.ylabel('OY')
    plt.legend()
    plt.show()

