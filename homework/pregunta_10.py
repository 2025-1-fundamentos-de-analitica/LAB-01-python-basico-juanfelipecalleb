"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    with open('files/input/data.csv','r') as datos:

        lista = []
        for row in datos:

            columns = row.split('\t')

            letra = columns[0]
            el1 = columns[3].split(',')
            el2 = columns[4].split(',')

            tupl = (letra, len(el1), len(el2))
            lista.append(tupl)

        return lista
    