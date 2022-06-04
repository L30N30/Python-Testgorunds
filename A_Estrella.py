class Nodo:
    def __init__(self, estado, padre = None, hijo = None, accion = None, costo = 0):
        self.estado = estado
        self.padre = padre
        self.hijo = None
        self.accion = accion
        self.costo = costo
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_datos(self, estado):
        self.estado = estado

    def get_datos(self):
      return self.estado

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo

    def set_accion(self, accion):
        self.accion = accion

    def get_accion(self):
        return self.accion

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_estado() == nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, nodo_lista):
        enlistado = False
        for n in nodo_lista:
            if self.equal(n):
                enlistado = True
        return enlistado

    def expandir(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, accion)
                for accion in problem.acciones(self.estado)]

    def obtenerCamino(self):
        #Retorna la lista de los nodos que conforman el camino desde el nodo inicio al nodo actual.
        nodo, camino_regreso = self, []
        while nodo:
            camino_regreso.append(nodo)
            nodo = nodo.padre
        return list(reversed(camino_regreso))

    def obtenerSolucion(self):
        #Retorna la secuencia de acciones desde el nodo inicio al nodo actual.
        return [nodo.accion for nodo in self.obtenerCamino()[1:]]

    def __str__(self):
        return str(self.get_estado())


def takeSecond(elem):
    return elem[1]


def costo_heuristica(estado):
    return estado[0] + 1


def busqueda_A_Estrella(estado_inicial, solucion, costo):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodo_raiz.set_costo(costo)
    # Se inicializa la lista con él [nodo, costo+heurística]
    nodos_frontera.append([nodo_raiz, 0])

    while (not resuelto) and len(nodos_frontera) != 0:
        nodos_frontera.sort(key=takeSecond)
        nodo_actual = nodos_frontera[0][0]
        nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)

        if nodo_actual.get_estado() == solucion:
            resuelto = True
            return nodo_actual
        else:
            estado_nodo = nodo_actual.get_estado()[:]

            # Acciones para crear nuevos estados
            nuevo_nodo = Nodo([3, 2, 1])

            if not nuevo_nodo.en_lista(nodos_visitados) and not nuevo_nodo.en_lista(nodos_frontera):
                nodos_frontera.append([nuevo_nodo, costo_heuristica(nuevo_nodo.get_estado())])

            nodo_actual.set_hijo(nuevo_nodo)


busqueda_A_Estrella([1, 2, 3], [3, 2, 1], 0)