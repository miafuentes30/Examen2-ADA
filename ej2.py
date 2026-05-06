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


def knapsack_fraccionado(articulos, capacidad):
    for articulo in articulos:
        articulo["ratio"] = calcular_ratio(articulo["precio"], articulo["peso"])

    articulos = ordenar_por_ratio(articulos)

    solucion = []
    valor_total = 0
    capacidad_restante = capacidad

    for articulo in articulos:
        if capacidad_restante == 0:
            break

        if articulo["peso"] <= capacidad_restante:
            cantidad_tomada = articulo["peso"]
        else:
            cantidad_tomada = capacidad_restante

        valor_obtenido = cantidad_tomada * articulo["ratio"]

        solucion.append({
            "nombre": articulo["nombre"],
            "cantidad_tomada": cantidad_tomada,
            "valor_obtenido": valor_obtenido,
            "ratio": articulo["ratio"]
        })

        valor_total += valor_obtenido
        capacidad_restante -= cantidad_tomada

    return solucion, valor_total


def mostrar_resultado(solucion, valor_total):
    print("Solucion encontrada:")
    print()

    for elemento in solucion:
        print("Articulo:", elemento["nombre"])
        print("Cantidad tomada:", elemento["cantidad_tomada"])
        print("Valor por unidad:", round(elemento["ratio"], 2))
        print("Valor obtenido:", round(elemento["valor_obtenido"], 2))
        print()

    print("Valor total robado:", round(valor_total, 2))


def main():
    articulos = [
        {"nombre": "item 1", "precio": 60, "peso": 10},
        {"nombre": "item 2", "precio": 100, "peso": 20},
        {"nombre": "item 3", "precio": 120, "peso": 30}
    ]

    capacidad = 50

    solucion, valor_total = knapsack_fraccionado(articulos, capacidad)
    mostrar_resultado(solucion, valor_total)


if __name__ == "__main__":
    main()