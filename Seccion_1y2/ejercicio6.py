# Calculo del Indice de Masa Corporal
print("Bienvenido al Calculador de IMC")
pesokg = int(input("Ingrese su peso en KG:"))
alturam = int(input("Ingrese su altura en metros:"))

imc = ((alturam * alturam)/pesokg)*100
imctotal = imc/100
print("Peso ingresado:", pesokg)
print("Altura ingresada:", alturam)
print("IMC Calculado:", imctotal)


