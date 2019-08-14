import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint,shuffle

mpl.use('Agg')

def listaInvertida(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def part(lista,inicio,fim):
    pivo = randint(inicio, fim)

    lista[fim], lista[pivo] = lista[pivo], lista[fim]

    pivo_index = inicio - 1
    for index in range(inicio, fim):
        if lista[index] < lista[fim]:
            pivo_index = pivo_index + 1
            lista[pivo_index], lista[index] = lista[index], lista[pivo_index]

    temp = lista[pivo_index + 1]
    lista[pivo_index + 1] = lista[fim]
    lista[fim] = temp

    return pivo_index + 1

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        pivo = randint(inicio, fim)
        temp = lista[fim]
        lista[fim] = lista[pivo]
        lista[pivo] = temp

        p = part(lista, inicio, fim)
        quick_sort(lista, inicio, p - 1)
        quick_sort(lista, p + 1, fim)

def desenhaGrafico(x, y,label, name, xl="Entradas", yl="Saídas"):

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
    lista = listaInvertida(tam[i])

    time.append(
        timeit.timeit("quick_sort({},{},{})".format(lista, 0 ,len(lista)-1), setup="from __main__ import quick_sort", number=3))


    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, time,"Melhor Tempo", "tempo.png")
