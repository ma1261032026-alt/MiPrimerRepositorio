notas = []
while True:
    n = float(input("Nota (0-10) o -1 para salir:"))
    if n == -1:
        break
    if 0 <= n <= 10:
        notas.append(n)
suma = 0
for nota in notas:
    suma += nota
    if notas:
        print(f"Promedio: {suma / len(notas)}")
