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




def mostrar_resultado(monto_original, resultado):
    total_monedas = 0

    print("Monto:", monto_original)
    print("Desglose de monedas:")

    for moneda, cantidad in resultado:
        total_monedas += cantidad

        if moneda == 25:
            nombre = "Q0.25"
        elif moneda == 10:
            nombre = "Q0.10"
        elif moneda == 5:
            nombre = "Q0.05"
        else:
            nombre = "Q0.01"

        print(nombre, ":", cantidad)

    print("Cantidad total de monedas:", total_monedas)


def main():
    monto = input("Ingrese el monto en quetzales. (Ej. 1.01): ")

    monto_centavos = convertir_a_centavos(monto)
    print("Total centavos: ", monto_centavos, "\n")
    
    resultado = hacer_sencillo(monto_centavos)
    print("Listas configuradas: ", resultado, "\n")
    
    mostrar_resultado(monto, resultado)


if __name__ == "__main__":
    main()