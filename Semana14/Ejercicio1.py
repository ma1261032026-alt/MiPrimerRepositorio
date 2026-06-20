def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


# Prueba
numeros = [12, 7, 4, 5, 8, 9, 10]
p, i = contar_pares_impares(numeros)
print(f"Pares: {p}, Impares: {i}")
