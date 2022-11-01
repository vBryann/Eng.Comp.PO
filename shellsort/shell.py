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

def shell_sort(tam):
    n = len(tam)
    pivo = n // 2

    while pivo > 0:

        for i in range(pivo, n):
            temp = tam[i]
            j = i
            while j >= pivo and tam[j - pivo] > temp:
                tam[j] = tam[j - pivo]
                j -= pivo
            tam[j] = temp
        pivo //= 2


def desenhaGrafico(x, y,label, name, xl="Tamanho da Lista", yl="Tempo"):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label )
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


tam = [100000, 200000, 400000, 500000, 1000000, 2000000]
timeAll = []

for i in range(len(tam)):
    lista = listaAleatoria(tam[i])
    timeAll.append(
        timeit.timeit("shell_sort({})".format(lista), setup="from __main__ import shell_sort", number=1))

    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, timeAll,"Lista aleatória", "tempo.png")
