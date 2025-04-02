# Calcular el precio final y descuento
precio = int(input("Ingrese el precio de su producto:"))
descuento = int(input("Ingrese el porcentaje de descuento:"))

predes = precio * descuento
total = predes/100

precio_descuento = precio - total

iva = int(input("Ingresar porcentaje de IVA:"))

iva = precio_descuento * iva
ivat = iva/100

prec_final = ivat + precio_descuento

print("Precio Original:", precio)
print("Descuento Apliacdo:", descuento)
print("Precio con Descuento", precio_descuento)
print("IVA:", iva)
print("Precio Final Total:", prec_final)