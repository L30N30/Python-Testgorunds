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


def busqueda_BPPR(nodo_inicial, solucion, visitado):
    visitado.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        # Expandir nodos sucesores (hijos)
        datos_nodo = nodo_inicial.get_estado()
        hijo = [datos_nodo[1], datos_nodo[0], datos_nodo[2], datos_nodo[3]]
        hijo_izquierda = Nodo(hijo)
        hijo = [datos_nodo[0], datos_nodo[2], datos_nodo[1], datos_nodo[3]]
        hijo_centro = Nodo(hijo)
        hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[3], datos_nodo[2]]
        hijo_derecha = Nodo(hijo)
        nodo_inicial.set_hijo([hijo_izquierda, hijo_centro, hijo_derecha])

        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_estado() in visitado:
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, solucion, visitado)
                if Solution is not None:
                    return Solution
        return None


if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = None
    visitado = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_actual = busqueda_BPPR(nodo_inicial, solucion, visitado)

    # Mostrar Resultado
    resultado = []
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)