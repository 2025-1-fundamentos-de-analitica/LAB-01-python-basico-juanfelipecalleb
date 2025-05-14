"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('files/input/data.csv', 'r') as datos:
        dic = {}

        for row in datos:
            col = row.split('\t')
            espe = col[4].split(',')
            
            val = 0

            for reg in espe:
                reg = reg.split(':')
                val += int(reg[1])
            

            if col[0] in dic:
                dic[col[0]] += val
            else:
                dic[col[0]] = val

        ord = dict(sorted(dic.items()))

        return ord