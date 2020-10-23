class Problema:

    metodo = -1
    operacion = ""
    restricciones = []
    tabla = []

    def __init__(self, metodo, objective, restricciones, tabla):
        self.metodo = metodo
        self.operacion = objective
        self.restricciones = restricciones
        self.tabla = tabla

    def propiedades(self):
        print(self.metodo)
        print(self.operacion)
        print(self.restricciones)
        print(self.tabla)

    def get_fila_objetivo(self):
        return self.tabla[0].pop()

    def get_resultados(self):

        resultados = []

        for i in range(len(self.tabla)):
            resultados.append(self.tabla[i][-1])
            i += 1

        return resultados

    def get_matriz_sin_objetivo(self):

        matriz_aux = self.tabla[1:]
        for i, j in enumerate(matriz_aux):
            matriz_aux[i].pop()
        return matriz_aux

    def get_operacion(self):
        return self.operacion

    def get_metodo(self):
        return self.metodo

    def get_tabla(self):
        return self.tabla

    def get_restricciones(self):
        return self.restricciones

    def __str__(self):
        return "Metodo: " + str(self.metodo) + "\n" \
               + "Objective: " + str(self.operacion) + "\n" \
               + "Tabla: " + str(self.tabla)
