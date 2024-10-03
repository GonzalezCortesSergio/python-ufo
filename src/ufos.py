import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple

Avistaminento = namedtuple("Avistamiento", 
                           "fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud")


def lee_avistamientos(fichero):
    res = []

    with open(fichero, encoding='utf-8') as csvfile:

        lector = csv.reader(csvfile)
        next(lector)

        for x in lector:

            fecha_hora = x[0]
            fecha_hora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistaminento(fecha_hora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)
    
    return res


def duracion_total(registros: list, estado: str):

    duracion = 0

    for registro in registros:

        if(registro.estado.__eq__(estado)):
            duracion+=registro.duracion

    return duracion


def comentario_mas_largo(registros: list, anyo: int, palabra: str):

    registros_anyo_palabra = []
    for registro in registros:

        if(registro.fechahora.year == anyo and registro.comentarios.__contains__(palabra)):

            registros_anyo_palabra.append(registro)
    
    
    comentario = ""

    for registro in registros_anyo_palabra:

        if len(registro.comentarios) > len(comentario):
            comentario = registro.comentarios

    for registro in registros_anyo_palabra:

        if(registro.comentarios.__eq__(comentario)):

            return registro

def indexa_formas_por_mes(registros):

    meses = {"Enero": set(), "Febrero": set(), "Marzo": set(), "Abril": set(), "Mayo": set(), 
             "Junio": set(), "Julio": set(), "Agosto": set(), "Septiembre": set(), "Octubre": set(),
             "Noviembre": set(), "Diciembre": set()}
    
    meses_indice= ["Enero", "Febrero", "Marzo", 
                   "Abril", "Mayo", "Junio", "Julio",
                   "Agosto", "Septiembre", "Octubre", "Noviembre",
                   "Diciembre"]
    
    
    for registro in registros:

        if meses.items()[0].__eq__(meses_indice[registro.fechahora.month - 1]):

            meses[meses_indice[registro.fechahora.month - 1]].add(registro.forma)



    return meses