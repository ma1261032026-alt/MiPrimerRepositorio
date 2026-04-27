suma_impares = 0
impares_ingresados = []
while True:
    num = int(input("Ingresa un numero (0 para salir):"))
    if num == 0:
        break
    if num % 2 != 0:
        suma_impares += num
impares_ingresados.append(num)

for n in impares_ingresados:
    print(f"impar: {n}")
    print(f"Suma total: {suma_impares}")
