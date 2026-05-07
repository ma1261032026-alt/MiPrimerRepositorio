def encontrar_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor


numeros = []
for i in range(8):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)

print(f"El número mayor es: {encontrar_mayor(numeros)}")
