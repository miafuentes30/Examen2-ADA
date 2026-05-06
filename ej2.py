def calcular_ratio(precio, peso):
    return precio / peso


def ordenar_por_ratio(articulos):
    n = len(articulos)

    for i in range(n):
        mayor = i

        for j in range(i + 1, n):
            if articulos[j]["ratio"] > articulos[mayor]["ratio"]:
                mayor = j

        temp = articulos[i]
        articulos[i] = articulos[mayor]
        articulos[mayor] = temp

    return articulos



def main():
    articulos = [
        {"precio": 60, "peso": 10},
        {"precio": 100, "peso": 20},
        {"precio": 120, "peso": 30}
    ]

    capacidad = 50




if __name__ == "__main__":
    main()