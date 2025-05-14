"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('files/input/data.csv', 'r') as datos:
        dic = {}
        for row in datos:
            col = row.split('\t')[4]
            espe = col.split(',')

            for reg in espe:
                reg = reg.split(':')
                if reg[0] in dic:
                    dic[reg[0]] += 1
                else:
                    dic[reg[0]] = 1


        dic_sort = dict(sorted(dic.items()))

        return dic_sort