def contar_combinaciones(n):
    movimientos = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [0, 5, 7, 8, 9],
        9: [6, 8, 9]
    }

    if n <= 0:
        return 0

    dp = [1] * 10

    for longitud in range(2, n + 1):
        nuevo = [0] * 10

        for digito in range(10):
            for anterior in movimientos[digito]:
                nuevo[digito] += dp[anterior]

        dp = nuevo

    total = 0

    for cantidad in dp:
        total += cantidad

    return total


def mostrar_caso(n):
    resultado = contar_combinaciones(n)
    print("n =", n)
    print("Cantidad total de combinaciones:", resultado)
    print()


def main():
    mostrar_caso(1)
    mostrar_caso(2)
    mostrar_caso(3)
    mostrar_caso(4)


if __name__ == "__main__":
    main()