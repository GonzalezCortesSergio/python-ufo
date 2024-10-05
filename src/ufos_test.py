from ufos import *

# Test de la función lee_avistamientos

print("Ejercicio 1: ")

for index, avistamiento in enumerate(lee_avistamientos("./data/ovnis.csv")):
    print(avistamiento)

    if index == 5:
        break

print("")
print("")

#Test de la función duracion_total

print("Ejercicio 2: ")

avistamientos = lee_avistamientos("./data/ovnis.csv")
print(f"Duración total de los avistamientos en in: {duracion_total(avistamientos, "in")}")
print(f"Duración total de los avistamientos en nm: {duracion_total(avistamientos, "nm")}")
print(f"Duración total de los avistamientos en pa: {duracion_total(avistamientos, "pa")}")
print(f"Duración total de los avistamientos en wa: {duracion_total(avistamientos, "wa")}")

print("")
print("")
# Test de la función comentario_mas_largo

print("Ejercicio 3: ")

print(comentario_mas_largo(avistamientos, 2005, "ufo"))

print("")
print("")

# Test de la función indexa_formas_por_mes

print("Ejercicio 4: ")

print(indexa_formas_por_mes(avistamientos))
print("")
print("")


# Test de la función avistamientos_fechas

print("Ejercicio 5: ")

print("Mostrando los avistamientos entre el 1 de mayo de 2005 y el 1 de junio de 2005: \n")

print(avistamientos_fechas(avistamientos, datetime(2005, 5, 1), datetime(2005, 6, 1)))

print("")
print("")


# Test de la función hora_mas_avistamientos

print("Ejercicio 6: ")

print(f"Hora en la que se han observado más avistamientos: {hora_mas_avistamientos(avistamientos)}")

print("")
print("")

# Test de la función dicc_estado_longitud_media_comentario

print("Ejercicio 7: ")

print(dicc_estado_longitud_media_comentario(avistamientos))

print("")
print("")

