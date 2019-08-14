import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint,shuffle

mpl.use('Agg')

def listaInvertida(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def part(tam,inicial,final):
    pivo = randint(inicial, final)

    tam[final], tam[pivo] = tam[pivo], tam[final]

    pivo_index = inicial - 1
    for index in range(inicial, final):
        if tam[index] < tam[final]:
            pivo_index = pivo_index + 1
            tam[pivo_index], tam[index] = tam[index], tam[pivo_index]

    temp = tam[pivo_index + 1]
    tam[pivo_index + 1] = tam[final]
    tam[final] = temp

    return pivo_index + 1

def quick_sort(tam, inicial, final):
    if inicial < final:
        pivo = randint(inicial, final)
        temp = tam[final]
        tam[final] = tam[pivo]
        tam[pivo] = temp

        p = part(tam, inicial, final)
        quick_sort(tam, inicial, p - 1)
        quick_sort(tam, p + 1, final)

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
