# Listas (arrays) para almacenar los nombres y las notas
nombres = []
notas = []

# Bucle while para mantener el menú funcionando
continuar = True
while continuar:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar estudiantes y sus notas")
    print("2. Mostrar la lista completa de estudiantes")
    print("3. Buscar un estudiante por nombre")
    print("4. Calcular y mostrar el promedio general")
    print("5. Salir del programa")

    opcion = input("Seleccione una opción (1-5): ")

    # Estructura match-case para controlar las opciones del menú
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            # Validación básica para la nota
            try:
                nota = float(input("Ingrese la nota del estudiante (0 a 10): "))
                if 0 <= nota <= 10:
                    nombres.append(nombre)
                    notas.append(nota)
                    print(f"Estudiante {nombre} agregado correctamente.")
                else:
                    print("Error: La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Ingrese un número válido para la nota.")

        case "2":
            if len(nombres) == 0:
                print("No hay estudiantes registrados.")
            else:
                print("\n--- LISTA DE ESTUDIANTES ---")
                # Bucle for para recorrer y mostrar los datos almacenados
                for i in range(len(nombres)):
                    nota_actual = notas[i]

                    # Estructuras if y elif para clasificar el estado del estudiante
                    if 9 <= nota_actual <= 10:
                        estado = "Excelente"
                    elif 7 <= nota_actual < 9:
                        estado = "Aprobado"
                    elif 6 <= nota_actual < 7:
                        estado = "Regular"
                    else:  # Menor a 6
                        estado = "Reprobado"

                    print(
                        f"Nombre: {nombres[i]} | Nota: {nota_actual} | Estado: {estado}"
                    )

        case "3":
            if len(nombres) == 0:
                print("No hay estudiantes registrados para buscar.")
            else:
                busqueda = input("Ingrese el nombre del estudiante a buscar: ")
                encontrado = False

                # Bucle for para buscar en las listas
                for i in range(len(nombres)):
                    if nombres[i].lower() == busqueda.lower():
                        nota_actual = notas[i]

                        # Clasificación de notas para el estudiante buscado
                        if 9 <= nota_actual <= 10:
                            estado = "Excelente"
                        elif 7 <= nota_actual < 9:
                            estado = "Aprobado"
                        elif 6 <= nota_actual < 7:
                            estado = "Regular"
                        else:
                            estado = "Reprobado"

                        print(f"\nEstudiante encontrado:")
                        print(
                            f"Nombre: {nombres[i]} | Nota: {nota_actual} | Estado: {estado}"
                        )
                        encontrado = True
                        break  # Sale del bucle al encontrarlo

                if not encontrado:
                    print(f"El estudiante '{busqueda}' no se encuentra en el sistema.")

        case "4":
            if len(notas) == 0:
                print("No hay notas registradas para calcular el promedio.")
            else:
                suma_notas = 0
                # Bucle for para sumar todas las notas
                for nota in notas:
                    suma_notas += nota

                promedio = suma_notas / len(notas)
                print(f"\nEl promedio general de las notas es: {promedio:.2f}")

        case "5":
            print("Saliendo del programa... ¡Hasta luego!")
            continuar = False

        case _:
            print(
                "Opción no válida. Por favor, intente de nuevo con un número del 1 al 5."
            )
