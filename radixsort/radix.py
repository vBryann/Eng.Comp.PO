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


def count_sort(tam, exp1):
    n = len(tam)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (tam[i] // exp1)
        count[(index) % 10] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (tam[i] // exp1)
        output[count[(index) % 10] - 1] = tam[i]
        count[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(tam)):
        tam[i] = output[i]




def radix_sort(tam):

    max1 = max(tam)
    exp = 1
    while max1 // exp > 0:
        count_sort(tam, exp)
        exp *= 10

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
        timeit.timeit("radix_sort({})".format(lista), setup="from __main__ import radix_sort", number=1))

    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, time,"Lista aleatória", "tempo.png")
