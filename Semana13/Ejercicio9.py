import random

secreto = random.randint(1, 50)
intentos = []
while True:
    guia = int(input("Adivina (1-50):"))
    intentos.append(guia)
    if guia == secreto:
        print("¡Ganaste!")
        break
    print("Mayor" if guia < secreto else "Menor")

for i in intentos:
    print(f"Intentos: {i}")
