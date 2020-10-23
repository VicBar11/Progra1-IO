import sys
from archivo import Archivo
from granm import GranM
from dosfases import DosFases
from simplex import Simplex


def main(argv):

    if len(sys.argv) == 1:
        print("No se recibieron argumentos")
        exit(0)

    elif sys.argv[1] == "-h":
        print("Formato de argumentos inválido")
        print("Formato válido: python3 main.py file.txt")

    else:

        num = -1
        for arg in sys.argv:

            num = num + 1

            if num == 0:
                print("Los archivos a procesar son:" + str(sys.argv[1:]))

            elif num > 0 and arg.endswith('.txt'):

                try:
                    print("Archivo" + str(num) + ":" + str(arg))
                    problem = Archivo.leer_archivo(arg)

                    # 0=Simplex, 1=GranM, 2=DosFases
                    if problem.metodo == 0 or problem.metodo == "simplex":
                        try:
                            simplex = Simplex(problem, arg)
                            simplex.setup()
                            simplex.solucion()
                        except:
                            return "Error al ejecutar simplex"

                    elif problem.metodo == 1 or problem.metodo == "granm":
                        try:
                            big_m = GranM(problem, arg)
                            big_m.setup()
                            big_m.solucion()
                        except:
                            return "Error al ejecutar Gran M"

                    elif problem.metodo == 2 or problem.metodo == "dosfases":
                        try:
                            two_phases = DosFases(problem, arg)
                            two_phases.solve()
                            two_phases.solucion()

                        except:
                            print("error")
                            return "Error al ejecutar Dos fases"

                except:
                    print("El archivo presenta un problema")

if __name__ == '__main__':
    main(sys.argv[1:])
