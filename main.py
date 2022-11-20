import random
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
def deviation(zbior, srednia):
    licznik = 0
    for elem in zbior:
        licznik += (elem - srednia) * (elem - srednia)
    return sqrt(licznik / (len(zbior) - 1))

def meanSet(X, y):
    return np.mean(X), np.mean(y)

def coefficient(X, y, sizeX):
    pass



if __name__ == "__main__":
    # observations / data
    X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([random.randint(0, 9) for i in range(11)])
    meanX, meany = meanSet(X, y)
    print(meanX, meany)
    # coefficient(X, y, np.size(X))
    #
    # print(X)
    # print(y)
