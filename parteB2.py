def salario (horas, antiguedad) -> float:
   
   salario_base = horas * 10

   incremento_antiguedad = salario_base * (0.03 * antiguedad) 

   salario_final = salario_base + incremento_antiguedad
   return salario_final


def productividad (cantidad, horas) -> float: 
   productividad_del_empleado = cantidad / horas 
   return productividad_del_empleado 

def info (name: str, edad: int, salariot, productividadt):
   print (f"nombre: {name}")
   print (f"edad: {edad}")
   print(f"El salario del empleado es: {salariot}")
   print (f" la productividad del empleado es: {productividadt}")

   

name = str (input ("nombre: "))
edad = int (input ("edad: "))
horas = float (input ("horas trabajadas: "))
antiguedad = float (input ("atiguedad: "))
cantidad = float (input ("cantidad de artefactos producidos: "))

salariot = salario (horas, antiguedad)

productividadt = productividad (cantidad, horas)

infot = info (name, edad, salariot, productividadt)