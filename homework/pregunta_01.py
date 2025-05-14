"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    acum = 0

    with open('files/input/data.csv', 'r') as datos:

        for line in datos:
            columnas = line.split('\t')
            acum += int(columnas[1])
    return acum