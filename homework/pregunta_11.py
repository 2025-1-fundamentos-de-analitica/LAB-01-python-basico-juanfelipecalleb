"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('files/input/data.csv', 'r') as datos:
        dic = {}

        for row in datos:
            col = row.split('\t')
            espe = col[3].split(',')

            for nu in espe:
                if nu in dic:
                    dic[nu] += int(col[1])
                else:
                    dic[nu] = int(col[1])

        ord = dict(sorted(dic.items()))

        return ord