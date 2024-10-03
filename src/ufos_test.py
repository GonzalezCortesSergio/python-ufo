from ufos import *

# Test de la función lee_avistamientos

for index, avistamiento in enumerate(lee_avistamientos("./data/ovnis.csv")):
    print(avistamiento)

    if index == 5:
        break

#Test de la función duracion_total
avistamientos = lee_avistamientos("./data/ovnis.csv")
print(f"Duración total de los avistamientos en in: {duracion_total(avistamientos, "in")}")
print(f"Duración total de los avistamientos en nm: {duracion_total(avistamientos, "nm")}")
print(f"Duración total de los avistamientos en pa: {duracion_total(avistamientos, "pa")}")
print(f"Duración total de los avistamientos en wa: {duracion_total(avistamientos, "wa")}")
# Test de la función comentario_mas_largo

print(comentario_mas_largo(avistamientos, 2005, "ufo"))

# Test de la función avistamientos_fechas

print(indexa_formas_por_mes(avistamientos))

# Test de la función hora_mas_avistamientos









