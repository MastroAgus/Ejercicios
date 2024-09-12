# Función que muestra por pantalla el número que recibe como parámetro.
def mostrar_numero(numero):
    print(f"El número es: {numero}")

# Función que determina si un número es par o no.
# Retorna True si el número es par y False si no lo es.
def es_par(numero):
    return numero % 2 == 0

# Función que muestra el número si está en el rango especificado.
# Valida si el número está entre 'desde' y 'hasta' inclusive.
def mostrar_numero_en_rango(numero, desde, hasta):
    if desde <= numero <= hasta:
        print(f"El número {numero} está en el rango ({desde}, {hasta}).")
    else:
        print(f"El número {numero} NO está en el rango ({desde}, {hasta}).")

# Programa principal
# Probar la función 'mostrar_numero'
mostrar_numero(10)

# Probar la función 'es_par'
numero = 8
if es_par(numero):
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Probar la función 'mostrar_numero_en_rango'
mostrar_numero_en_rango(15, 10, 20)
mostrar_numero_en_rango(25, 10, 20)




