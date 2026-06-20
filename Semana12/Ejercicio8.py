# Ejercicio 8: Tipos de triángulos
l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if l1 == l2 == l3:
    print("Equilátero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Isósceles")
else:
    print("Escaleno")
