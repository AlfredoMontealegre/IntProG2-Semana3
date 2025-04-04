# Calcula el volumen del cilintro
radio = int(input("Ingrese el radio de un cilindro:"))
altura = int(input("Ingrese la altura del cilindro:"))

areabase = ((radio * radio ) * 3.1416)
volumen = (areabase * altura)

arealat = (2 * (3.1416 * radio * altura))
areasuf = (arealat + (2 * areabase))

print("Radio Ingresado:", radio)
print("Altura Ingresado:", altura)
print("Volumen:", volumen)
print("Area Superficial:", areasuf)