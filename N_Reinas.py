import random


reina = 'R'


def generar_casillas(dim, num_reinas):
    lista = []

    while len(lista) < num_reinas:
        pos = random.randint(0, dim)

        if pos not in lista:
            lista.append(pos)

    return lista


def generar_tabla(dim, num_reinas):
    tabla = []
    lista_pos = generar_casillas(dim, num_reinas)

    for i in range(dim):
        if i in lista_pos:
            tabla.append(random.randint(1, dim))
        else:
            tabla.append(0)

    return tabla


def generar_poblacion(num_poblacion, dim, num_reinas):
    pob = []

    while len(pob) < num_poblacion:
        pob.append(generar_tabla(dim, num_reinas))

    return pob


def fitness(individuo):
    dim = len(individuo)
    fit = 0

    for i in range(dim):
        if individuo[i] != 0 and (i + 1 < dim - 1):
            for j in range(i + 1, dim):
                if individuo[j] == individuo[i]:
                    fit += 10


def run():
    prob_mutacion = 0.2
    num_poblacion = 100
    num_reinas = 8
    dimension = 8

    poblacion = generar_poblacion(num_poblacion, dimension, num_reinas)
    resuelto = False

    # while not resuelto:

run()