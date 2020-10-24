from simplex import Simplex

class DosFases(Simplex):

    fila_objetivo_aux = []

    def __init__(self, problema, nombre_archivo):
        super().__init__(problema, nombre_archivo)

    def setup_dos_fases(self):

        for i, operation in enumerate(self.operadores):

            if operation == '<=':  # +S
                self.variables(i, 1)
                self.fila_objetivo.append(0)

            elif operation == '>=':  # -E +R
                self.variables(i, -1)
                self.variables(i, 1)
                self.fila_objetivo.append(0)
                self.fila_objetivo.append(0)

            else:  # +R
                self.variables(i, 1)
                self.fila_objetivo.append(0)

    def setup_aux(self):

        indices = []

        self.fila_objetivo_aux = self.fila_objetivo
        self.fila_objetivo = [x - x for x in self.fila_objetivo]

        for i, operador in enumerate(self.operadores):

            if operador == '<=':  # +S
                self.variables(i, 1)
                self.fila_objetivo.append(0)

            elif operador == '>=':  # -S +R
                self.variables(i, -1)
                self.variables(i, 1)
                self.fila_objetivo.append(0)
                self.fila_objetivo.append(-1)
                indices.append(len(self.fila_objetivo) - 1)

            else:  # +R
                self.variables(i, 1)
                self.fila_objetivo.append(-1)
                indices.append(len(self.fila_objetivo) - 1)

        return indices
    #Busca la fila con el indice igual a 1
    def buscar_fila(self, indice):

        for i, fila in enumerate(self.restricciones):
            if fila[indice] == 1:
                return i

    def solve(self):

        #I fase, se calcula la nueva función objetivo
        indices = self.setup_aux()

        for i, columna in enumerate(indices):
            fila = self.buscar_fila(columna)

            for j, valor in enumerate(self.restricciones[fila]):
                self.fila_objetivo[j] += valor

            self.resultados[0] += self.resultados[fila + 1]

        self.fila_objetivo = [-x for x in self.fila_objetivo]
        self.resultados[0] *= -1

        self.solucion()

        self.fila_objetivo = self.fila_objetivo_aux
        self.setup_fila_objetivo()

        #Contador de reducciones en la columna
        cont = 0

        for columna in indices:

            for fila in self.restricciones:
                fila.pop(columna - cont)

            cont += 1
