def realizar_operacion (num1,num2,ope):
    if ope == "s":
        return num1 + num2
    elif ope == "r":
        return num1 - num2
    
num1 = float (input ("seleccione numero 1 entre 10 y 100: "))
while num1 < 10 or num1 > 100:
    print ("numero incumplio reglas establecidas")
    num1 = float(input("Ingrese un número entre 10 y 100: "))

num2 = float (input ("seleccione numero 2 entre 10 y 100: "))
while num2 < 10 or num2 > 100:
    print ("numero incumplio reglas establecidas")
    num2 = float(input("Ingrese un número entre 10 y 100: "))

ope = input("Ingrese la operación ('s' para sumar, 'r' para restar)")

resultado = realizar_operacion (num1, num2, ope)
print (f"el resultado entre {num1} {ope} {num2} es {resultado}")

