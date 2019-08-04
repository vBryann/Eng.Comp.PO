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


def selection_sort(vetor):
    count = 0
    for i in range(len(vetor)):
        min = i
        for j in range(i + 1, len(vetor)):
            count = count + 1
            if (vetor[min] > vetor[j]):
                min = j


        aux = vetor[i]
        vetor[i] = vetor[min]
        vetor[min] = aux

    return count

def listaInvertida(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam -= 1
    return lista

def desenhaGrafico(x, y, y2,label,label2, name, xl="Entradas", yl="Saídas"):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label)
    ax.plot(x, y2, label=label2)
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


tam = [10000,20000,50000,100000]
time = []
time2 = []
count = []
count2 = []
list = []
list2 = []

#Os indices 2 , referem-se as operações envolvidas a lista invertida


for i in tam:
    list.append(geraLista(i))
    list2.append(listaInvertida(i))

for i in range(len(list)):
    time.append(
        timeit.timeit("selection_sort({})".format(list[i]), setup="from __main__ import selection_sort", number=1))
    count.append(selection_sort(list[i]))
    time2.append(
        timeit.timeit("selection_sort({})".format(list2[i]), setup="from __main__ import selection_sort", number=1))
    count2.append(selection_sort(list2[i]))



desenhaGrafico(tam, time, time2,"Random list time","Inverse list time", "time.png")

desenhaGrafico(tam, count,count2,"Random list iterations","Inverse list iterations","iterations.png")
