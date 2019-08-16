import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def listaInvertida(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def listaAleatoria(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista

def merge_sort(tam):
    if len(tam) > 1:
        mid = len(tam) // 2
        L = tam[:mid]
        R = tam[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tam[k] = L[i]
                i += 1
            else:
                tam[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            tam[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tam[k] = R[j]
            j += 1
            k += 1



def desenhaGrafico(x, y,label, name, xl="Tamanho da Lista", yl="Tempo"):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label )
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


tam = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []

for i in range(len(tam)):
    lista = listaAleatoria(tam[i])
    time.append(
        timeit.timeit("merge_sort({})".format(lista), setup="from __main__ import merge_sort", number=1))

    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, time,"Lista aleatória", "tempo.png")
