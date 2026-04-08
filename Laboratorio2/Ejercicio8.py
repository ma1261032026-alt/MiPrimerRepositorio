def aplicar_cambio(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    return "Opción no válida"


def menu():
    print("\n--- MENÚ DE TRANSFORMACIÓN ---")
    print("1. Todo a Mayúsculas")
    print("2. Todo a Minúsculas")
    print("3. Primera Letra Mayúscula")

    texto = input("Ingresa el texto: ")
    opcion = int(input("Elige tu opción: "))

    print("Resultado final:", aplicar_cambio(texto, opcion))


# Ejecutar el menú
menu()
