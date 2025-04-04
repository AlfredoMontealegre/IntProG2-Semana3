# Calcula el salario neto de un empleado
salariobrut = int(input("Ingrese su salario bruto:"))
impuesto = salariobrut * 0.10
seg_soc = salariobrut * 0.05
pensc = salariobrut * 0.03

egresos = (impuesto + seg_soc + pensc)
salario = salariobrut - egresos
print("Tu Salario Neto es:", salario)