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

    
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"
             , "Junio", "Julio", "Agosto", "Septiembre", 
             "Octubre", "Noviembre", "Diciembre"]
    
    formas_por_mes = {mes: set() for mes in meses}

    for registro in registros:

        mes = meses[registro.fechahora.month -1]
        formas_por_mes[mes].add(registro.forma)


    return formas_por_mes



def avistamientos_fechas(registros, fecha_inicial, fecha_final):

    reg = []

    if fecha_final == None and fecha_inicial == None:
        return registros
    
    elif (fecha_final == None):

        for registro in registros:

            if registro.fechahora.date() >= fecha_inicial.date():
                reg.append(registro)

    else:

        for registro in registros:

            if registro.fechahora.date() >= fecha_inicial.date() and registro.fechahora.date() <= fecha_final.date():

                reg.append(registro)

    
    return reg


def hora_mas_avistamientos(registros):

    horas = []

    mayor_tamano = 0

    for hora in range(24):
       
        horas.append(hora)

    avistamientos_hora = {hora: set() for hora in horas}

    for registro in registros:
       
        hora = horas[registro.fechahora.hour]
        avistamientos_hora[hora].add(registro)

    
    for hora in horas:

        if avistamientos_hora[hora].__len__() > mayor_tamano:
            mayor_tamano = avistamientos_hora[hora].__len__()
    
    for hora in horas:

        if avistamientos_hora[hora].__len__() == mayor_tamano:

            for avistamiento in avistamientos_hora[hora]:

                return avistamiento.fechahora.hour
            

def dicc_estado_longitud_media_comentario(registros):

    estados = set()

    for registro in registros:

        estados.add(registro.estado)


    estados_registros = {estado: set() for estado in estados}
    
    
    