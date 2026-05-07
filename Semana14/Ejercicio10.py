def ordenar_ascendente(lista):
    n = len(lista)
    # Método Burbuja
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


elementos = []
for i in range(6):
    valor = int(input(f"Ingrese el número {i+1}: "))
    elementos.append(valor)

print(f"Lista ordenada: {ordenar_ascendente(elementos)}")
