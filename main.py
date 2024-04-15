import numpy as np
import random as rand

def zad1():
#Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
    a = np.array([[2,4,3]])
    b = np.array([[5,8,1]])

    return a*b
    #return np.dot(a,b)

#print(zad1())

def zad2():
#Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

    a = np.arange(16).reshape((4,4))
    b = np.arange(9).reshape((3,3))

    print(a.min(axis=0))
    print(a.min(axis=1))
    print(b.min(axis=0))
    print(b.min(axis=1))

#zad2()

def zad3():
#Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
    a = np.array([[2, 4, 3]])
    b = np.array([5, 8, 1])

    print(np.dot(a,b))

#zad3()

def zad4():
#Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia
    a=np.arange(3,dtype=int).reshape((1,3))
    b=np.arange(3,dtype=float).reshape((1,3))

    print(a)
    print(b)

    return a*b

print(zad4())