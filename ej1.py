def convertir_a_centavos(monto):
    partes = monto.strip().split(".")

    if len(partes) == 1:
        quetzales = int(partes[0])
        centavos = 0
    else:
        quetzales = int(partes[0])
        centavos_texto = partes[1]

        if len(centavos_texto) == 1:
            centavos_texto += "0"
        elif len(centavos_texto) > 2:
            centavos_texto = centavos_texto[:2]

        centavos = int(centavos_texto)

    return quetzales * 100 + centavos


def hacer_sencillo(monto_centavos):
    monedas = [25, 10, 5, 1]
    resultado = []

    restante = monto_centavos

    for moneda in monedas:
        cantidad = restante // moneda
        resultado.append((moneda, cantidad))
        restante = restante % moneda

    return resultado


def main():
    monto = input("Ingrese el monto en quetzales. Ejemplo 2.93: ")

    monto_centavos = convertir_a_centavos(monto)
    #print(monto_centavos)
    
    resultado = hacer_sencillo(monto_centavos)
    print(resultado)
    


if __name__ == "__main__":
    main()