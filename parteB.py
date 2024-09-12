def valor_exportaciones (valor_exp, retenciones = 15) -> float:
    resultado_exportaciones = valor_exp* (1 - (retenciones / 100))
    return resultado_exportaciones

def valor_ventas_nacionales (nacional, iva = 21) -> float:
    resultado_nacional = nacional* (1 / (1 + (iva / 100)))
    return resultado_nacional

def calculo_impuestos(resultado_nacional, resultado_exportaciones) -> float:
    resultado_final = resultado_nacional + resultado_exportaciones
    print(f"El resultado final después de aplicar IVA y retenciones es: {resultado_final}")


valor_exp = float(input("Ingrese el valor de las exportaciones: "))
nacional = float(input("Ingrese el valor de las ventas nacionales: "))

exp = valor_exportaciones (valor_exp)

nac = valor_ventas_nacionales (nacional)

total = calculo_impuestos (exp, nac)





