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

#print(zad4())

#zad5():
#Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”
macierz = np.array([[5,3,8],[-6,1,0]])

a=np.sin(macierz)

#print(a)
#zad6():
#Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
macierz = np.array([[7, 1, -9], [2, -4, -7]])

b = np.cos(macierz)

#print(b)

def zad7(macierz1,macierz2):
#Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
    return macierz1+macierz2

#print(zad7(a,b))

def zad8():
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
    a = np.arange(9).reshape((3,3))
    print(a)
    for b in a:
        print(b)

#zad8()

def zad9():
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())
    a=np.arange(9).reshape((3,3))
    for b in a.flat:
        print(b)

#zad9()

def zad10():
#Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
    a = np.arange(81).reshape((9,9))
    print(a)
    b = a.reshape((27,3))
    print(b)
    c = b.reshape((3,27))
    print(c)
    d = c.reshape((1,81))
    print(d)
    e = d.reshape((81,1))
#mozna zmieniac ksztalt w taki sposob zeby ilosc elementow sie zgadzala,
#zad10()

def zad11():
#Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

    a = np.arange(12)
    b = a.reshape((3,4))
    c = a.reshape((4,3))
    d = a.reshape((2,6))

    print(a)
    print(b)
    print(c)
    print(d)
    print(b.ravel())
    print(c.ravel())
    print(d.ravel())

#wyniki sa takie same
zad11()