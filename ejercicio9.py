# Calcular Duracion de una pelicula con comerciales
dura_min = int(input("Ingrese la duracion en minutos de la peli:"))
comer_prev = int(input("Ingrese la duracion en minutos de los comerciales:"))
comer_int = int(input("Ingrese la duracion en minutos de las pausas:"))

duratotal = (dura_min + comer_int + comer_prev)

print("Duracion de la pelicula:", dura_min)
print("Duracion total de la proyeccion:", duratotal)