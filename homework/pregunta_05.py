"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as datos:

        valores = {}
        for ren in datos:
            columns = ren.split('\t')

            if columns[0] in valores:
                if valores[columns[0]][0] < columns[1]:
                    valores[columns[0]][0] = columns[1]

                if valores[columns[0]][1] > columns[1]:
                    valores[columns[0]][1] = columns[1]

            else:
                valores[columns[0]] = [columns[1], columns[1]]

        lista = valores.items()
        items = [(p[0], int(p[1][0]), int(p[1][1])) for p in lista]
        items.sort()

        return items
    