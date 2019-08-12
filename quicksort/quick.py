import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')

def listaInvertida(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam -= 1
    return lista

def part(tam,inicio,fim):
    i = (inicio - 1)
    x = tam[fim]

    for j in range(inicio, fim):
        if tam[j] <= x:
            i = i + 1
            tam[i], tam[j] = tam[j], tam[i]

    tam[i + 1], tam[fim] = tam[fim], tam[i + 1]
    return (i + 1)

def quick_sort(lista, inicial, final):
    tamanho = final - inicial + 1
    pilha = [0] * (tamanho)
    topo = -1
    topo = topo + 1
    pilha[topo] = inicial
    topo = topo + 1
    pilha[topo] = final

    while topo >= 0:
        final = pilha[topo]
        topo = topo - 1
        inicial = pilha[topo]
        topo = topo - 1
        pivo = part(lista, inicial, final)

        if pivo - 1 > inicial:
            topo = topo + 1
            pilha[topo] = inicial
            topo = topo + 1
            pilha[topo] = pivo - 1

        if pivo + 1 < final:
            topo = topo + 1
            pilha[topo] = pivo + 1
            topo = topo + 1
            pilha[topo] = final


def desenhaGrafico(x, y,label, name, xl="Size", yl="Time"):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label)
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


tam = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []



for i in range(len(tam)):
    lista = listaInvertida(tam[i])
    time.append(
        timeit.timeit("quick_sort({},{},{})".format(lista, 0 ,len(lista)-1), setup="from __main__ import quick_sort", number=1))


    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, time,"Inverse list time", "time.png")
