def realizarDescuento(valor):
    descuento = valor * 0.05
    valor_con_descuento = valor - descuento
    return valor_con_descuento

numero1 = float(input("Ingrese un número entre 10 y 100: "))
while numero1 < 10 or numero1 > 100:
    print ("numero incumplio reglas establecidas")
    numero1 = float(input("Ingrese un número entre 10 y 100: "))

resultado = realizarDescuento(numero1)
print(f"El valor con un descuento del 5% es: {resultado}")