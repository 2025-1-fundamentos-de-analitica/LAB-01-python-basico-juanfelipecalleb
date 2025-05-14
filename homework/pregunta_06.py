"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', 'r') as datos:
        dic = {}
        for row in datos:
            col = row.split('\t')[4]
            espe = col.split(',')

            for reg in espe:
                reg = reg.split(':')
                if reg[0] in dic:
                    if dic[reg[0]][0] > int(reg[1]):
                        dic[reg[0]][0] = int(reg[1])

                    if dic[reg[0]][1] < int(reg[1]):
                        dic[reg[0]][1] = int(reg[1])

                else:
                    dic[reg[0]] = [int(reg[1]), int(reg[1])]

        lista = dic.items()
        items = [(d[0], d[1][0], d[1][1]) for d in lista]
        items.sort()

        return items
    