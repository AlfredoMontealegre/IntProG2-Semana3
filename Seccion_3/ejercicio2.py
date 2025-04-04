# Leer x cantidad de producto comprado a x precio
# Aplica el IVA  del 15%
# Un descuento del 10
# Mostrar el Total antes del IVA
# Monto del IVA
# Monto del Descuento
# Total a Pagar

""" Se debe leer el nombre del cliente, nombre del producto y mostrar una factura """
print("="*20)
print("Sistema de Facturacion")
print("="*20)
print("Ingresa los siguientes datos: ")
cliente = input("Nombre del Cliente: ")
producto = input("Nombre del Producto: ")
precio = float(input("Precio del Producto: "))
cantidad = float(input("Cantidad del Producto: "))

total = precio * cantidad
iva = total * 0.15
descuento = total * 0.10

monto = total + iva - descuento

import os
press_key = input("Presiona una tecla para continuar...")
os.system ("cls || clear")
print("+"*30)
print("Factura ")
print("+"*30)
print(f"Cliente: {cliente}")
print("Productos \t Cantidad \t Precio \t Total")
print(f"{producto:>10} {cantidad:>12} {precio:>12} {total:>12}")
print(f"IVA: {iva}")
print(f"Desc: {descuento}")
print(f"Monto: {monto}")


