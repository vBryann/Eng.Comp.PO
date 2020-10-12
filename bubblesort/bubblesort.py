from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1, 1 * tam)
        if n not in lista: lista.append(n)
    return lista

mpl.use('Agg')

def bubble_sort(vetor):
    countAux = 0
    for j in range(len(vetor)):
        for i in range((len(vetor) - 1)):
            if vetor[i] > vetor[i + 1]:
                countAux = countAux + 1
                aux=vetor[i]
                vetor[i]=vetor[i+1]
                vetor[i+1]=aux

    return countAux

def desenhaGrafico(x, y, w, name , xl="Entradas", yl="Saídas" ) :
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label= w)
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)

tam = [10000, 20000, 50000, 100000]
time = []
count = []
list = []

for i in tam:
    list.append(geraLista(i))

for i in range(len(list)):
    time.append(timeit.timeit("bubble_sort({})".format(list[i]), setup="from __main__ import bubble_sort", number=1))
    count.append(bubble_sort(list[i]))

desenhaGrafico(tam, time, "Tempo gasto", "time.png")
desenhaGrafico(tam, count, "Número de iterações", "iterations.png")
