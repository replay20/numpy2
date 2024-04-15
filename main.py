import numpy as np
import random as rand

def zad1():
#Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
    a = np.array([[2,4,3]])
    b = np.array([[5,8,1]])

    return a*b
    #return np.dot(a,b)

print(zad1())