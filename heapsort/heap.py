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


def sort(arr, n, i):
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        maior = l

    if r < n and arr[maior] < arr[r]:
        maior = r

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        sort(arr, n, maior)




def heap_sort(tam):
    n = len(tam)


    for i in range(n, -1, -1):
        sort(tam, n, i)


    for i in range(n - 1, 0, -1):
        tam[i], tam[0] = tam[0], tam[i]
        sort(tam, i, 0)

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
        timeit.timeit("heap_sort({})".format(lista), setup="from __main__ import heap_sort", number=1))

    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, time,"Lista aleatória", "tempo.png")
