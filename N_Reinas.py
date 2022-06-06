import random


reina = 'R'


def generar_casillas(dim, num_reinas):
    lista = []

    while len(lista) < num_reinas:
        pos = [random.randint(0, dim-1), random.randint(0, dim-1)]

        if pos not in lista:
            lista.append(pos)

    return lista


def generar_tabla(dim, num_reinas):
    tabla = []
    lista_pos = generar_casillas(dim, num_reinas)
    cont = 0

    for i in range(dim):
        columna = []

        for j in range(dim):
            isReina = False

            for k in lista_pos:
                if k[0] == i and k[1] == j:
                    isReina = True

            if isReina:
                columna.append(reina)
                cont += 1
            else:
                columna.append('')

        tabla.append(columna)

    return tabla


def generar_poblacion(num_poblacion, dim, num_reinas):
    pob = []

    while len(pob) < num_poblacion:
        pob.append(generar_tabla(dim, num_reinas))

    return pob


def fitness(individuo):
    dim = len(individuo[0])
    print(dim)


def run():
    prob_mutacion = 0.2
    num_poblacion = 100
    num_reinas = 8
    dimension = 8

    poblacion = generar_poblacion(num_poblacion, dimension, num_reinas)
    resuelto = False
    print(poblacion)
    fitness(poblacion[0])

    #while not resuelto:
        #print('a')


run()