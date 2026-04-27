positivos = 0
negativos = 0
while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    if num > 0:
        positivos += 1
    else:
        negativos += 1

resumen = [f"Positivos: {positivos}", f"Negativos: {negativos}"]
for r in resumen:
    print(r)
