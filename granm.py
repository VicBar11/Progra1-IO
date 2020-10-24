from archivo import Archivo
from simplex import Simplex


class GranM(Simplex):
    M = 10000

    def __init__(self, problema, archivo):
        super().__init__(problema, archivo)

    def setup(self):

        if str.upper(self.problema.operacion) == "MIN":
            self.fila_objetivo = [-x for x in self.fila_objetivo]

        for fila_actual, operacion in enumerate(self.operadores):

            if operacion == '<=':  # +S
                self.variables(fila_actual, 1)
                self.fila_objetivo.append(0)

            elif operacion == '>=':  # +R -S

                r_column = len(self.restricciones[fila_actual])
                self.variables(fila_actual, 1)
                self.variables(fila_actual, -1)
                self.fila_objetivo.append(0)
                self.fila_objetivo.append(0)
                self.add_artificiales(fila_actual, r_column)

            else:  # +R

                r_column = len(self.restricciones[fila_actual])
                self.variables(fila_actual, 1)
                self.fila_objetivo.append(0)
                self.add_artificiales(fila_actual, r_column)

        self.setup_fila_objetivo()
    #agrega las las variables artificiales.
    def add_artificiales(self, i, j):

        self.resultados[0] += -self.M * self.resultados[i + 1]

        for k, valor in enumerate(self.restricciones[i]):
            if k != j:
                self.fila_objetivo[k] += self.M * valor

