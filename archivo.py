from problema import Problema

class Archivo:
#lee el archivo de entrada
    @staticmethod
    def leer_archivo(file_name):

        try:

            file = open(file_name, 'r')

            line_count = 0

            method = -1
            objective = ""
            restriccions_array = []
            matrix = []

            for line in file.readlines():
                line = line.strip("\n")
                line_splitted_by_comma = line.split(",")

                if line_count == 0:
                    if line_splitted_by_comma[0].isnumeric():
                        method = int(line_splitted_by_comma[0])

                    if line_splitted_by_comma[1] == "max" or line_splitted_by_comma[1] == "min":
                        objective = line_splitted_by_comma[1]

                    else:
                        raise Exception("Error al procesar el  archivo")

                else:
                    Archivo.leer_linea(line_splitted_by_comma, restriccions_array, matrix, line_count)

                line_count += 1

            matrix[0].append(0)
            return Problema(method, objective, restriccions_array, matrix)

        except:
            print("El archivo no existe o hay un error dentro del mismo.")
#lee las lineas del archivo una por una
    @staticmethod
    def leer_linea(linea, restricciones, matriz, cantidad):

        fila = []

        for i in range(len(linea)):
            if i == (len(linea) - 2) and cantidad > 1:
                if linea[i] == "<=" or linea[i] == ">=" or linea[i] == "=":
                    restricciones.append(linea[i])
                else:
                    return "Símbolo no identificado"
            else:
                if Archivo.is_digit(linea[i]):
                    fila.append(float(linea[i]))

        matriz.append(fila)
#crea el nombre del archivo solucion
    @staticmethod
    def crearNombre(nombre_archivo):
        nombre_sin_extension = (nombre_archivo.split('.')[:-1])[0]
        extension = (nombre_archivo.split('.')[-1:])[0]
        archivo_solucion = nombre_sin_extension + '_solucion.' + extension
        return archivo_solucion
#crea el Archivo nuevo.
    @staticmethod
    def crearArchivo(nombre_archivo, contenido):
        try:
            archivo = open(nombre_archivo, 'a')
            archivo.write(contenido)
            archivo.close()
        except:
            print("ERROR: El archivo no existe.")

    @staticmethod
    def is_digit(n):
        try:
            float(n)
        except ValueError:
            return False
        return True