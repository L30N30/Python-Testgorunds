class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.accionAnterior = -1
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_accion(self, accion):
        self.padre = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def setAccionAnterior(self, accion):
        self.accionAnterior = accion

    def getAccionAnterior(self):
        if self.accionAnterior != None:
            return self.accionAnterior
        else:
            return None

    def __str__(self):
        return str(self.get_estado())


def takeSecond(elem):
    return elem[1]


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
            nuevo_nodo = Nodo()

            if not nuevo_nodo.en_lista(nodos_visitados) and not nuevo_nodo.en_lista(nodos_frontera):
                nodos_frontera.append([nuevo_nodo, 'costo_heuristica'])

            nodo_actual.set_hijo(nuevo_nodo)