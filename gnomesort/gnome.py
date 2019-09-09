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


def gnome_sort(lista):
    tam = len(lista)
    pivo = 0
    while pivo < tam:
        if pivo == 0:
            pivo = pivo + 1
        if lista[pivo] >= lista[pivo - 1]:
            pivo = pivo + 1
        else:
            aux = lista[pivo]
            lista[pivo] = lista[pivo-1]
            lista[pivo-1] = aux
            pivo = pivo - 1
    return lista

def desenhaGrafico(x, y,label, name, xl="Tamanho da Lista", yl="Tempo"):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label )
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


tam = [10000, 20000, 40000, 50000, 100000, 200000]
time = []

for i in range(len(tam)):
    lista = listaAleatoria(tam[i])
    time.append(
        timeit.timeit("gnome_sort({})".format(lista), setup="from __main__ import gnome_sort", number=1))

    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, time,"Lista aleatória", "tempo.png")
