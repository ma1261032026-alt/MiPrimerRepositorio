def suma_pares(arreglo):
    total = 0
    for n in arreglo:
        if n % 2 == 0:
            total += n
    return total


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"La suma de los números pares es: {suma_pares(numeros)}")
