import math
import sys

from archivo import Archivo

class Simplex:

    fila_objetivo = []
    resultados = []
    operadores = []
    restricciones = []
    pivotes = []
    problema = None
    archivo = ''

    def __init__(self, problema, nombre_archivo):

        self.problema = problema
        self.archivo = nombre_archivo
        self.fila_objetivo = problema.tabla[0][:-1]
        self.resultados = problema.get_resultados()
        self.operadores = problema.get_restricciones()
        self.restricciones = problema.get_matriz_sin_objetivo()

    def setup(self):

        if str.upper(self.problema.operacion) == "MIN":
            self.fila_objetivo = [-x for x in self.fila_objetivo]

        for i, operation in enumerate(self.operadores):

            if operation == '<=':  # +S
                self.variables(i, 1)
                self.fila_objetivo.append(0)

            else:
                print('ERROR')
                sys.exit(0)

        self.setup_fila_objetivo()

    def setup_fila_objetivo(self):

        self.fila_objetivo = [-x for x in self.fila_objetivo]

    #Rellena por columnas, se encarga de poner la variable en la fila dada y rellena con ceros
    def variables(self, indice, variable):
        for j, row in enumerate(self.restricciones):
            if indice == j:
                row.append(variable)
            else:
                row.append(0)


    def get_columna_pivote(self):
        min_index = 0
        min_item = math.inf

        for index, item in enumerate(self.fila_objetivo):

            if item < min_item:
                min_item = item
                min_index = index

        return min_index

    def get_fila_pivote(self, c):
        min_index = 0
        min_item = math.inf

        for index, row in enumerate(self.restricciones):

            if row[c] > 0:

                if (self.resultados[index + 1] / row[c]) < min_item:
                    min_item = self.resultados[index + 1] / row[c]
                    min_index = index

        return min_index

    def minimizar(self):

        columna_pivote = self.get_columna_pivote()
        fila_pivote = self.get_fila_pivote(columna_pivote)
        valor = self.restricciones[fila_pivote][columna_pivote]

        self.pivotes.append((fila_pivote + 1, columna_pivote))

        # reduce pivot row, pivot value equals to 1
        for k, value in enumerate(self.restricciones[fila_pivote]):
            self.restricciones[fila_pivote][k] = value / valor

        # apply same operation to result array
        self.resultados[fila_pivote + 1] /= valor

        # reduce the rest of the rows to zero
        for i, row in enumerate(self.restricciones):

            if i != fila_pivote:
                aux_value = self.restricciones[i][columna_pivote]

                for j, value in enumerate(self.restricciones[i]):
                    self.restricciones[i][j] = value - (aux_value * self.restricciones[fila_pivote][j])

                # apply same operation to result array
                self.resultados[i + 1] -= (aux_value * self.resultados[fila_pivote + 1])

        aux_value = self.fila_objetivo[columna_pivote]

        # reduce the u row to zero
        for i, value in enumerate(self.fila_objetivo):
            self.fila_objetivo[i] = value - (aux_value * self.restricciones[fila_pivote][i])

        # apply same operation to result array
        self.resultados[0] -= (aux_value * self.resultados[fila_pivote + 1])

    #identifica si ya se solucionó el problema
    def terminado(self):
        for value in self.fila_objetivo:
            if value < 0:
                return False
        return True

    def solucion(self):

        i = 1
        while not self.terminado():
            texto = "I N T E R M E D I A     "+str(i)
            self.imprimir_tabla(texto)
            self.minimizar()
            i+=1

        self.imprimir_tabla("F I N A L")
        self.imprimir_solucion()

    def imprimir_tabla(self,recursion):

        x = Archivo.crearNombre(self.archivo)

        with open(x, 'a') as archivo:

            print('-' * (12 * (len(self.fila_objetivo) + 1)), file=archivo)
            print(' ' * (3 * (len(self.fila_objetivo) + 1)) + "T A B L A     "+recursion, file=archivo)
            print('-' * (12 * (len(self.fila_objetivo) + 1)), file=archivo)

            for value in self.fila_objetivo:
                print('%10.2f,' % value, end='', file=archivo)

            print('%10.2f' % self.resultados[0], file=archivo)

            for i, row in enumerate(self.restricciones):

                for j, value in enumerate(row):
                    print('%10.2f,' % value, end='', file=archivo)

                print('%10.2f' % self.resultados[i + 1], file=archivo)

            print('-' * (12 * (len(self.fila_objetivo) + 1)), file=archivo)
            print("\nLISTA PIVOTES:  " + str(self.pivotes)+"\n", file=archivo)
            print('-' * (12 * (len(self.fila_objetivo) + 1))+"\n", file=archivo)

    def imprimir_solucion(self):

        print('-' * (12 * (len(self.fila_objetivo) + 1)))
        print(' '* (3 * (len(self.fila_objetivo) + 1)) + "T A B L A     S O L U C I O N")
        print('-' * (12 * (len(self.fila_objetivo) + 1)))

        for value in self.fila_objetivo:
            print('%10.2f,' % value, end='')

        print('%10.2f' % self.resultados[0])

        for i, row in enumerate(self.restricciones):

            for j, value in enumerate(row):
                print('%10.2f,' % value, end='')

            print('%10.2f' % self.resultados[i + 1])

        print('-' * (12 * (len(self.fila_objetivo) + 1)))
        print("\nLISTA PIVOTES:  " + str(self.pivotes) + "\n")
        print('-' * (12 * (len(self.fila_objetivo) + 1)))







