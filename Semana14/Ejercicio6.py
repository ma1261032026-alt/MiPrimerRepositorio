import random


def contar_mayores_a_50(lista):
    contador = 0
    for n in lista:
        if n > 50:
            contador += 1
    return contador


aleatorios = [random.randint(1, 100) for _ in range(10)]
print(f"Lista generada: {aleatorios}")
print(f"Mayores a 50: {contar_mayores_a_50(aleatorios)}")

#
