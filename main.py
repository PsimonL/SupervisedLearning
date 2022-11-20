import random
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
def StandardDeviation(set, mean):
    counter = 0
    for elem in set:
        counter += (elem - mean) * (elem - mean)
    return sqrt(counter / (len(set) - 1))

def MeanSet(X, y):
    return np.mean(X), np.mean(y)
def PearsonCorrelationCoefficient(n, X, y, meanX, meany):
    tempXY = [((X[j] - meanX) * (y[j] - meany)) for j in range(n)]
    SumTempXY = sum(tempXY)

    tempX = [(X[j] - meanX) ** 2 for j in range(n)]
    SumTempX = sum(tempX)
    tempy = [(y[j] - meany) ** 2 for j in range(n)]
    SumTempy = sum(tempy)

    squaredBottom = sqrt(SumTempX * SumTempy)
    return SumTempXY / squaredBottom
def LinearFunctionCoefficient(X, y, sizeX):
    pass




if __name__ == "__main__":
    # observations / data
    # X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # y = np.array([random.randint(0, 9) for i in range(len(X))])
    X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    meanX, meany = MeanSet(X, y)
    print(meanX, meany)
    deviationX, deviationy  = StandardDeviation(X, meanX), StandardDeviation(y, meany)
    print(deviationX, deviationy)
    R = PearsonCorrelationCoefficient(X.size(), X, y, meanX, meany)
    print(R)

    # coefficient(X, y, np.size(X))
    #
    # print(X)
    # print(y)
