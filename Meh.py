class individuo:
    def __init__(self, estado, funcion_suma=None):
        self.estado = estado
        self.funcion_suma = funcion_suma

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_funcion_suma(self, funcion_suma):
        self.funcion_suma = funcion_suma

    def get_funcion_suma(self):
        suma = self.funcion_suma(self.estado)
        return suma


def suma(array_numeros):
    suma = 0
    for i in array_numeros:
        suma += int(i)
    return suma


def run():
    estado1 = [1, 1, 1, 1, 2]
    individuo1 = individuo(estado1, suma)

    print(individuo1.get_funcion_suma())


run()