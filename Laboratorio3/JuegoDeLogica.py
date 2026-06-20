# Laboratorio 3: Juego de Logica

jugar = "si"
while jugar == "si":
    # Esto sirve para separar los juegos
    print("\n" * 5)
    print("--- MI JUEGO DE LOGICA ---")
    print("1. Nivel Facil")
    print("2. Nivel Dificil")

    # 2. MATCH (que es el Select Case) para la dificultad (Requisito)
    opcion = input("Elige nivel 1 o 2: ")

    match opcion:
        case "1":
            print("Sumas:")
            # 3. FOR para hacer 3 preguntas (Requisito)
            for i in range(1, 4):
                respuesta = int(input(f"¿Cuanto es {i} + 10? "))
                # 4. IF para validar (Requisito)
                if respuesta == (i + 10):
                    print("¡Correcto!")
                else:
                    print("Incorrecto")

        case "2":
            print("Multiplicaciones:")
            for i in range(1, 4):
                respuesta = int(input(f"¿Cuanto es {i} * 5? "))
                if respuesta == (i * 5):
                    print("¡Correcto!")
                else:
                    print("Incorrecto")

        case _:
            print("Opcion no valida")

    # Preguntamos si quiere seguir para que el WHILE funcione
    jugar = input("\n¿Quieres jugar otra vez? (si/no): ")

print("Programa finalizado.")
