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



def main():
    monto = input("Ingrese el monto en quetzales. Ejemplo 2.93: ")

    monto_centavos = convertir_a_centavos(monto)
    print(monto_centavos)


if __name__ == "__main__":
    main()